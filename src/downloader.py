from pathlib import Path

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError as YtDlpDownloadError

class DownloadError(Exception):
    """Erro de download com mensagem pronta para o usuário."""

def _opcoes_base(pasta: str) -> dict:
    """Cria a pasta e devolve opções comuns"""
    Path(pasta).mkdir(parents=True, exist_ok=True)
    return {
        "outtmpl": str(Path(pasta) / "%(title)s.%(ext)s"),
        "noplaylist": True,
    }
def _baixar(url: str, opcoes: dict) -> None:
    """Baixa o vídeo da URL com as opções dadas; levanta DownloadError se falhar."""
    try:
        with YoutubeDL(opcoes) as ydl:
            ydl.download([url])
    except YtDlpDownloadError as err:
        raise DownloadError(str(err)) from err
    return None
def baixar_video(url: str, pasta: str = 'downloads') -> None:
    """Baixa o vídeo da URL em MP4, na melhor qualidade"""
    opcoes = _opcoes_base(pasta)
    opcoes.update({
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4'    # verificar extensao se cair no caso /best (sem merge)
    })
    _baixar(url, opcoes)
