#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000  Donald N. Allingham
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

"Disconnected individuals"

import Filter
import RelLib
import intl
_ = intl.gettext

class Disconnected(Filter.Filter):
    "Disconnected individuals"

    def match(self,person):
        return person.getMainFamily() == None and len(person.getFamilyList()) == 0

def create(text):
    return Disconnected(text)

def need_qualifier():
    return 0

def get_name():
    return _("Disconnected individuals")
