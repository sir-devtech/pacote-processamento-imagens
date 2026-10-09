import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def find_difference(image1, image2):
    if image1.shape != image2.shape:
        raise ValueError("As duas imagens precisam ter o mesmo tamanho.")

    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    score, difference_image = structural_similarity(
        gray_image1,
        gray_image2,
        full=True,
        data_range=1.0,
    )
    print(f"Similaridade das imagens: {score:.4f}")

    amplitude = np.max(difference_image) - np.min(difference_image)
    if amplitude == 0:
        return np.zeros_like(difference_image)

    return (difference_image - np.min(difference_image)) / amplitude


def transfer_histogram(image1, image2):
    if image1.ndim != image2.ndim:
        raise ValueError("As duas imagens precisam ter o mesmo número de canais.")
    return match_histograms(image1, image2, channel_axis=-1 if image1.ndim == 3 else None)
