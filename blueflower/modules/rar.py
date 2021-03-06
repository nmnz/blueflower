# rar.py
#
# This file is part of blueflower.
# 
# blueflower is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# blueflower is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with blueflower.  If not, see <http://www.gnu.org/licenses/>.
#
#
# Copyright 2014 JP Aumasson <jeanphilippe.aumasson@gmail.com>


import os
import re
import rarfile

from blueflower.do import do_data
from blueflower.settings import INFILENAME
from blueflower.types import types_data
from blueflower.utils import log_error, log_secret


def rar_do_rar(arar, afile):
    """ arar:RarFile, afile:source archive(s) name """
    infilename = re.compile('|'.join(INFILENAME))

    # iterate over infolist to detect directories
    # (unlike zipfile, doesnt append '/' to dir names
    for member in arar.infolist():
        # sort directories out
        if member.isdir():
            continue
        # check file name
        filename =  os.path.basename(member.filename).lower()
        res = infilename.search(filename)
        if res:
            log_secret(res.group(), afile+':'+member.filename)

        # check file content, calling other modules
        data = arar.read(member)
        (ftype, keep) = types_data(data)
        if keep:
            do_data(ftype, data, afile+':'+member.filename)


def rar_do_file(afile):
    # fixes problems with default '\' separator
    rarfile.PATH_SEP = '/'
    try:
        arar = rarfile.RarFile(afile)
    except rarfile.BadRarFile:
        log_error('rarfile.BadRarFile', afile)
        return
    rar_do_rar(arar, afile)
    arar.close()

