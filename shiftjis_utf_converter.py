# cd target_dir/
# python shiftjis_utf_converter.py
# convert everyfile from shift-jis into utf-8

import json
import os
import glob

files = glob.glob("*")

for file_name in files:
    v = dict(file_name=file_name)
    command = "nkf -w %(file_name)s  > utf_%(file_name)s" % v
    print(command)
    os.system(command)
