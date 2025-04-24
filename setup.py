import re
import sys
from setuptools import setup, find_packages
from pathlib import Path

if sys.version_info < (3, 10):
    sys.exit('Sorry, Python < 3.10 is not supported.')

with open("README.md", "r") as fh:
    long_description = fh.read()

def get_version():
    init_path = Path(__file__).parent / "unavlib" / "__init__.py"
    with init_path.open("r") as f:
        content = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name="unavlib",
    packages=[package for package in find_packages()],
    version=get_version(),
    license="GPL",
    description="MultiWii Serial Protocol autonomous flight SDK for INAV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Frogmane",
    author_email="",
    url="https://github.com/xznhj8129/uNAVlib",
    download_url="",
    keywords=['Betaflight', 'iNAV', 'drone', 'UAV', 'Multi Wii Serial Protocol', 'MSP'],
    install_requires=['packaging', 'pyserial','asyncio','simple-pid','geographiclib','mgrs','geojson'],
    classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Information Technology',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Framework :: Robot Framework :: Library',
          'Topic :: Education',
          'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ]
)
