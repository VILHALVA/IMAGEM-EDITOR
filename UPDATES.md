# [ATUALIZAÇÕES:](./UPDATES.md#vers%C3%A3o-10---31072024)

## VERSÃO 1.1 - 15/08/2025:
* ✅**Novo nome do app**: Antes chamado `CUSTOMTKINTER IMAGEM EDITOR`, agora é apenas `IMAGEM EDITOR`.
* ✅**Interface aprimorada**:
  * 🔹Título adicionado: `EDITOR DE IMAGENS`.
  * 🔹Placeholder do campo de texto alterado de `CUSTOMTKINTER` para `EDITADO`.
  * 🔹Botões de rádio alinhados em **uppercase** nos seus respectivos containers.
  * 🔹O app inicia com **zoom total** e agora suporta **rolagem vertical**.
* ✅**Botão principal atualizado**: O antigo `"SALVAR"` foi renomeado para `"EDITAR"` e agora permanece **desabilitado** até que um diretório seja selecionado.
* ✅**Botões reorganizados**: `"SELECIONAR"` (agora `"DIRETÓRIO"`) e `"EDITAR"` estão lado a lado.
* ✅**Status e progresso**: Adicionados um **campo de status** e uma **barra de progresso** que mostram, em tempo real, o diretório selecionado e o andamento da conversão.
* ✅**Seleção de pasta**: O usuário agora escolhe uma pasta inteira em vez de arquivos individuais, e as imagens editadas são salvas automaticamente em uma subpasta chamada `IMAGEM_EDITOR`.
* ✅**Ignorar arquivos ocultos e de sistema**: Arquivos ocultos ou do sistema são automaticamente ignorados durante a conversão, mesmo que estejam visíveis no Explorador do Windows.
* ✅Foi criado o `INSTALADOR`.
---

## VERSÃO 1.0 - 12/12/2024:
* ✅O aplicativo é um editor de imagens simples desenvolvido com `customtkinter` e `PIL` (Pillow), que permite ao usuário adicionar texto personalizado sobre uma imagem, configurando cor, tamanho, posição e cor de fundo do texto. É possível escolher a imagem a partir do computador, ajustar o estilo do texto (com opções de cores predefinidas, tamanhos de 20px a 200px e posições no topo, centro ou base da imagem) e salvar o resultado em um novo arquivo, preferencialmente no formato PNG. A interface gráfica moderna oferece seleção de arquivo, inserção e posicionamento do texto com cálculo automático das coordenadas, além de feedback ao usuário por meio de caixas de mensagem. O sistema tenta usar a fonte `arial.ttf` e recorre à fonte padrão caso não a encontre, garantindo funcionalidade mesmo em ambientes diferentes.
