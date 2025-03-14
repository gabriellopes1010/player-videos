# Player de Vídeos - Full Cycle 3.0

Este projeto é um player de vídeos desenvolvido para o curso Full Cycle 3.0. Ele permite a navegação entre módulos, seções e vídeos, além de oferecer funcionalidades como alternar entre temas claro e escuro, salvar notas e ajustar o tamanho da fonte.

## Funcionalidades

- **Navegação entre vídeos**: Permite navegar entre vídeos de diferentes módulos e seções.
- **Alternar tema**: Alterna entre temas claro e escuro.
- **Salvar notas**: Salva notas do usuário localmente e permite o download das notas em formato `.txt`.
- **Ajuste de fonte**: Permite aumentar ou diminuir o tamanho da fonte.

## Instalação

1. Clone o repositório:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd player-videos
    ```

2. Instale as dependências:
    ```sh
    npm install
    ```

3. Inicie a aplicação:
    ```sh
    npm start
    ```

## Uso

- Acesse a aplicação em `http://localhost:3000`.
- Navegue pelos módulos e seções para selecionar um vídeo.
- Use os botões "Anterior" e "Próximo" para navegar entre os vídeos.
- Use o botão "Alternar Tema" para mudar entre os temas claro e escuro.
- Salve suas notas usando o botão "Salvar Notas".
- Ajuste o tamanho da fonte usando os botões "A-" e "A+".

## Desenvolvimento

### Debugging

Para depurar a aplicação, você pode usar as configurações do Visual Studio Code definidas em `.vscode/launch.json`.

### Docker

A aplicação pode ser executada em um contêiner Docker. Use o arquivo `compose.yaml` para configurar e iniciar os serviços necessários.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
