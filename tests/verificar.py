import tempfile
from pathlib import Path

import numpy as np

from image_processing.processing.combination import find_difference, transfer_histogram
from image_processing.processing.transformation import resize_image
from image_processing.utils.io import read_image, save_image
from image_processing.utils.plot import plot_histogram, plot_result


def main():
    gerador = np.random.default_rng(7)
    original = gerador.integers(0, 255, size=(40, 60, 3), dtype=np.uint8)
    referencia = gerador.integers(0, 255, size=(40, 60, 3), dtype=np.uint8)

    with tempfile.TemporaryDirectory() as pasta:
        pasta = Path(pasta)
        caminho = pasta / "original.png"
        save_image(original, caminho)
        carregada = read_image(caminho)
        if carregada.shape != original.shape:
            raise SystemExit(f"leitura mudou o formato: {carregada.shape}")

        reduzida = resize_image(carregada, 0.5)
        if reduzida.shape[0] != 20 or reduzida.shape[1] != 30:
            raise SystemExit(f"redimensionamento inesperado: {reduzida.shape}")

        try:
            resize_image(carregada, 0)
            raise SystemExit("proporção 0 deveria falhar")
        except ValueError:
            pass

        transferida = transfer_histogram(carregada, referencia)
        if transferida.shape != carregada.shape:
            raise SystemExit(f"histograma mudou o formato: {transferida.shape}")

        diferenca = find_difference(carregada, carregada)
        if diferenca.shape[:2] != carregada.shape[:2]:
            raise SystemExit(f"diferença com formato inesperado: {diferenca.shape}")

        try:
            find_difference(carregada, carregada[:20])
            raise SystemExit("imagens de tamanhos diferentes deveriam falhar")
        except ValueError:
            pass

        histograma = pasta / "histograma.png"
        resultado = pasta / "resultado.png"
        plot_histogram(carregada, caminho=histograma)
        plot_result(carregada, transferida, caminho=resultado)
        if not histograma.is_file() or histograma.stat().st_size == 0:
            raise SystemExit("histograma não foi gravado")
        if not resultado.is_file() or resultado.stat().st_size == 0:
            raise SystemExit("resultado não foi gravado")

    print("verificacao ok")


if __name__ == "__main__":
    main()
