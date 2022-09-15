from utils.packager import download
from utils.extra import read
import os

_home = os.path.expanduser('~')
_dir = os.path.join(_home, '.yaybuntu')




#pkg = ["btop", "htop"]
_file = f"{_dir}/lazygit/.SRCINFO"
#ret = download.run_as_sudo(pkg=pkg)
ret = read.read(_file)
