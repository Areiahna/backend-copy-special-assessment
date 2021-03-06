#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Areiahna Cooks, Study Hall w/Daniel & friends"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""

    paths = os.listdir(dirname)
    special_paths = []
    for filename in paths:
        match = re.search(r"__\w+__", filename)
        if match:
            special_paths.append(os.path.abspath(
                os.path.join(dirname, filename)))

    return special_paths


def copy_to(path_list, dest_dir):
    for filename in path_list:
        if not dest_dir:
            os.mkdir(dest_dir)
            shutil.copy(filename, dest_dir)


def zip_to(path_list, dest_zip):
    cmd = ["zip", '-j', dest_zip]
    cmd.extend(path_list)
    print("Command I'm going to do:")
    print(' '.join(cmd))
    output = subprocess.check_output(cmd)
    return output


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).
    special_paths = get_special_paths(ns.from_dir)
    if ns.todir:
        copy_to(special_paths, ns.todir)
    if ns.tozip:
        zip_to(special_paths, ns.tozip)
    else:
        print('\n'.join(special_paths))


if __name__ == "__main__":
    main(sys.argv[1:])
