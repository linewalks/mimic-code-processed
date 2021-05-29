DROP TABLE IF EXISTS {mimic_derived}.kdigo_uo;

CREATE TABLE {mimic_derived}.kdigo_uo (
	icustay_id integer,
	charttime timestamp without time zone,
	weight double precision,
	urineoutput_6hr double precision,
	urineoutput_12hr double precision,
	urineoutput_24hr double precision,
	uo_rt_6hr double precision,
	uo_rt_12hr double precision,
	uo_rt_24hr double precision,
	uo_tm_6hr double precision,
	uo_tm_12hr double precision,
	uo_tm_24hr double precision
);
