from utils.config import paths
from utils.packager.clone import clone
import subprocess
import os

PATH = paths()

def packager(path: str = PATH,                    # source dir
             url: str = "https://mpr.makedeb.org",  # main url to clone
             package_name: list = None):            # package name
  

  source_p = path["source"]
  _plist = [] # list of new dirs

  for pac in package_name:      # create package folders for each package name
    _p = f"{source_p}/{pac}"    # create dir query
    os.system(f"mkdir -p {_p}")
    clone(url, pac, _p)         # start the clonning process
    