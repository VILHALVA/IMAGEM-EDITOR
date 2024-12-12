# CUSTOMTKINTER IMAGE EDITOR
👨‍🏫ESSE APLICATIVO OFERECE UMA MANEIRA SIMPLES DE ADICIONAR TEXTOS PERSONALIZADOS ÀS SUAS IMAGENS.

<img src="./IMAGENS/FOTO_1.png" align="center" width="500"> <br>
<img src="./IMAGENS/FOTO_2.png" align="center" width="500"> <br>

## DESCRIÇÃO:
Esse aplicativo é um editor de imagens simples utilizando o `customtkinter` e a biblioteca `PIL` (Pillow) para manipulação de imagens. O objetivo é permitir que o usuário adicione um texto personalizado sobre uma imagem, configure o estilo do texto (como cor, tamanho e posição), e depois salve a imagem modificada.

## FUNCIONALIDADES:
1. **Selecionar Imagem**: O usuário pode selecionar uma imagem do seu computador para editar.
2. **Inserir Texto**: O usuário pode digitar o texto que deseja adicionar à imagem. O texto pode ser configurado com:
   - **Cor do texto**: Escolha entre "branco", "vermelho", "verde" ou "azul".
   - **Cor de fundo do texto**: Escolha entre "branco", "vermelho", "verde" ou "azul".
   - **Tamanho da fonte**: Escolha entre tamanhos predefinidos de 20px até 200px.
   - **Posição do texto**: O texto pode ser posicionado no topo, no centro ou na parte inferior da imagem.
3. **Salvar Imagem**: Após editar a imagem, o usuário pode salvar a imagem com o texto sobreposto em um novo arquivo.

## RECURSOS:
- **Seleção de Imagem**: O código usa o `filedialog.askopenfilename()` para abrir a janela de seleção de arquivo. O arquivo selecionado deve ser uma imagem (extensões `.png`, `.jpg`, `.jpeg`).
- **Adição de Texto**: O texto é desenhado na imagem usando o `ImageDraw.Draw()`, e a cor e o tamanho da fonte são configuráveis. O código tenta carregar a fonte `arial.ttf` e, caso não a encontre, utiliza a fonte padrão do sistema.
- **Posição do Texto**: A posição do texto na imagem é determinada pelo valor selecionado (Top, Center, Bottom). O código calcula as coordenadas para centralizar ou posicionar o texto conforme a opção escolhida.
- **Salvamento de Imagem**: O usuário pode salvar a imagem editada em um novo local usando o `filedialog.asksaveasfilename()`, que oferece a possibilidade de salvar no formato PNG.
- **Interface Gráfica**: A interface é construída com `customtkinter`, proporcionando uma aparência mais moderna e configurável.
- **Manipulação de Imagens**: A biblioteca `PIL` é utilizada para abrir, modificar e salvar a imagem.
- **Feedback ao Usuário**: A interface usa caixas de mensagem (`messagebox`) para dar feedback ao usuário sobre ações como selecionar ou salvar uma imagem, ou quando ocorrem erros.

## EXECUTANDO ESSE PROJETO:
1. **Instalação das Dependências::**
   - Entre no diretório `CODIGO` e execute o comando:

   ```bash
   pip install -r requirements.txt
   ```

2. **Execução do Aplicativo:**
   - Para executar o arquivo Python, utilize o comando abaixo no terminal, dentro do diretório `./CODIGO`:
   ```bash
   python CODIGO.py
   ```

3. **Selecionar Imagem**: 
   - Clique no botão "SELECIONAR" para abrir uma janela de seleção de arquivos e escolher uma imagem.

4. **Digite o Texto**: 
   - No campo "DIGITE O TEXTO", insira o texto que deseja adicionar à imagem. O texto inicial é "CUSTOMTKINTER".

5. **Configure o Estilo do Texto**:
   - Selecione a cor do texto desejada.
   - Escolha a cor do fundo do texto.
   - Selecione o tamanho da fonte.
   - Defina a posição do texto (Top, Center, ou Bottom).

6. **Salvar Imagem**: 
   - Após configurar o texto, clique no botão "SALVAR" para escolher o local onde deseja salvar a imagem editada.

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE CUSTOMTKINTER](https://github.com/VILHALVA/CURSO-DE-CUSTOMTKINTER)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)





