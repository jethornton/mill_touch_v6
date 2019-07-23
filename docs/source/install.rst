=====================
Installing Mill Touch
=====================

Mill Touch uses `QtPyVCP <https://qtpyvcp.kcjengr.com/>`_ so that must be
installed first.

To install you may need some dependencies installed.


Requires python-pyqt5.qtsql and python-pyqt5.qsci to be installed for the
database to work
::

  sudo apt install python-pyqt5.qtsql python-pyqt5.qsci

To clone and install Mill Touch
::

  git clone https://github.com/jethornton/mill_touch_v6.git
  cd mill_touch_v6
  pip install -e .

Copy the .xsessionrc file to your home directory and either log out and back in
or reboot. (you may need to set show hidden files to see it in the file browser)

To create the directories that LinuxCNC uses run the Axis simulator once.

To test copy the mill_touch_v6 directory from the config directory to
linuxcnc/configs

To use with your config in the ini file set

    DISPLAY = qtpyvcp
    VCP = mill_touch_v6

`QtPyVCP INI options <https://qtpyvcp.kcjengr.com/configuration/ini_options.html>`_
