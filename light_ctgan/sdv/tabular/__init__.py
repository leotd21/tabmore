"""Models for tabular data."""

from light_ctgan.sdv.tabular.copulagan import CopulaGAN
from light_ctgan.sdv.tabular.copulas import GaussianCopula
from light_ctgan.sdv.tabular.ctgan import CTGAN, TVAE

__all__ = (
    'GaussianCopula',
    'CTGAN',
    'TVAE',
    'CopulaGAN',
)
