import subprocess

def install(package_path: str = '/path/to/package'):
    pkgfile_path = os.path.join(package_path, 'PKGBUILD')
    command = f"makedeb {pkgfile_path}"
    # print("install here", package_path)
    subprocess.run(command.split())

