# Gonullu Graphical User Interface (Gonullu GUI)
Gonullu Graphical User Interface (Gonullu GUI) is GUI for Pisi GNU/Linux's Gonullu application. Gonullu GUI has been written with Python 3.x and PyQt 5.x. For information about Gonullu, see Gonullu's GitHub repository ([https://github.com/PisiLinuxNew/gonullu](https://github.com/PisiLinuxNew/gonullu)).

**NOTE:** Gonullu is Turkish only but Gonullu GUI is multilingual.

# Versioning
Stable version numbers consist a major release and a minor release number. The major release number starts from 1, the minor release number starts from 0. Version numbers contain "dev" string (e.g. 1.0.dev0, 2.0.dev3) indicate development version of major release, and 1.0.dev0 version number indicates entire non-functional phase. After development versions, preview versions come. Version numbers contain "rc" string (e.g. 1.0rc2) indicate preview versions. Also, after "dev" and "rc" strings, very minor version numbers come. Very minor version number starts from 1 except 1.0dev versions.

**NOTE:** Very old non-functional phase versions may be different beacuse versioning has been changed already.

# Installation and running
After downloading or cloning this repository, open a terminal in directory that this repository has been downloaded or cloned into and run as root that command for installation:

    python3 setup.py install

After installation, you can run that command in any directory for running:

    gonullu-gui

Also, you can run Gonullu GUI via your desktop menu.

**NOTE:** Gonullu GUI requires Gonullu, PyQt5 and [distro](https://pypi.python.org/pypi/distro) but if possible, you should installing requirements via your distrobution's package repositories.

# Translating
Translation files are langs/*.ts files in source code. Also, Gonullu GUI's desktop file in source code (data/gonullu-gui.desktop file) should be translated in accordance with freedesktop.org's [Desktop Entry Specification](https://freedesktop.org/wiki/Specifications/desktop-entry-spec/) and Gonullu GUI's polkit configuration files in source code (data/org.freedesktop.policykit.gonullu-gui.policy and data/org.freedesktop.policykit.gonullu-gui-local.policy files) should be translated in accordance with freedesktop.org's [polkit](https://www.freedesktop.org/wiki/Software/polkit/).

# License
Gonullu GUI is licensed by GPLv3 (see LICENSE for GPLv3), but because of bin/gonullu-gui script in source code has been taken from multibootusb project, this file is licensed by GPLv2 (see LICENSE_2 for GPLv2)
