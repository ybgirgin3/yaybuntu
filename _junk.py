from utils.packager import depends
from utils.packager import download

ret = download.isInstalled('btop')

# ret = depends.find_dep(path=f"/home/berkay/.yaybuntu/btop")
print(ret)
