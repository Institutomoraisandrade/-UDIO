from pathlib import Path
import argparse

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--ref", required=True)
    p.add_argument("--text", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--speed", type=float, default=1.03)
    args=p.parse_args()

    from f5_tts.api import F5TTS

    model=F5TTS(
        device="cpu",
        ckpt_file="hf://Cataldir/F5-TTS-pt-br/model_last.safetensors",
        vocab_file="hf://Cataldir/F5-TTS-pt-br/vocab.txt",
    )
    text=Path(args.text).read_text(encoding="utf-8").strip()
    model.infer(
        ref_file=args.ref,
        ref_text="",
        gen_text=text,
        file_wave=args.out,
        speed=args.speed,
        remove_silence=True,
    )

if __name__=="__main__":
    main()
