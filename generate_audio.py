#!/usr/bin/env python3
"""Buat suara perempuan (Microsoft Neural, id-ID-GadisNeural) untuk semua teks di stories.json.

Cara pakai:
    pip install edge-tts
    python generate_audio.py

Hasilnya masuk ke folder audio/ (satu mp3 per kalimat cerita dan per pertanyaan).
Jalankan lagi setelah mengubah stories.json: hanya teks yang berubah yang dibuat ulang.

Ingin suara lain? Ganti VOICE / RATE di bawah. Untuk layanan resmi berbayar-gratis-terbatas
(Azure Speech, Google Cloud Text-to-Speech, ElevenLabs), cukup ganti isi fungsi synth().
"""
import asyncio
import hashlib
import json
import pathlib

import edge_tts

VOICE = "id-ID-GadisNeural"   # perempuan. Laki-laki: id-ID-ArdiNeural
RATE = "-12%"                 # sedikit lebih lambat supaya mudah diikuti anak

root = pathlib.Path(__file__).parent
out = root / "audio"
out.mkdir(exist_ok=True)
hash_file = out / "hash.json"
old = json.loads(hash_file.read_text()) if hash_file.exists() else {}

items = {"ok": "Hebat!", "done": "Selesai! Kamu hebat."}
data = json.loads((root / "stories.json").read_text(encoding="utf-8"))
for s in data["stories"]:
    for i, t in enumerate(s["s"]):
        items[f'{s["id"]}_s{i}'] = t
    for i, q in enumerate(s["qs"]):
        items[f'{s["id"]}_q{i}'] = q["q"]


async def synth(text, path):
    await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(path))


async def main():
    new = {}
    for name, text in items.items():
        h = hashlib.md5((VOICE + RATE + text).encode()).hexdigest()
        new[name] = h
        f = out / f"{name}.mp3"
        if f.exists() and old.get(name) == h:
            continue
        print("membuat", name, "-", text)
        await synth(text, f)
    hash_file.write_text(json.dumps(new, indent=1))
    print("selesai:", len(items), "file di", out)


asyncio.run(main())
