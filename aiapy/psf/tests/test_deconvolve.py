"""
Test deconvolution
"""
import pytest
import aiapy.psf
import sunpy.data.test
import sunpy.map


def test_deconvolve(aia_171_map):
    # Skip this test if cupy is not installed because it is too
    # slow. This is mostly for the benefit of the CI.
    try:
        import cupy
    except ImportError:
        pytest.skip('Cannot import cupy. Skipping deconvolution test with full PSF')
    map_decon = aiapy.psf.deconvolve(aia_171_map, iterations=1)
    assert isinstance(map_decon, sunpy.map.GenericMap)
    assert map_decon.data.shape == aia_171_map.data.shape


def test_deconvolve_specify_psf(aia_171_map, psf):
    map_decon = aiapy.psf.deconvolve(aia_171_map, psf=psf, iterations=1)
    assert isinstance(map_decon, sunpy.map.GenericMap)
    assert map_decon.data.shape == aia_171_map.data.shape
