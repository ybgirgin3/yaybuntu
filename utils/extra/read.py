from utils.logger import logger
from collections import Counter


def read(fp: str = '/path/to/file'):
  "read and extract information as a json"
  print("current file path:", fp)
  content = open(f'{fp}', 'r').readlines()
  content = [i.strip() for i in content]

  logger("make file parsing.. \npackage information details..\n")

  deps = dict()

  for line in content:
    k, v = line.split("=")
    k,v = k.strip(), v.strip()
    if k in deps:
      if not isinstance(deps[k], list):
        deps[k] = []
      deps[k].append(v)
    else:
      deps[k] = v

  return deps 
