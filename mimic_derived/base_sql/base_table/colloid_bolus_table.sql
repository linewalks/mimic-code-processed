DROP TABLE IF EXISTS {mimic_derived}.colloid_bolus;

CREATE TABLE {mimic_derived}.colloid_bolus (
  icustay_id integer,
  charttime timestamp without time zone,
  colloid_bolus double precision
);
