# mimic-code-processed

How To Execute:

1. Install requirements (in virtualenv if possible) using
```
pip install -r requirements.txt
```
2. Make a copy of default.ini and rename as mimicdb.ini
3. Edit MIMIC3 Database access information in mimicdb.ini
4. Execute below command:
```
python run_extractor.py {source_schema} {dest_schema}
```

Original SQL Files from Dr. Alistair Johnson
https://github.com/MIT-LCP/mimic-code

Converted from Google BigQuery to PostgreSQL
by Woosung Jung
william.jung@yale.edu
