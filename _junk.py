from utils.packager import depends
from utils.packager import download
import os


deps, makedeps = depends.find_dep(path=f"{os.path.expanduser('~')}/.yaybuntu/btop")
ret = download.download(deps, makedeps)
print(ret)
