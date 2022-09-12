from utils.logger import logger
from utils.extra import read
import tempfile
import os

from utils.packager import download


# read pkg file in the repo and extract makedepends


_tmp_file = tempfile.gettempdir()
_installed = 'installed.txt'
installed_pac = os.path.join(_tmp_file, _installed)


def find_dep(path: str = '/path/to/repo') -> list:
  "find dependecies of package"
  logger(f"path in find_dep: {path}")
  pkg = f"{path}/PKGBUILD"
  content = read.read(pkg)                                      # read package
  deps = [dep.strip() for dep in content if 'makedep' in dep]   # extract deps
  if len(deps): # if list is not empty
    for s in deps:
      deps = s[s.find("(")+1:s.find(")")]

  return deps

