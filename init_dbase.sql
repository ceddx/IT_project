DROP TABLE IF EXISTS Players CASCADE ;
CREATE TABLE Players (
id_player serial PRIMARY KEY,
player_name  text  NOT NULL,
email  text  NOT NULL,
pass_word text NOT NULL
);


DROP TABLE IF EXISTS History;
CREATE TABLE History (
    id_history SERIAL PRIMARY KEY ,
    id_player integer REFERENCES Players(id_player),
    score integer,
    attempts  integer,
    article text
    );