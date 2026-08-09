import requests
from pathlib import Path


class DownloaderPDF:
    def __init__(self, destino, url, arquivo):
        destino.mkdir(exist_ok=True)
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "")
        if "application/pdf" not in content_type:
            raise ValueError(f"A resposta não parece ser PDF: {content_type}")
        caminho = destino /arquivo
        caminho.write_bytes(response.content)
        print(caminho)
