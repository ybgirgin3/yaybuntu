import subprocess

from utils.logger import logger

ubuntu_download_command = "sudo apt install"

def download(deps: str):
    cmd = f"{ubuntu_download_command} {deps}"
    logger(f"Running command: {cmd}")
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    process.wait
    return process.returncode

