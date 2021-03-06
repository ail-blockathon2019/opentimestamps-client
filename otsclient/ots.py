# Copyright (C) 2017 The OpenTimestamps developers
#
# This file is part of the OpenTimestamps Client.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of the OpenTimestamps Client, including this file, may be copied,
# modified, propagated, or distributed except according to the terms contained
# in the LICENSE file.

import sys
import logging

import otsclient.args

def main():
    args = otsclient.args.parse_ots_args(sys.argv[1:])

    logging.basicConfig(format='%(message)s')

    if args.verbosity == 0:
        logging.root.setLevel(logging.INFO)
    elif args.verbosity > 0:
        logging.root.setLevel(logging.DEBUG)
    elif args.verbosity == -1:
        logging.root.setLevel(logging.WARNING)
    elif args.verbosity < -1:
        logging.root.setLevel(logging.ERROR)

    if not hasattr(args, 'cmd_func'):
        args.parser.error('No command specified')

    args.cmd_func(args)

# vim:syntax=python filetype=python
