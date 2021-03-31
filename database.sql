create table "owners" (
	"id" SERIAL PRIMARY KEY,
	"first_name" VARCHAR (256),
	"last_name" VARCHAR (256)
);

create table "pets" (
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR (256),
	"breed" VARCHAR (256),
	"is_checked_in" boolean NOT NULL DEFAULT False,
	"owner_id" int REFERENCES "owners" ON DELETE CASCADE NOT NULL 
);

INSERT INTO "owners" ("first_name", "last_name")
VALUES ('Dusty', 'Meyers'), ('Zack', 'Werner');

INSERT INTO "pets" ("name", "breed", "owner_id")
VALUES ('Lilo', 'Tabby', 1), ('Tucker', 'Golden Retriever', 2);