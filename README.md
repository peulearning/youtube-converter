# YouTube to MP3/MP4 Converter

Este projeto é uma aplicação web que permite aos usuários converter vídeos do YouTube em arquivos MP3 ou MP4. Foi construído usando Flask para o backend e HTML para o frontend.

## Funcionalidades

- Converte vídeos do YouTube para MP3 ou MP4.
- Interface simples e fácil de usar.

## Tecnologias Utilizadas

- **Backend**: Flask
- **Bibliotecas Python**:
  - `pytube` para baixar vídeos do YouTube.
  - `moviepy` para converter vídeos em MP3.
- **Frontend**: HTML, CSS

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Configuração

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/youtube-converter.git
    cd youtube-converter
    ```

2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:
    - **Linux/Mac**:
      ```bash
      source venv/bin/activate
      ```
    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Inicie o servidor Flask:
    ```bash
    python app.py
    ```

6. Abra o navegador e acesse `http://localhost:5000`.

## Uso

1. Insira a URL do vídeo do YouTube no campo fornecido.
2. Selecione o formato desejado (MP3 ou MP4).
3. Clique em "Convert".
4. Baixe o arquivo convertido usando o link gerado.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

## Contribuição

1. Faça um fork do projeto.
2. Crie um branch para sua feature (`git checkout -b feature/fooBar`).
3. Faça commit das suas alterações (`git commit -am 'Add some fooBar'`).
4. Envie para o branch (`git push origin feature/fooBar`).
5. Crie um novo Pull Request.

## Contato

- Autor: Seu Nome
- Email: seuemail@dominio.com
