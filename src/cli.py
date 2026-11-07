import argparse

def criar_parser() -> argparse.ArgumentParser:
    """Cria o leitor de argumentos da linha de comando"""
    parser = argparse.ArgumentParser(prog='yt-downloader', description='Baixa vídeos e áudio do YouTube')
    parser.add_argument('url', help='URL do video do Youtube')
    parser.add_argument('-a', '--audio', action='store_true', help='Baixar apenas o áudio, em MP3 (sem a flag, baixa o vídeo)')
    parser.add_argument('-o','--output', default='downloads', help='Pasta onde os arquivos serão salvos (padrão: %(default)s)')

    return parser
