from typing import NoReturn
from pathlib import Path
from downloader import DownloaderPDF


def inicializador() -> NoReturn:
    aula_caminho = "Banco de Dados (univesp)"
    destino: Path = Path(f"{aula_caminho}/")
    destino.mkdir(exist_ok=True)
    i: int = 1
    while True:
        if i < 10:
            text: str = str(f"0{i}")
        else:
            text: str = i
        print(f"Slide da aula {aula_caminho} baixado {text}")
        semana = (i + 2) // 3
        url = f"https://assets.univesp.br/disciplinas/COM300/pdf/s{semana}_slides_videoaula{i}.pdf"

        arquivo = f"Aula({text}).pdf"
        DownloaderPDF(destino=destino, url=url, arquivo=arquivo)
        i += 1
