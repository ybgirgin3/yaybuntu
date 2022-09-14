import os
import subprocess
from utils.logger import logger
from utils.extra import is_installed
from utils.config import args

ubnt_install = args()["install"]          # install command

def run_command(pkg: list = []):
    os.system(f"{ubnt_install} {pkg.split(' ')}")




# def run_as_sudo(sudo_user=os.getlogin(),
#                 cmd_str:list = [],
#                 shell=False,
#                 timeout=None):
# 
#     sudo_args = ["sudo", "-u", sudo_user]
# 
#     def run_cmd(cmd_array, shell=False, timeout=None):
#       if shell:
#         return subprocess.run(" ".join(cmd_array), shell=shell, timeout=timeout)
# 
#       # https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess
#       return subprocess.run(cmd_array, shell=shell, timeout=timeout)
# 
#     # run command
#     print("ret: ", sudo_args + cmd_str)
#     r = run_cmd(sudo_args + cmd_str.split(), shell=shell, timeout=timeout)
#     return r


def download(deps: list, mkdeps: list):
  "download deps"
  dep_installation_q = []
  make_dep_installation_q = []
  

  def _download_proc(deps, mkdeps):
    deps = deps if len(deps) else None        # define none if len is 0
    mkdeps = mkdeps if len(mkdeps) else None  # define none if len is 0


    # * install deps
    if deps is not None:
      run_as_sudo(cmd_str=deps)


    if mkdeps is not None:
      run_as_sudo(cmd_str=mkdeps)

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


