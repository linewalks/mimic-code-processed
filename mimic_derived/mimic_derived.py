from common.base_extractor import BaseExtractor
from mimic_derived.subtasks.init_schema import InitSchema
from mimic_derived.subtasks.base_table import BaseTable
from mimic_derived.subtasks.extract_preliminary_features import ExtractPreliminaryFeatures
from mimic_derived.subtasks.extract_pivoted_features import ExtractPivotedFeatures
import time


class MimicDerivedExtractor(BaseExtractor):
  def __init__(self, db, mimic_clinical, mimic_derived):
    super().__init__(db, mimic_clinical)
    self.sql_path = "./mimic_derived/base_sql"
    self.mimic_derived = mimic_derived

  def extract(self):
    start_time = time.time()

    common_params = [self.conn, self.sql_path, self.mimic_clinical, self.mimic_derived]

    InitSchema(*common_params).execute_query()
    BaseTable(*common_params).execute_query()

    ExtractPreliminaryFeatures(*common_params).execute_query()
    ExtractPivotedFeatures(*common_params).execute_query()

    end_time = time.time()

    print(f"Total time: {end_time-start_time:.2f}secs")
