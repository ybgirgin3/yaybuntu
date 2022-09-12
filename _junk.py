from utils.packager import depends
from utils.packager import download


depeds_= depends.find_dep(path=f"/home/berkay/.yaybuntu/btop")
ret = download.download(depeds_)
print(ret)
