from pathlib import Path
import argparse

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--ref", required=True)
    p.add_argument("--text", required=True)
    p.add_argument("--out", required=True)
    args=p.parse_args()

    from TTS.api import TTS

    text=Path(args.text).read_text(encoding="utf-8").strip()
    tts=TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
    tts.tts_to_file(
        text=text,
        speaker_wav=args.ref,
        language="pt",
        file_path=args.out,
        split_sentences=True,
    )

if __name__=="__main__":
    main()
