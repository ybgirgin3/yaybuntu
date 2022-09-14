import subprocess
import os

def install(package_path: str = '/path/to/package'):
    pkgfile_path = os.path.join(package_path, 'PKGBUILD')
    print("pkgfile path: ", pkgfile_path)
    command = f"makedeb -i {pkgfile_path}"
    # print("install here", package_path)
    subprocess.run(command.split())

