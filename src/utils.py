import shutil
from urllib.parse import urlparse


def ffmpeg_instalado() -> bool:
    #True se o FFmpeg esta disponivel no PATH
    return shutil.which("ffmpeg") is not None


DOMINIOS_VALIDOS = {"youtube.com", "www.youtube.com", "m.youtube.com", "music.youtube.com", "youtu.be"}
SCHEMES_VALIDOS = {"http", "https"}
def url_valida(url: str) -> bool:
    # Valida e limpa formato do link, verifica DOMINIOS E SCHEMES
    try:
        url_part = urlparse(url.strip().lower())
    except ValueError:
        return False
    vld_schem = url_part.scheme in SCHEMES_VALIDOS
    vld_dom = url_part.netloc in DOMINIOS_VALIDOS
    return vld_schem and vld_dom

