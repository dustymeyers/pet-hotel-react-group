from flask import Flask, jsonify, render_template, request, make_response
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

### GET Routes ###

@app.route('/api/pets/all', methods=['GET'])
def get_all_pets():
  try:
    # Connect to your postgres DB
    conn = psycopg2.connect(
      # Change this info to fit your DB
      """
      dbname=pet-hotel
      host=localhost
      user=joshgulledge
      port=5432
      """
    )
    cur = conn.cursor()
    # Execute a query
    cur.execute("""
    SELECT "pets".*, "owners".first_name, "owners".last_name FROM "pets"
    JOIN "owners" ON "pets".owner_id = "owners".id
    GROUP BY "owners".id, "pets".id
    ORDER BY "pets".id;
    """)
    # Retrieve query results
    pets = cur.fetchall()
    print("The number of pets: ", cur.rowcount)
    for row in pets:
      print(row)
    # returns all pets as an array of arrays
    return jsonify(pets)
  except (Exception, psycopg2.Error) as error:
    print(error)
  finally:
    # closing database connection.
    if(conn):
      # clean up our connections
      cur.close()
      conn.close()
      print("PostgreSQL connection is closed")

@app.route('/api/owners/all', methods=['GET'])
def get_all_owners():
  try:
    # Connect to your postgres DB
    conn = psycopg2.connect(
      # Change this info to fit your DB
      """
      dbname=pet-hotel
      host=localhost
      user=patricknelson
      port=5432
      """
    )
    cur = conn.cursor()
    # Execute a query
    cur.execute("""
    SELECT COUNT(*), "owners".* FROM "pets"
    JOIN "owners" ON "pets".owner_id = "owners".id
    GROUP BY "owners".id;
    """)
    # Retrieve query results
    owners = cur.fetchall()
    print("The number of owners: ", cur.rowcount)
    for row in owners:
      print(row)
    # returns all pets as an array of arrays
    return jsonify(owners)
  except (Exception, psycopg2.Error) as error:
    print(error)
  finally:
    # closing database connection.
    if(conn):
      # clean up our connections
      cur.close()
      conn.close()
      print("PostgreSQL connection is closed")

### POST Routes ###

@app.route('/api/owner/add', methods=['POST'])
def add_new_owner():
  print(f'request, {request} request.json, {request.json}')
  first_name = request.json['first_name']
  last_name = request.json['last_name']
  print(f'first_name {first_name}, last_name{last_name}')
  try:
    # Connect to your postgres DB
    conn = psycopg2.connect(
      # Change this info to fit your DB
      """
      dbname=pet-hotel
      host=localhost
      user=patricknelson
      port=5432
      """
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    post_query = """
      INSERT INTO "owners" ("first_name", "last_name")
      VALUES (%s, %s);"""
    cur.execute(post_query, (first_name, last_name))
    conn.commit()
    count = cur.rowcount
    print('number of owners added:', count)
    # respond nicely
    result = {'status': 'CREATED'}
    return make_response(jsonify(result), 201)
  except (Exception, psycopg2.Error) as error:
    # there was a problem
    if(conn):
      print("Failed to insert owner", error)
      # respond with error
      result = {'status': 'ERROR'}
      return make_response(jsonify(result), 500)
  finally:
    # closing database connection.
    if(conn):
      # clean up our connections
      cur.close()
      conn.close()
      print("PostgreSQL connection is closed")

@app.route('/api/pets/add', methods=['POST'])
def add_new_pet():
  pet_name = request.json['pet_name']
  pet_breed = request.json['pet_breed']
  color = request.json['color']
  owner_id = request.json['owner_id']

  try:
    # Connect to your postgres DB
    conn = psycopg2.connect(
      # Change this info to fit your DB
      """
      dbname=pet-hotel
      host=localhost
      user=patricknelson
      port=5432
      """
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    post_query = """
      INSERT INTO "pets" ("name", "breed", "color", "owner_id")
      VALUES (%s, %s, %s, %s);"""
    cur.execute(post_query, (pet_name, pet_breed, color, owner_id))
    conn.commit()
    count = cur.rowcount
    print('number of pets added:', count)
    # respond nicely
    result = {'status': 'CREATED'}
    return make_response(jsonify(result), 201)
  except (Exception, psycopg2.Error) as error:
    # there was a problem
    if(conn):
      print("Failed to insert pets", error)
      # respond with error
      result = {'status': 'ERROR'}
      return make_response(jsonify(result), 500)
  finally:
    # closing database connection.
    if(conn):
      # clean up our connections
      cur.close()
      conn.close()
      print("PostgreSQL connection is closed")

### DELETE Routes ###

@app.route('/api/pets/delete/<int:id>', methods=['DELETE'])
def delete_pet(id):
  print('id', id)
  try:
    conn = psycopg2.connect(
      """
      dbname=pet-hotel
      host=localhost
      user=patricknelson
      port=5432
      """
    )
    cur = conn.cursor()
    delete_query = 'DELETE FROM "pets" WHERE "id" = %s;'
    cur.execute(delete_query, (id,))
    conn.commit()
    count = cur.rowcount
    print('Number of deletes:', count)
    result = {'status': 'DELETED'}
    return make_response(jsonify(result), 200)
  except (Exception, psycopg2.Error) as error:
    # there was a problem
    if(conn):
      print("Failed to delete pet", error)
      # respond with error
      result = {'status': 'ERROR'}
      return make_response(jsonify(result), 500)
  finally:
    # closing database connection.
    if(conn):
      # clean up our connections
      cur.close()
      conn.close()
      print("PostgreSQL connection is closed")

@app.route('/api/owner/delete/<int:id>', methods=['DELETE'])
def delete_owner(id):
  print('id', id)
  try:
    conn = psycopg2.connect(
      """
      dbname=pet-hotel
      host=localhost
      user=patricknelson
      port=5432
      """
    )
    cur = conn.cursor()
    delete_query = 'DELETE FROM "owners" WHERE "id" = %s;'
    cur.execute(delete_query, (id,))
    conn.commit()
    count = cur.rowcount
    print('Number of deletes:', count)
    result = {'status': 'DELETED'}
    return make_response(jsonify(result), 200)
  except (Exception, psycopg2.Error) as error:
    # there was a problem
    if(conn):
      print("Failed to delete owner", error)
      # respond with error
      result = {'status': 'ERROR'}
      return make_response(jsonify(result), 500)
  finally:
    # closing database connection.
    if(conn):
      # clean up our connections
      cur.close()
      conn.close()
      print("PostgreSQL connection is closed")

### PUT Routes ###

# Pet Check In Status Update
@app.route('/api/pets/update/<int:id>', methods=['PUT'])
def update_pet(id):
  update_check_in = request.json['update_check_in']
  print('id', id)
  try:
    conn = psycopg2.connect(
      """
      dbname=pet-hotel
      host=localhost
      user=patricknelson
      port=5432
      """
    )
    cur = conn.cursor()
    update_query = 'UPDATE pets SET is_checked_in = %s WHERE id = %s;'
    cur.execute(update_query, (update_check_in, id))
    conn.commit()
    count = cur.rowcount
    print('Number of updates:', count)
    result = {'status': 'UPDATED'}
    return make_response(jsonify(result), 200)
  except (Exception, psycopg2.Error) as error:
    # there was a problem
    if(conn):
      print("Failed to update pet", error)
      # respond with error
      result = {'status': 'ERROR'}
      return make_response(jsonify(result), 500)
  finally:
    # closing database connection.
    if(conn):
      # clean up our connections
      cur.close()
      conn.close()
      print("PostgreSQL connection is closed")

  # If we're running in stand alone mode, run the application
if __name__ == '__main__':
  app.run(debug=True)