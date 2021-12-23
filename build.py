from Cython.Build import cythonize
from setuptools import Extension


# This function will be executed in setup.py:
def build(setup_kwargs):
    # The PyQualicision extension
    pyqualicision_extension = Extension(
        "cython_code",
        ["poetry_cython_demo/cython_code.pyx", "poetry_cython_demo/compiled/source.c"],
    )
    # Build
    setup_kwargs.update(
        {
            "ext_modules": cythonize(
                pyqualicision_extension,
                language_level=3,
            ),
            "include_package_data": False,
        }
    )
