# docx.py
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


import io
import zipfile

from xml.etree.cElementTree import XML
from xml.etree.ElementTree import XML

from blueflower.modules.text import text_do_data
from blueflower.utils import log_error


# thanks to http://etienned.github.io/posts/extract-text-from-word-docx-simply/

def docx_do_docx(azip, afile):
    word_namespace = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    par = word_namespace + 'p'
    txt = word_namespace + 't'
 
    xml_content = azip.read('word/document.xml')
    tree = XML(xml_content)
 
    paragraphs = []
    for paragraph in tree.getiterator(par):
        texts = [node.text
                 for node in paragraph.getiterator(txt)
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))
 
    text = '\n\n'.join(paragraphs)
    text_do_data(text, afile)


def docx_do_data(data, afile):
    filelike = io.BytesIO(data)
    try:
        azip = zipfile.ZipFile(filelike)
    except zipfile.BadZipfile:
        log_error('zipfile.BadZipFile', afile)
        return
    docx_do_docx(azip, afile)
    azip.close()


def docx_do_file(afile):
    try:
        azip = zipfile.ZipFile(afile)
    except zipfile.BadZipfile:
        log_error('zipfile.BadZipFile', afile)
        return
    docx_do_docx(azip, afile)
    azip.close()
