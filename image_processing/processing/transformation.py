from skimage.transform import resize


def resize_image(image, proportion):
    if not 0 < proportion <= 1:
        raise ValueError("Informe uma proporção maior que 0 e no máximo 1.")

    height = max(1, round(image.shape[0] * proportion))
    width = max(1, round(image.shape[1] * proportion))
    return resize(image, (height, width), anti_aliasing=True)
