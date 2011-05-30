#
# core.py
#
# Copyright (C) 2011 Nikita Kovaliov <dev@maizy.ru>
#
# Basic plugin template created by:
# Copyright (C) 2008 Martijn Voncken <mvoncken@gmail.com>
# Copyright (C) 2007-2009 Andrew Resch <andrewresch@gmail.com>
# Copyright (C) 2009 Damien Churchill <damoxc@gmail.com>
# Copyright (C) 2010 Pedro Algarvio <pedro@algarvio.me>
#
# Deluge is free software.
#
# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# deluge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with deluge.    If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA  02110-1301, USA.
#
#    In addition, as a special exception, the copyright holders give
#    permission to link the code of portions of this program with the OpenSSL
#    library.
#    You must obey the GNU General Public License in all respects for all of
#    the code used other than OpenSSL. If you modify file(s) with this
#    exception, you may extend this exception to your version of the file(s),
#    but you are not obligated to do so. If you do not wish to do so, delete
#    this exception statement from your version. If you delete this exception
#    statement from all source files in the program, then also delete it here.
#

from deluge.plugins.pluginbase import CorePluginBase
import deluge.component as component
import deluge.configmanager
from deluge.core.rpcserver import export
import os

DEFAULT_PREFS = {
    'allowed_base_paths': '/', #divided by :
}

class Core(CorePluginBase):
    def enable(self):
        self.config = deluge.configmanager.ConfigManager("chooselocation.conf", DEFAULT_PREFS)

    def disable(self):
        pass

    def update(self):
        pass

    @export
    def set_config(self, config):
        """Sets the config dictionary"""
        for key in config.keys():
            self.config[key] = config[key]
        self.config.save()

    @export
    def get_config(self):
        """Returns the config dictionary"""
        return self.config.config

    @export
    def get_dirs(self, base_location=u"/"):
        base_location = unicode(base_location)

        result = []
        try:
            dirs = [ent for ent
                        in os.listdir(base_location)
                        if ent[0] != '.' and os.path.isdir(os.path.join(base_location, ent))]
            dirs.sort()
            for name in dirs:
                abs_path = os.path.join(base_location, name)
                try:
                    has_children = bool(os.listdir(abs_path))
                except OSError:
                    has_children = False

                result.append({
                    'path': abs_path,
                    'name': name,
                    'has_children': has_children,
                })
        except OSError:
            pass
        
        return result


if __name__ == '__main__':

    def dump(slf, pluginname):
        pass
    Core.__init__ = dump

    core = Core('chooselocation')

    print core.get_dirs()
    print core.get_dirs('/mnt/R2D2')