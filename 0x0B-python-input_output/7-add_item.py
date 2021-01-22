#!/usr/bin/python3

import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


lis = []
jfile = 'add_item.json'

if os.path.exists(jfile):
    lis = load_from_json_file(jfile)

for i in range(1, len(sys.argv)):
    lis.append(sys.argv[i])

save_to_json_file(lis, jfile)
