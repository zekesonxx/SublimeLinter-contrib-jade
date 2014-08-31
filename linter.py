#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Zeke
# Copyright (c) 2014 Zeke Sonxx
#
# License: MIT
#

"""This module exports the Jade plugin class."""

from SublimeLinter.lint import Linter, util


class Jade(Linter):

    """Provides an interface to the jade linter."""

    syntax = 'jade'
    cmd = 'jade'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.5'
    regex = (
        r'Error: .+\:(?P<line>[0-9]+)\r?\n'
        r'(?:\s+(?:\>\s*)?[0-9]+\|.+\r?\n)*\r?\n'
        r'(?P<message>.+)'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_STDERR
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'