# definition
import os
app_installation_folder = '/usr/bin'

def is_installed(pkg_name) -> bool:
  return True if pkg_name in os.listdir(app_installation_folder) else False



