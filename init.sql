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
