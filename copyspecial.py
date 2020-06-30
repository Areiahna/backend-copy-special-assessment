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
    # grabbing files in directory
    paths = os.listdir(dirname)
    # identify "special" files "__w__" (regex)
    special_paths = []
    for filename in paths:
        # regex pattern : 2 underscores + 1 or more word characters + 2 underscores
        match = re.search(r"__\w+__", filename)
        if match:
            # os.path.abspath() gets the absolute path
            # os.payj.join() joins directory & file path
            special_paths.append(os.path.abspath(
                os.path.join(dirname, filename)))

    return special_paths


def copy_to(path_list, dest_dir):
    # getlist of file paths
    file_paths = get_special_paths(path_list)
    # copyfile(src, destination)
    from shutil import copyfile
    # copy list of files into given directory
    return copyfile(file_paths, dest_dir)


def zip_to(path_list, dest_zip):
    # your code here
    return


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
    print(special_paths)
    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
