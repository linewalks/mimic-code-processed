DROP TABLE IF EXISTS {mimic_derived}.urine_output;

CREATE TABLE {mimic_derived}.urine_output (
	icustay_id integer,
	charttime timestamp without time zone,
	value double precision
);
