import os
from utils.logger import logger
from utils.extra import is_installed
from utils.config import args



  

def download(deps: list, mkdeps: list):
  "download deps"
  dep_installation_q = []
  make_dep_installation_q = []

  
  

  def _download_proc(deps, mkdeps):
    deps = deps if len(deps) else None        # define none if len is 0
    mkdeps = mkdeps if len(mkdeps) else None  # define none if len is 0
    ubnt_install = args()["install"]          # install command

    # * install deps
    if deps is not None:
      for dep in deps:
        cur_cmd = f"{ubnt_install} {dep}"     # enter command and what for finish
        os.system(cur_cmd)


    if mkdeps is not None:
      for mk in mkdeps:
        cur_cmd = f"{ubnt_install} {mk}"      # enter command and what for finish
        os.system(cur_cmd)




  for dep in deps:
    isExists = is_installed.is_installed(dep)  # control if pkg is installed
    if not isExists and dep not in dep_installation_q:
      dep_installation_q.append(dep)

  for mk in mkdeps:
    isExists = is_installed.is_installed(mk)  # control if pkg is installed
    if not isExists and mk not in dep_installation_q:
      make_dep_installation_q.append(mk)

      
  _download_proc(dep_installation_q, make_dep_installation_q)


        
    #return dep_installation_q, make_dep_installation_q


