from pathlib import Path

from setuptools import find_packages, setup

readme = Path(__file__).with_name("README.md").read_text(encoding="utf-8")

setup(
    name="sirtech-imagens",
    version="0.1.0",
    author="Moisés Santos de Oliveira",
    author_email="moises@gcmsistema.com.br",
    description="Redimensiona imagens, transfere histograma e mede a diferença estrutural.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/sir-devtech/pacote-processamento-imagens",
    packages=find_packages(),
    install_requires=[
        "numpy==2.5.3",
        "scikit-image==0.26.0",
        "matplotlib==3.11.2",
    ],
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
