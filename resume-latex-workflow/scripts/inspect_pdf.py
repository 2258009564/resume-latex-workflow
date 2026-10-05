"""Render a resume PDF and report bounds, fonts and links. Requires PyMuPDF."""
import argparse
import json
from pathlib import Path
import fitz


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    report = {'pages': []}
    with fitz.open(args.pdf) as doc:
        for index, page in enumerate(doc):
            spans = [s for b in page.get_text('dict')['blocks'] if 'lines' in b
                     for line in b['lines'] for s in line['spans']]
            outside = [s['text'] for s in spans if not page.rect.contains(fitz.Rect(s['bbox']))]
            fonts = []
            for font in page.get_fonts():
                xref = font[0]
                embedded = bool(doc.extract_font(xref)[3]) if xref else False
                fonts.append({'name': font[3], 'embedded': embedded})
            preview = args.output / f'page-{index + 1}.png'
            page.get_pixmap(matrix=fitz.Matrix(3, 3)).save(preview)
            report['pages'].append({'page': index + 1, 'size': list(page.rect),
                                    'has_selectable_text': bool(page.get_text().strip()),
                                    'text_outside_page': outside, 'fonts': fonts,
                                    'links': [l.get('uri') for l in page.get_links() if l.get('uri')],
                                    'preview': preview.name})
    (args.output / 'inspection.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'pages': len(report['pages']), 'report': str(args.output / 'inspection.json')}))


if __name__ == '__main__':
    main()
