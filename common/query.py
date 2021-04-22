from psycopg2 import sql


def load_sql(sql_path, **kwargs):
  with open(sql_path, "r") as fd:
    query = sql.SQL(fd.read())
    if len(kwargs) > 0:
      query = query.format(**kwargs)
    return query
