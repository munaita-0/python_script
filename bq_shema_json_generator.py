# python3 bq_shema_json_generator.py column1,column2,column3,column4,column5,column6
# generate string nullable schema json

import sys
import json

args = sys.argv

array = []
for column in args[1].split(','):
    mapping = {}
    mapping['name'] = column.strip()
    mapping['type'] = 'STRING'
    array.append(mapping)

print(json.dumps(array))
