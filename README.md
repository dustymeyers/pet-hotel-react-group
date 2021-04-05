# Pet Hotel Python Server

## Description

_Duration: 1 Day Sprint_
Given 48 hours to learn enough about the software language, Python. Students were put into groups and charge with putting together a RESTful api server that communicates between a database and clientside browser page. The files included in this GitHub repository are specific to the server and database for this project. A link to the client side repository can be found [here](https://github.com/dustymeyers/pet_hotel_client).

The Pet Hotel app has two major views, a `pet owners manager` view and a `dashboard` view. On the pet owners view, pet owners can be added to the database by form entry. All owners in the database are displayed on this page as well as the number of pets that are assigned to the owner. Pets can be added in the dashboard view including their name, breed, color, and their owner. By default, all pets are considered checked in. Pets and owners both can be deleted. This version does not include the full pet table view for the dashboard page, but the API route has been setup for easy setup in future versions.

### Prerequisites

- [Python](https://www.python.org/)
- [Flask](https://palletsprojects.com/p/flask/)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [Postico](https://eggerapps.at/postico/)

## Installation
1. Create a database named `pet-hotel`,
2. The queries in the `database.sql` file are set up to create all the necessary tables and populate the needed data to allow the application to run correctly. The project is built on [Postgres](https://www.postgresql.org/download/), so you will need to make sure to have that installed. We recommend using Postico to run those queries as that was used to create the queries.
3. Open your editor of choice and run `python3 -m venv venv`.
4. Run `venv/bin/activate` in your terminal.
5. Run `pip3 install Flask` in your terminal.
6. Run `pip3 install psycopg2-binary` in your terminal.
7. Run `export FLASK_APP=server.py` in your terminal.
8. Run `flask run` in your terminal to boot up the server.
9. For clientside installation view the clientside repostiory [here](https://github.com/dustymeyers/pet_hotel_client).

## Usage
1. As a user, I can add owners to the database that are registering at the hotel.
2. As a user, I can add pets for each owner to the database.
3. As a user, I can view all owners from the database that are registered to the hotel.
4. As a user, I can see how many pets each owner has at the hotel.

## Built With
This serverside application was built with Python, Flask, SQL, and psycopg2.

## Acknowledgement
Thanks to [Prime Digital Academy](www.primeacademy.io) who equipped and helped me to make this application a reality. And a special thanks to Zack Werner, Patrick Nelson, and Josh Gulledge for being outstanding teammates.

