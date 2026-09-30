from pathlib import Path
import argparse
import asyncio
import edge_tts

async def synthesize(input_path: str, output_path: str, voice: str, rate: str, pitch: str):
    text = Path(input_path).read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("O roteiro está vazio.")
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate, pitch=pitch)
    await communicate.save(output_path)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="roteiros/teste.txt")
    p.add_argument("--output", default="output/teste-antonio.mp3")
    p.add_argument("--voice", default="pt-BR-AntonioNeural")
    p.add_argument("--rate", default="-5%")
    p.add_argument("--pitch", default="+0Hz")
    a = p.parse_args()
    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    asyncio.run(synthesize(a.input, a.output, a.voice, a.rate, a.pitch))

if __name__ == "__main__":
    main()
