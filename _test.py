from utils.packager import download

pkg = ["btop", "htop"]
ret = download.run_as_sudo(pkg)
