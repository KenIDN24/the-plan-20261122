"""Rencana 30 hari: ubah $100 menjadi sebanyak mungkin.

Skrip kecil ini menyimpan teks rencana final ke /output/entry.txt.
Dijalankan ulang berapa kali pun, hasilnya sama persis.
Catatan: tidak ada argumen baris perintah dan tidak ada efek samping
selain menulis file keluaran tersebut.
"""

from pathlib import Path

PLAN = (
    "Day 1: post a $49 'landing page in 24h' service on Fiverr and Contra. "
    "Then DM 30 Google Maps businesses with a free AI-made homepage mockup "
    "of their shop; close 2 a day. Reinvest only profits into more mockups. "
    "Likely day 30: $800-$1,500, $100 kept as float."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
