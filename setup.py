from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mill_touch_v6",
    version="0.0.1",
    author="John Doe",
    author_email="<doe.john@example.com>",
    description="mill_touch_v6 - A QtPyVCP based Virtual Control Panel for LinuxCNC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/USERNAME/REPO",
    download_url="https://github.com/USERNAME/REPO/tarball/master",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'mill_touch_v6=mill_touch_v6:main',
        ],
        'qtpyvcp.vcp': [
            'mill_touch_v6=mill_touch_v6',
        ],
    },
)
