class BaseTask:
  def __init__(self, conn, sql_path, mimic_clinical, mimic_derived):
    self.conn = conn
    self.cursor = conn.cursor()
    self.sql_path = sql_path
    self.mimic_clinical = mimic_clinical
    self.mimic_derived = mimic_derived
