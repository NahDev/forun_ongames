# forun_ongames
# Documentação do Projeto Django

Este é o guia passo a passo para executar o projeto Django localmente em seu ambiente de desenvolvimento. Siga as instruções abaixo para configurar o ambiente e iniciar o projeto.

## Pré-requisitos

Antes de começar, verifique se o seu sistema possui os seguintes requisitos instalados:

- Python 3 (versão 3.6 ou superior)
- Pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado para isolar o ambiente)

## Configurando o Ambiente

1. Clone este repositório para o seu ambiente local ou faça o download dos arquivos.

2. Navegue até o diretório do projeto no terminal.

3. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   virtualenv env
   ```

4. Ative o ambiente virtual:

   - No Windows:

     ```bash
     env\Scripts\activate
     ```

   - No macOS e Linux:

     ```bash
     source env/bin/activate
     ```

5. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

6. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

7. Crie um superusuário para acessar a área de administração (opcional):

   ```bash
   python manage.py createsuperuser
   ```

## Executando o Projeto

Agora que o ambiente está configurado, você pode iniciar o servidor de desenvolvimento do Django e acessar o projeto em seu navegador.

1. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

2. Abra o navegador e visite `http://localhost:8000/` para acessar o projeto.

3. Se você criou um superusuário, pode acessar a área de administração em `http://localhost:8000/admin/`.

## Contribuição

Se você quiser contribuir para este projeto, siga as etapas abaixo:

1. Faça um fork deste repositório e clone-o para o seu ambiente local.

2. Crie uma nova branch para suas alterações:

   ```bash
   git checkout -b nome-da-sua-branch
   ```

3. Faça as alterações desejadas e faça commit das mesmas:

   ```bash
   git commit -m "Descrição das alterações"
   ```

4. Envie as alterações para o repositório remoto:

   ```bash
   git push origin nome-da-sua-branch
   ```

5. Abra uma solicitação pull no GitHub para revisar suas alterações.

## Problemas Comuns

- Se você encontrar algum problema durante a execução do projeto, verifique se os pré-requisitos estão instalados corretamente e se as dependências foram instaladas sem erros.
- Certifique-se de que as migrações do banco de dados foram executadas corretamente antes de iniciar o servidor.
- Se ocorrerem erros relacionados a portas em uso, você pode alterar a porta do servidor de desenvolvimento adicionando o número da porta após o comando `runserver`, por exemplo: `python manage.py runserver 8080`.

---

Agora você está pronto para executar o projeto Django em seu ambiente local. Divirta-se desenvolvendo!
