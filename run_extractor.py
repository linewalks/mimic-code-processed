import sys
import os
sys.path.append(os.getcwd())

from common.db import ExtractorDB
from mimic_derived.mimic_derived import MimicDerivedExtractor
import argparse


def start(mimic_clinical, mimic_derived):
  print("MIMIC Derived Extract Start")
  db = ExtractorDB()
  extractor = MimicDerivedExtractor(db, mimic_clinical, mimic_derived)
  extractor.extract()
  db.close()


if __name__ == "__main__":
  argparser = argparse.ArgumentParser(description=__doc__)
  argparser.add_argument(
      dest="mimic_clinical",
      type=str,
      nargs=1,
      help="source schema name")
  argparser.add_argument(
      dest="mimic_derived",
      type=str,
      nargs=1,
      help="destination schema name")

  args = argparser.parse_args()

  start(args.mimic_clinical[0], args.mimic_derived[0])
