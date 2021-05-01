DROP TABLE IF EXISTS {mimic_derived}.vasopressor_durations;

CREATE TABLE {mimic_derived}.vasopressor_durations (
  icustay_id integer,
  vasonum bigint,
  starttime timestamp without time zone,
  endtime timestamp without time zone,
  duration_hours double precision
);
