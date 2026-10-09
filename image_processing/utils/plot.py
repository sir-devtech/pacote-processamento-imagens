import matplotlib.pyplot as plt


def _finish(fig, caminho=None):
    if caminho:
        fig.savefig(caminho, bbox_inches="tight")
        plt.close(fig)
        return
    plt.show()


def plot_image(image, caminho=None):
    fig = plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    _finish(fig, caminho)


def plot_result(*images, caminho=None):
    quantidade = len(images)
    fig, axis = plt.subplots(nrows=1, ncols=quantidade, figsize=(12, 4))
    if quantidade == 1:
        axis = [axis]

    nomes = [f"Imagem {indice}" for indice in range(1, quantidade)]
    nomes.append("Resultado")
    for ax, nome, image in zip(axis, nomes, images):
        ax.set_title(nome)
        ax.imshow(image, cmap="gray")
        ax.axis("off")

    fig.tight_layout()
    _finish(fig, caminho)


def plot_histogram(image, caminho=None):
    if image.ndim != 3 or image.shape[2] < 3:
        raise ValueError("O histograma colorido precisa de uma imagem com canais vermelho, verde e azul.")

    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    cores = ["red", "green", "blue"]
    titulos = ["Vermelho", "Verde", "Azul"]
    for indice, (ax, cor, titulo) in enumerate(zip(axis, cores, titulos)):
        ax.set_title(f"Histograma {titulo}")
        ax.hist(image[:, :, indice].ravel(), bins=256, color=cor, alpha=0.8)

    fig.tight_layout()
    _finish(fig, caminho)
