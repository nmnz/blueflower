# utils.py
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


import logging
import time


def log(message):
    logging.info(message)


def log_comment(comment):
    log('# %s: %s' % (timestamp(), comment))


def log_encrypted(ftype, filename=''):
    log('ENCRYPTED, %s, %s' % (ftype, filename))


def log_error(error, filename=''):
    log('ERROR, %s, %s' % (error, filename))


def log_secret(secret, filename=''):
    log('SECRET, %s, %s' % (secret, filename))



def log_selected(ftype, filename):
    log('SELECTED, %s, %s' % (ftype, filename))


def timestamp():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())
