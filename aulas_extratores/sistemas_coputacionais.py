from pathlib import Path
from downloader import DownloaderPDF
from typing import NoReturn


def inicializador() -> NoReturn:

    destino: Path = Path("Sistemas Computacionais (univesp)/")
    destino.mkdir(exist_ok=True)
    i: int = 1
    while True:
        if i < 10:
            text: str = str(f"0{i}")
        else:
            text: str = i
        print(f"Slide da aula baixado{i}")
        url = f"https://assets.univesp.br/disciplinas/COM210/pdf/slide-videoaula-{text}.pdf"
        arquivo = f"Aula({text}).pdf"
        DownloaderPDF(destino=destino, arquivo=arquivo, url=url)
        i += 1
