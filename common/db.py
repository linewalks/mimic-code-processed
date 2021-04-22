from common.config import read_config
import psycopg2
import os


class ExtractorDB:
  def __init__(self, inidir=None):
    if inidir:
      cfg = read_config(inidir)
    else:
      cfg = read_config(f"{os.getcwd()}/mimicdb.ini")

    host = cfg["mimicdb"]["PSQL_HOST"]
    password = cfg["mimicdb"]["PSQL_PASSWORD"]
    dbname = cfg["mimicdb"]["PSQL_DBNAME"]
    user = cfg["mimicdb"]["PSQL_USER"]

    self.connect_to_db(host, password, dbname, user)

  def connect_to_db(self, host, password, dbname, user):
    try:
      self.conn = psycopg2.connect(host=host,
                                   user=user,
                                   dbname=dbname,
                                   password=password)
      self.conn.autocommit = True
      print("Success connect to db!")
    except Exception as e:
      print(e)
      print("*******Failed connect to db!*******")
      exit()

  def close(self):
    if self.conn:
      self.conn.close()
