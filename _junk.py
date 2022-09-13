from utils.packager import depends
from utils.packager import download
from utils.extra import is_installed
import os


deps, makedeps = depends.find_dep(path=f"{os.path.expanduser('~')}/.yaybuntu/btop")
download.download(deps, makedeps)
#ret = is_installed.is_installed('btop')
