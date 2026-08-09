import requests
from pathlib import Path

destino:Path = Path("Banco de Dados (univesp)/")
destino.mkdir(exist_ok=True)
i:int=1
while i <=9:

    if i < 10:
        text:str = str(f"0{i}")
    else:
        text:str = i
    print(f"Slide da aula baixado{i}")
    url = f"https://assets.univesp.br/disciplinas/COM300/pdf/s{aula}_slides_videoaula{i}.pdf"
    response = requests.get(url, timeout=60)
    response.raise_for_status()

    content_type = response.headers.get("Content-Type", "")

    if "application/pdf" not in content_type:
        raise ValueError(
            f"A resposta não parece ser PDF: {content_type}"
        )

    arquivo = destino / f"Aula({text}).pdf"

    arquivo.write_bytes(response.content)
    i += 1

print(arquivo)