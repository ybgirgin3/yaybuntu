import subprocess
import os

def install(package_path: str = '/path/to/package'):
    # pkgfile_path = os.path.join(package_path, 'PKGBUILD')

    command = f"makedeb -i PKGBUILD"
    # print("install here", package_path)

    os.chdir(f'{package_path}')
    subprocess.run(command.split())

