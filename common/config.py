import configparser


def read_config(inidir):
  cfg = configparser.ConfigParser()
  cfg.read(inidir)
  return cfg
