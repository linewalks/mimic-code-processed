from mimic_derived.subtasks.base_task import BaseTask
from mimic_derived.subtasks.base_table import BaseTable
from common.query import load_sql
import os
import time


class ExtractPreliminaryFeatures(BaseTask):
  def __init__(self, conn, sql_path, mimic_clinical, mimic_derived):
    super().__init__(conn, sql_path, mimic_clinical, mimic_derived)
    self.tables_to_extract = BaseTable.preliminary_tables

  def execute_query(self):
    print("\n====================Start Extracting Preliminary Features====================\n")

    for table in self.tables_to_extract:
      print(f"\n====================Start Extracting {table}====================\n")
      start_time = time.time()
      query = load_sql(os.path.join(self.sql_path, "extract_data", f"make_{table}.sql"),
                       mimic_clinical=self.mimic_clinical,
                       mimic_derived=self.mimic_derived)
      self.cursor.execute(query)
      end_time = time.time()
      print(f"Extracting time: {end_time-start_time:.2f}secs\n")
      print(f"\n====================Finished Extracting {table}====================\n")

    print("====================Finished Extracting Preliminary Features====================\n")
