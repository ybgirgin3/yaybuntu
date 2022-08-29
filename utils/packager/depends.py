from utils.extra import read
import subprocess
import tempfile
import os

# read pkg file in the repo and extract makedepends


_tmp_file = tempfile.gettempdir()
_installed = 'installed.txt'
installed_pac = os.path.join(_tmp_file, _installed)


def find_dep(path: str = '/path/to/repo'):
  pkg = f"{path}/PKGBUILD"
  content = read.read(pkg)                                      # read package
  deps = [dep.strip() for dep in content if 'makedep' in dep]   # extract deps
  if len(deps): # if list is not empty
    for dep in deps:
      os.system(f"apt list --installed | grep {dep} > {installed_pac}")
      #subprocess.run(["apt", "list", "--installed", "grep", dep, ">", installed_pac])

    
    #for dep in deps:
      #process = subprocess.Popen(['apt', 'list', '--installed', '|', 'grep', f'{dep}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      #out, err = process.communicate()
      #print(out.decode('utf-8').split())


#find_dep("/home/berkay/.yaybuntu/btop")