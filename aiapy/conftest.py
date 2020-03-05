import pytest
import hissw
import astropy.units as u
import sunpy.map
import sunpy.data.test
from astropy.version import version as astropy_version
if astropy_version < '3.0':
    # For older versions of astropy
    from astropy.tests.pytest_plugins import *
else:
    from astropy.tests.plugins.display import (PYTEST_HEADER_MODULES,
                                               TESTED_VERSIONS)
from astropy.tests.helper import enable_deprecations_as_exceptions


@pytest.fixture
def aia_171_map():
    m = sunpy.map.Map(sunpy.data.test.get_test_filepath('aia_171_level1.fits'))
    # For testing purposes, need the map to be 4K-by-4K
    return m.resample((4096, 4096)*u.pixel)


@pytest.fixture(scope='session')
def idl_environment():
    if idl_available():
        return hissw.Environment(ssw_packages=['sdo/aia'], ssw_paths=['aia'])
    else:
        pytest.skip('''A working IDL installation is not available. You will
                       not be able to run portions of the test suite.''')


@pytest.fixture(scope='session')
def ssw_home():
    if idl_available():
        return hissw.Environment().ssw_home
    else:
        return None


def idl_available():
    try:
        _ = hissw.Environment().run('')
    except (FileNotFoundError, ValueError):
        return False
    else:
        return True
