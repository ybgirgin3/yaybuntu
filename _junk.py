from utils.packager import depends
from utils.packager import download
import os


depeds_= depends.find_dep(path=f"{os.path.expanduser('~')}/.yaybuntu/btop")
ret = download.download(depeds_)
print(ret)
