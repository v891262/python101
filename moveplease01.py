#!/usr/bin/env python3

import shutil
import os

os.chdir("/home/student1/python101/")
xname = input("What is the new name for kerrigan.obj?")
shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)
