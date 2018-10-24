import os.path

from setuptools import setup

install_requires=["cffi>=1.0.0", "six"]

dirname = os.path.dirname(os.path.abspath(__file__))

setup(
    name="memcached-cffi",
    # use_scm_version=True,
    version="0.0.1",
    description="A CFFI binding for libmemcached",
    author="Wenxiang Wu",
    author_email="thewrongboy@gmail.com",
    url="https://github.com/wenxiang/memcached-cffi",
    license="MIT",
    package_dir={"": "src"},
    packages=["memcached_cffi"],
    setup_requires=["setuptools_scm", "cffi>=1.0.0"],
    install_requires=install_requires,
    cffi_modules=["src/build_ffi.py:ffi"],
)
