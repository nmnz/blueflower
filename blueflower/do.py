# do.py
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


def do_data(ftype, data, afile):
    if ftype == 'other':
        return
    elif ftype == 'bzip2': 
        from blueflower.modules.bzip2 import bzip2_do_data
        bzip2_do_data(data, afile)
    elif ftype == 'gz': 
        from blueflower.modules.gz import gz_do_data
        gz_do_data(data, afile)
    elif ftype == 'pdf': 
        from blueflower.modules.pdf import pdf_do_data
        pdf_do_data(data, afile)
    elif ftype == 'tar': 
        from blueflower.modules.tar import tar_do_data
        tar_do_data(data, afile)
    elif ftype == 'text': 
        from blueflower.modules.text import text_do_data
        text_do_data(data, afile)
    elif ftype == 'zip': 
        from blueflower.modules.zip import zip_do_data
        zip_do_data(data, afile)


def do_file(ftype, afile):
    if ftype == 'other':
        return
    elif ftype == 'bzip2': 
        from blueflower.modules.bzip2 import bzip2_do_file
        bzip2_do_file(afile)
    elif ftype == 'gz': 
        from blueflower.modules.gz import gz_do_file
        gz_do_file(afile)
    elif ftype == 'rar': 
        from blueflower.modules.rar import rar_do_file
        rar_do_file(afile)
    elif ftype == 'pdf': 
        from blueflower.modules.pdf import pdf_do_file
        pdf_do_file(afile)
    elif ftype == 'tar': 
        from blueflower.modules.tar import tar_do_file
        tar_do_file(afile)
    elif ftype == 'text': 
        from blueflower.modules.text import text_do_file
        text_do_file(afile)
    elif ftype == 'zip': 
        from blueflower.modules.zip import zip_do_file
        zip_do_file(afile)

