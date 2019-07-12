=====================
Installing Mill Touch
=====================

Mill Touch uses `QtPyVCP <https://qtpyvcp.kcjengr.com/>`_ so that must be
installed first.

To install you may need some dependencies installed.


Requires python-pyqt5.qtsql to be installed for the database to work
::

  sudo apt install python-pyqt5.qtsql python-pyqt5.qsci

To clone and install Mill Touch
::

  git clone https://github.com/jethornton/mill_touch_v6.git
  cd mill_touch_v6
  pip install -e .

To create the directories that LinuxCNC uses run the Axis simulator.

to test copy the config to linuxcnc/configs

to use with your config in the ini file set

    DISPLAY = qtpyvcp
    VCP = mill_touch_v6

