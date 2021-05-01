from mimic_derived.subtasks.base_task import BaseTask
from common.query import load_sql
import os
import time


class BaseTable(BaseTask):
  preliminary_tables = [
    "icustay_times",
    "icustay_hours",
    "ventilation_classification",
    "ventilation_durations",
    "echo_data",
    "weight_durations",
    "norepinephrine_dose",
    "epinephrine_dose",
    "dopamine_dose",
    "dobutamine_dose",
    "vasopressor_durations"
  ]

  pivoted_tables = [
    "pivoted_bg",
    "pivoted_bg_art",
    "pivoted_lab",
    "pivoted_vital",
    "pivoted_fio2",
    "pivoted_gcs",
    "pivoted_uo",
    "pivoted_sofa"
  ]

  def __init__(self, conn, sql_path, mimic_clinical, mimic_derived):
    super().__init__(conn, sql_path, mimic_clinical, mimic_derived)

  def execute_query(self):
    print("\n====================Start Making All Tables====================\n")
    for tablename in self.preliminary_tables+self.pivoted_tables:
      start_time = time.time()
      print(f"Start making {tablename} table!")
      query = load_sql(os.path.join(self.sql_path, "base_table", f"{tablename}_table.sql"),
                       mimic_derived=self.mimic_derived)
      self.cursor.execute(query)
      print(f"Finished making {tablename} table!")
      end_time = time.time()
      print(f"{tablename} table Making time: {end_time-start_time:.2f}secs\n")
    print("====================Finished Making All Tables====================\n")
