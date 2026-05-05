# [READ.md.txt](https://github.com/user-attachments/files/27410964/READ.md.txt)

1. Organização dos Arquivos

Certifique-se de que todos os seus arquivos (main.py, services.py, repositories.py, etc.) estão dentro da mesma pasta no seu computador.

2. Preparação do Ambiente

(Terminal)Abra o terminal (ou CMD) diretamente nessa pasta. É recomendável criar um ambiente virtual para não misturar as bibliotecas com as do seu sistema:Criar: python -m venv venvAtivar (Windows): .\venv\Scripts\activateAtivar (Linux/Mac): source venv/bin/activate

3. Instalação das Ferramentas

Você só precisa instalar dois pacotes principais:FastAPI: O framework da sua API.Uvicorn: O servidor que vai "segurar" a API no ar para receber os acessos.Comando: pip install fastapi uvicorn

4. Execução do Servidor

Com o ambiente pronto, digite o seguinte comando:bashuvicorn main:app --reload
Use o código com cuidado.main: É o nome do seu arquivo principal (se o seu arquivo se chamar api.py, mude para api:app).app: É o nome da variável que você criou dentro do código (ex: app = FastAPI()).--reload: Serve para que a API reinicie sozinha toda vez que você salvar uma alteração no código.

5. Como Testar

Assim que o comando rodar, ele indicará um endereço (geralmente http://127.0.0.1:8000).Para testar visualmente, adicione /docs ao final do endereço no seu navegador.Lá, o FastAPI abrirá uma página interativa onde você pode clicar nos botões POST, GET, PUT e DELETE, preencher os campos e clicar em "Execute" para ver se o seu banco SQLite está salvando e retornando os produtos corretamente.
