# cd target_dir/
# python %{path_to_file}/bq_loader.py dataset.table_name

import sys
import json
import os
import glob

files = glob.glob("*")
table = sys.argv[1]

for file_name in files:
    v = dict(file_name=file_name, table=table)
    command = "bq load --source_format=CSV %(table)s %(file_name)s" % v
    print(command)
    os.system(command)
