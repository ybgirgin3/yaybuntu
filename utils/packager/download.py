import subprocess

from utils.logger import logger

ubuntu_download_command = "sudo apt install"

def isInstalled(pkg: str):
  all_installed_packages = subprocess.check_output("apt", "list" , "--installed")
  print(all_installed_packages)


def download(deps: list):
  "download deps"
  p_codes = []
  for dep in deps:
    cmd = f"{ubuntu_download_command} {dep}"
    logger(f"Running command: {cmd}")
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    process.wait
    p_codes.append(process.returncode)

  return p_codes



