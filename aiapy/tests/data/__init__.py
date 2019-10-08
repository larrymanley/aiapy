"""
Data used for testing
"""
from astropy.utils.data import get_pkg_data_filename

__all__ = ['get_test_filepath']


def get_test_filepath(filename, **kwargs):
    """
    Return the full path to a test file in the ``data/test`` directory.
    Parameters
    ----------
    filename : `str`
        The name of the file inside the ``data/test`` directory.
    Return
    ------
    filepath : `str`
        The full path to the file.
    Notes
    -----
    This is a wrapper around `astropy.utils.data.get_pkg_data_filename` which
    sets the ``package`` kwarg to be `aiapy.tests.data`.
    """
    return get_pkg_data_filename(filename, package="aiapy.tests.data",
                                 **kwargs)
