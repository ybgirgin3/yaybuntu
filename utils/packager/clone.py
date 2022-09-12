import os

def clone(url: str = "https://mpr.makedeb.org", pac: str = None, _p: str = None):
  "clone repo from mbr"
  download_url = f"{url}/{pac}.git"
  cmd = f"git clone '{download_url}' {_p}" # use git for downloader
  os.system(cmd)
  return _p
