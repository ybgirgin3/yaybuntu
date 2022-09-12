from utils.config import paths
from utils.packager import depends, clone, download

import os

PATH = paths()

def packager(path: str = PATH,                    # source dir
             url: str = "https://mpr.makedeb.org",  # main url to clone
             package_name: list = None):            # package name
  

  source_p = path["source"]
  # _plist = [] # list of new dirs

  for pac in package_name:      # create package folders for each package name
    _p = f"{source_p}/{pac}"    # create dir query
    os.system(f"mkdir -p {_p}")
    cloned_path = clone.clone(url, pac, _p)  # start the clonning process
    deps, makedeps = depends.find_dep(cloned_path)  # find depends as str
    cmd_status = download.download(deps, makedeps)
    print("command status: ", cmd_status)


    
