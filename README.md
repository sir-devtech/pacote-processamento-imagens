# sirtech-imagens

Pacote de processamento de imagens do desafio **Criando um Pacote de Processamento de Imagens com Python**, da [DIO](https://www.dio.me/). A organização segue a aula: processamento de um lado, leitura e visualização do outro.

O nome de instalação é `sirtech-imagens`. No código, o import continua `image_processing`.

## O que o pacote faz

- **processing.combination**: mede a diferença estrutural entre duas imagens do mesmo tamanho e transfere o histograma de uma para a outra.
- **processing.transformation**: redimensiona a imagem por uma proporção entre 0 e 1.
- **utils.io**: lê e salva a imagem.
- **utils.plot**: mostra a imagem, o resultado lado a lado e o histograma dos canais. Se você passar um caminho, a figura é gravada em PNG em vez de abrir uma janela.

A transferência de histograma usa `channel_axis=-1`. O parâmetro antigo `multichannel=True` não existe mais nas versões atuais do scikit-image.

## Como instalar a partir deste repositório

```bash
pip install .
```

## Como gerar as distribuições

Na raiz do projeto:

```bash
python -m pip install build
python -m build
```

Isso cria o arquivo fonte (`sdist`) e o `wheel` na pasta `dist`.

Publicar no PyPI pede uma conta sua e o comando `twine upload dist/*`. Este repositório entrega o pacote pronto para isso. O envio ao PyPI não faz parte da entrega na DIO.

## Exemplo

```python
from image_processing.processing.transformation import resize_image
from image_processing.utils.io import read_image, save_image

imagem = read_image("foto.png")
menor = resize_image(imagem, 0.5)
save_image(menor, "foto_menor.png")
```

## Autor

Moisés Santos de Oliveira, [Sir Tech Solutions](https://sirtechsolutions.com.br).
