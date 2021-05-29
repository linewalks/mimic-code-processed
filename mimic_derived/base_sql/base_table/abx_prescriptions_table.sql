DROP TABLE IF EXISTS {mimic_derived}.abx_prescriptions;

CREATE TABLE {mimic_derived}.abx_prescriptions (
	subject_id integer,
	hadm_id integer,
	icustay_id integer,
	antibiotic text,
	route text,
	startdate timestamp without time zone,
	enddate timestamp without time zone
);
