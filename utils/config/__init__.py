import yaml

def args() -> dict:
  "get default paths from yaml file"
  yaml_content = yaml.safe_load(open("utils/config/string_args.yaml"))

  return {
    # --- paths ---
    "source": yaml_content["source"],

    # --- commands ---
    "install": yaml_content["install"]
  }

  