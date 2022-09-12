from utils.logger import logger


def read(fp: str = '/path/to/file'):
  logger(f"path in read: {fp}")
  return open(fp, 'r').readlines()
