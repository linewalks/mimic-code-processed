from mimic_derived.subtasks.base_task import BaseTask
from common.query import load_sql
import os
import time


class InitSchema(BaseTask):
  def __init__(self, conn, sql_path, mimic_clinical, mimic_derived):
    super().__init__(conn, sql_path, mimic_clinical, mimic_derived)

  def execute_query(self):
    print(f"\n====================Start Making {self.mimic_derived} Schema====================\n")
    start_time = time.time()
    query = load_sql(os.path.join(self.sql_path, "init_schema.sql"),
                     mimic_derived=self.mimic_derived)
    self.cursor.execute(query)
    end_time = time.time()
    print(f"{self.mimic_derived} schema Making time: {end_time-start_time:.2f}secs\n")
    print(f"\n====================Finished Making {self.mimic_derived} Schema====================\n")
