create table if not exists weather(
	STATE varchar(20),
	DESCRIPTION varchar(255),
	TEMPERATURE decimal,
	FEELS_LIKE_TEMPERATURE decimal,
	MIN_TEMPERATURE decimal,
	MAX_TEMPERATURE decimal,
	HUMIDITY numeric,
	CLOUDS numeric
);