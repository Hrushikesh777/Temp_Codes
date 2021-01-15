import os
import sys
import subprocess

def run_cmd(cmd):
    op = subprocess.run(cmd, stderr=subprocess.PIPE, universal_newlines=True)
    if op.stderr:
        sys.exit(op.stderr)


def create_folder(folder_name):
    if os.path.exists(folder_name):
        os.removedirs(folder_name)
    os.mkdir(folder_name)


def compress(folder_name):
    create_folder(folder_name)
    run_cmd('tar -zcvf Stuff.tar.gz ' + folder_name + '/')


def decompress(folder_name):
    create_folder(folder_name)
    run_cmd('tar -zxvf ' + folder_name + '.tar.gz')
