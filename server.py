from flask import Flask, jsonify, render_template, request, make_response
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/api/allpets', methods=['GET'])
def get_all_pets():
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
    if(connection):
      # clean up our connections
      cursor.close()
      conn.close()
      print("PostgreSQL connection is closed")

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

@app.route('/api/pets/delete')


  # If we're running in stand alone mode, run the application
if __name__ == '__main__':
  app.run(debug=True)
  get_all_pets()
  add_new_owner()