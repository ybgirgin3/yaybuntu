import yaml

def paths() -> dict:
  "get default paths from yaml file"
  yaml_content = yaml.safe_load(open("utils/config/paths.yaml"))

  return {
    "source": yaml_content["source"]
  }
  