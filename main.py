import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


load_dotenv()


def buscar_notas():
    sessao = requests.Session()
    # Chaves devem ser iguais às do formulário de login
    login_data = {"matricula": os.getenv("MATRICULA"), "password": os.getenv("SENHA")}
    sessao.post(os.getenv("URL"), data=login_data)

    resposta = sessao.get(os.getenv("URL_BOLETIM"))
    sopa = BeautifulSoup(resposta.text, "html.parser")

    # Encontrar todas as tabelas (no meu caso, existem múltiplas tabelas)
    tabelas = sopa.select(".row .conteudo-body .table-responsive")

    for tabela in tabelas:
        # Pular o cabeçalho da tabela
        linhas = tabela.select("tr")[1:]
        for linha in linhas:
            colunas = linha.select("td")
            print(colunas[2].text.strip().ljust(50), end=" ")
            print(colunas[3].text.strip(), end="\t ")
            print(colunas[5].text.strip())


if __name__ == "__main__":
    buscar_notas()
