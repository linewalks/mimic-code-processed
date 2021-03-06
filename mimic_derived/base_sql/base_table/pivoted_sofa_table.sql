DROP TABLE IF EXISTS {mimic_derived}.pivoted_sofa;

CREATE TABLE {mimic_derived}.pivoted_sofa (
  icustay_id integer,
  hr integer,
  starttime timestamp without time zone,
  endtime timestamp without time zone,
  pao2fio2ratio_novent double precision,
  pao2fio2ratio_vent double precision,
  rate_epinephrine double precision,
  rate_norepinephrine double precision,
  rate_dopamine double precision,
  rate_dobutamine double precision,
  meanbp_min double precision,
  gcs_min double precision,
  urineoutput double precision,
  bilirubin_max double precision,
  creatinine_max double precision,
  platelet_min double precision,
  respiration smallint,
  coagulation smallint,
  liver smallint,
  cardiovascular smallint,
  cns smallint,
  renal smallint,
  respiration_24hours smallint,
  coagulation_24hours smallint,
  liver_24hours smallint,
  cardiovascular_24hours smallint,
  cns_24hours smallint,
  renal_24hours smallint,
  sofa_24hours integer
);
