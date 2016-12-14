CREATE TABLE users (
    "id" serial,
    "email" text NOT NULL UNIQUE,
    "username" varchar(25) text NOT NULL UNIQUE,
    "Password" text NOT NULL,

    PRIMARY KEY ("id"),
    UNIQUE ("name")
);

CREATE TABLE events (
    "id" serial,
    "users" text NOT NULL,
    "number" integer NOT NULL,
    "type" text NOT NULL,
    PRIMARY KEY ("id"),
    CONSTRAINT "events_team1_fkey" FOREIGN KEY ("team1") REFERENCES teams(id),
    CONSTRAINT "events_team2_fkey" FOREIGN KEY ("team2") REFERENCES teams(id)
);
