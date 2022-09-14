import subprocess
from utils.logger import logger
from utils.extra import is_installed
from utils.config import args

ubnt_install = args()["install"]          # install command
arch_install = "yay -S"

def run_as_sudo(pkg: str):
    pkg_str = " ".join(pkg)
    command = f"{ubnt_install} {pkg_str}"
    logger(f"::> installation package(s) named: {pkg}", 'important')
    logger(command, 'info')
    subprocess.run(command.split())


def download(deps: list, mkdeps: list):
  "download deps"
  dep_installation_q = []
  make_dep_installation_q = []
  

  def _download_proc(deps, mkdeps):
    "carry packages to run as sudo command"
    deps = deps if len(deps) else None        # define none if len is 0
    mkdeps = mkdeps if len(mkdeps) else None  # define none if len is 0


    # * install deps
    if deps is not None:
      run_as_sudo(pkg=deps)


    if mkdeps is not None:
      run_as_sudo(pkg=mkdeps)

  for dep in deps:
    isExists = is_installed.is_installed(dep)  # control if pkg is installed
    if not isExists and dep not in dep_installation_q:
      dep_installation_q.append(dep)
    else: print(f"::> package named {dep} is already installed")

  for mk in mkdeps:
    isExists = is_installed.is_installed(mk)  # control if pkg is installed
    if not isExists and mk not in dep_installation_q:
      make_dep_installation_q.append(mk)
    else: print(f"::> package named {mk} is already installed")

      
  _download_proc(dep_installation_q, make_dep_installation_q)

  #return dep_installation_q, make_dep_installation_q


