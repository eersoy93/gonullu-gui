#
#  Gonullu GUI setup script
#
#  Copyright 2017 Erdem Ersoy (erdemersoy@live.com)
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

# Imports modules
from setuptools import setup
from os import listdir, system
from distro import linux_distribution
from gonullugui.version import __version__


# Adds .qm files to langs list. In Pisi GNU/Linux, lrelease-qt5 is exist
# instead of lrelease.
langs = []
for file in listdir('langs'):
    if file.endswith('ts'):
        if (linux_distribution()[0] == "PisiLinux"):
            system('lrelease-qt5 langs/{}'.format(file))
        else:
            system('lrelease langs/{}'.format(file))
        langs.append(('langs/{}'.format(file)).replace('.ts', '.qm'))

# Adds data files which be specified by setputools setup function's data_files
# attribute.
datas = [
        ('/usr/share/applications/', ['data/gonullu-gui.desktop']),
        ('/usr/share/polkit-1/actions/',
            ['data/org.freedesktop.policykit.gonullu-gui.policy']),
        ('/usr/share/polkit-1/actions/',
            ['data/org.freedesktop.policykit.gonullu-gui-local.policy'])
    ]

if (linux_distribution()[0] == "PisiLinux"):
    datas.append(('/usr/share/gonullu-gui/langs/', langs))
else:
    datas.append(('/usr/local/share/gonullu-gui/langs/', langs))

# Converts python code but this operation not yet implemented.
# system('pyrcc5 gonullu-gui.qrc -o gonullugui/resource.py')

# setuptools setup function
setup(
    name="GonulluGUI",
    version=__version__,
    packages=["gonullugui"],
    scripts=["bin/gonullu-gui", "bin/gonullu-gui-main"],
    # install_requires=[               # If possible, you should installing
    #     "distro", "gonullu", "PyQt5" # requirements via your distrobution's
    #     ],                           # package repositories.
    data_files=datas,
    author="Erdem Ersoy",
    author_email="erdemersoy@live.com",
    description="Graphical user interface for Gonullu.",
    license="GPLv3",
    keywords=["PyQt5", "gonullu"],
    url="https://github.com/eersoy93/gonullu-gui"
)
