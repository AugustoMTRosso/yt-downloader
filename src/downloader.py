from pathlib import Path

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError as YtDlpDownloadError

class DownloadError(Exception):
    """Erro de download com mensagem pronta para o usuário."""

def _opcoes_base(pasta: str) -> dict:
    """Cria a pasta e devolve opções comuns."""
    Path(pasta).mkdir(parents=True, exist_ok=True)
    return {
        'outtmpl': str(Path(pasta) / '%(title)s.%(ext)s'),
        'noplaylist': True,
    }

def _baixar(url: str, opcoes: dict) -> None:
    """Baixa a URL com as opções dadas; levanta DownloadError se falhar."""
    try:
        with YoutubeDL(opcoes) as ydl:
            ydl.download([url])
    except YtDlpDownloadError as err:
        raise DownloadError(str(err)) from err

def baixar_video(url: str, pasta: str = 'downloads') -> None:
    """Baixa o vídeo da URL em MP4, na melhor qualidade."""
    opcoes = _opcoes_base(pasta)
    opcoes.update({
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',           #Verificar extensão se cair no caso /best (sem merge)
    })
    _baixar(url, opcoes)

def baixar_audio(url: str, pasta: str = 'downloads') -> None:
    """Baixa áudio da URL em MP3, na melhor qualidade, embutindo capa."""
    opcoes = _opcoes_base(pasta)
    opcoes.update({
        'format': 'bestaudio/best',
        'writethumbnail': True,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',    #Converte p mp3 com preferredcodec
                'preferredcodec': 'mp3',
                'preferredquality': '192',      #128min ,320 max
            },
            {
                'key': 'EmbedThumbnail',        #Embute capa
            }
        ]
    })
    _baixar(url, opcoes)
