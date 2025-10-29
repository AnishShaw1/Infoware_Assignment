
#!/usr/bin/env python3
import argparse
import os
from pdf_ingest import extract_text
from summarizer import extract_keypoints_and_notes
from slides_builder import build_pptx
from tts_video import make_video_from_pptx

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', required=True, help='input PDF path')
    parser.add_argument('--outdir', '-o', default='output', help='output directory')
    parser.add_argument('--slides-count', type=int, default=8)
    parser.add_argument('--tts', choices=['on','off'], default='on')
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    print("1) Extracting text...")
    pages = extract_text(args.input)

    print("2) Extracting keypoints and speaker notes...")
    slides = extract_keypoints_and_notes(pages, top_n=args.slides_count)

    print("3) Building PPTX...")
    pptx_path = os.path.join(args.outdir, 'slides.pptx')
    build_pptx(slides, pptx_path)

    print("4) Rendering video...")
    video_path = os.path.join(args.outdir, 'video.mp4')
    make_video_from_pptx(pptx_path, slides, video_path, tts=(args.tts=='on'))

    print("Done. Outputs:")
    print(f" - {pptx_path}")
    print(f" - {video_path}")

if __name__ == '__main__':
    main()
