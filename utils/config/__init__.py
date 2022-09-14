import yaml
import os

def args() -> dict:
  "get default paths from yaml file"
  yaml_content = yaml.safe_load(open("utils/config/string_args.yaml"))

  _home = os.path.expanduser('~')
  _dir = os.path.join(_home, '.yaybuntu')

  return {
    # --- paths ---
    #"source": yaml_content["source"],
    "source": f'{_dir}',

    # --- commands ---
    "install": yaml_content["install"]
  }

  
