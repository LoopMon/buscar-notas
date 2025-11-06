# 📊 Buscador de Notas Automático

Este projeto é um script em **Python** que acessa automaticamente o portal acadêmico de um aluno, realiza o login e extrai suas **notas** diretamente da página do boletim.
Ele utiliza as bibliotecas **Requests** e **BeautifulSoup** para realizar a autenticação e o scraping dos dados, e **dotenv** para gerenciar informações sensíveis (como matrícula e senha) de forma segura.

## 🚀 Funcionalidades

* Faz login automático no sistema acadêmico.
* Coleta e exibe as notas diretamente no terminal.
* Utiliza variáveis de ambiente para proteger informações pessoais.

## 🧰 Tecnologias Utilizadas

* **Python 3.10+**
* [Requests](https://pypi.org/project/requests/) — para fazer requisições HTTP.
* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) — para extrair e processar os dados HTML.
* [python-dotenv](https://pypi.org/project/python-dotenv/) — para gerenciar variáveis de ambiente.

## ⚙️ Configuração do Ambiente

### 1. Clone este repositório

```bash
git clone https://github.com/LoopMon/buscar-notas.git
cd buscar-notas
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Se ainda não tiver o arquivo `requirements.txt`, você pode gerá-lo com:
>
> ```bash
> pip freeze > requirements.txt
> ```

## 🔐 Configuração das Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```env
URL=https://exemplo.com/login
URL_BOLETIM=https://exemplo.com/boletim
MATRICULA=seu_usuario_aqui
SENHA=sua_senha_aqui
```

> ⚠️ **Importante:** nunca envie o arquivo `.env` para o GitHub!
> Adicione-o ao seu `.gitignore` para manter seus dados protegidos.

## ▶️ Como Executar

Depois de configurar o `.env`, execute o script com:

```bash
python main.py
```

O programa exibirá algo semelhante a:

```
Programação Web       8.5   7.5
Banco de Dados        9.0   6.9
Estrutura de Dados    7.5   9.5
```

## 🧠 Como Funciona

1. O script cria uma **sessão HTTP** com `requests.Session()`.
2. Realiza o **login** enviando `MATRICULA` e `SENHA` para o `URL` de autenticação.
3. Acessa o `URL_BOLETIM` e coleta os dados HTML.
4. Usa o **BeautifulSoup** para localizar as tabelas com as notas.
5. Exibe as informações (matéria, nota) formatadas no terminal.

## ✨ Autor

Desenvolvido por **João Lucas**

🐙 GitHub: [@loopmon](https://github.com/loopmon)
