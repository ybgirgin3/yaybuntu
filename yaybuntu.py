from utils.packager import packager
import os
import argparse


def parse_opt():
  # parser options
  parser = argparse.ArgumentParser()
  parser.add_argument('-S', nargs='+', type=str, help='install package')

  # make parses ready to use
  opt = parser.parse_args()
  print(vars(opt))
  return opt

  
def main(opt):
  app_list = opt.S                # list of programmes
  packager(package_name=app_list) # start download process
  

if __name__ == '__main__':
  opt = parse_opt()
  main(opt)