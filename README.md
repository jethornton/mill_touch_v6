# mill_touch_v6
QtPyVCP Mill Touch Screen

Requires python-pyqt5.qtsql
    sudo apt install python-pyqt5.qtsql

to clone and install
    git clone https://github.com/jethornton/mill_touch_v6.git
    cd mill_touch_v6
    pip install -e .

to test copy the config to linuxcnc/configs

to use with your config in the ini file set
    DISPLAY = qtpyvcp
    VCP = mill_touch_v6
