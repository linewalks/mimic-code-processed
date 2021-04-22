from psycopg2 import sql


class BaseExtractor:
  def __init__(self, db, mimic_clinical):
    self.db = db
    self.conn = db.conn
    self.mimic_clinical = sql.Identifier(mimic_clinical)
