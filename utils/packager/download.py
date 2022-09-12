import os
import subprocess

from utils.logger import logger

ubuntu_download_command = "sudo apt install"

def isInstalled(pkg: str, installation_folder: str = '/usr/bin') -> list:
  q = []
  for installed_apps in os.listdir(installation_folder):
    if pkg in installed_apps:
      logger(f"{pkg} package already installed.. passing..")
    else:
      q.append(pkg)

  if len(q):
    for i in q:
      logger(f"{i} added to installation queue..", 'warning')
  else: logger("no package is in installation queue")
  return q
  


def download(deps: list, makedeps: list) -> list or bool:
  "download deps"

  def _process(pkg):
    p_codes = []
    if len(isInstalled(pkg)) > 0:
      cmd = f"{ubuntu_download_command} {pkg}"
      logger(f"Running command: {cmd}")
      process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
      process.wait
      p_codes.append(process.returncode)
      return p_codes

    else:
      logger("no package found to installation queue")
      return True



  for dep in deps:  # look for deps
    _process(dep)
  for mkdep in makedeps:  # look for makedeps
    _process(mkdep)



