CREATE TABLE users (
    "id" serial PRIMARY KEY,
    "email" text NOT NULL UNIQUE,
    "username" varchar(25) NOT NULL UNIQUE,
    "password" text NOT NULL


);

CREATE TABLE numbers (
    "id" serial PRIMARY KEY,
    "users" text NOT NULL,
    "number" integer NOT NULL,
    user_id integer REFERENCES users
);

-- SELECT n.number
-- FROM numbers n
-- WHERE n.user_id = 3

CREATE TABLE teams (
    "id" serial,
    "name" text NOT NULL,
    PRIMARY KEY ("id"),
    UNIQUE ("name")
);

CREATE TABLE events (
    "id" serial,
    "team1" integer NOT NULL,
    "team2" integer NOT NULL,
    "datetime" timestamp without time zone NOT NULL,
    "type" text NOT NULL,
    PRIMARY KEY ("id"),
    CONSTRAINT "events_team1_fkey" FOREIGN KEY ("team1") REFERENCES teams(id),
    CONSTRAINT "events_team2_fkey" FOREIGN KEY ("team2") REFERENCES teams(id)
);
