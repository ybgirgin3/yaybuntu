import os

from utils.logger import logger

def clone(url: str = "https://mpr.makedeb.org", pac: str = None, _p: str = None):
  "clone repo from mbr"
  if os.path.exists(_p):
      logger(f"Path already exists: {_p}", 'warning')
  download_url = f"{url}/{pac}.git"
  cmd = f"git clone '{download_url}' {_p}" # use git for downloader
  os.system(cmd)
  return _p
