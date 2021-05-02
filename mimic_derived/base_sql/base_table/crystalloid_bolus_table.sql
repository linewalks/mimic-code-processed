DROP TABLE IF EXISTS {mimic_derived}.crystalloid_bolus;

CREATE TABLE {mimic_derived}.crystalloid_bolus (
  icustay_id integer,
  charttime timestamp without time zone,
  crystalloid_bolus double precision
);
