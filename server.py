from flask import Flask, jsonify
from flask import render_template
import psycopg2

app = Flask(__name__)

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

@app.route('/allpets', methods=['GET'])
def get_all_pets():
  # conn = None
  # try:
    # params = config()
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
  cur.close()

  # If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
    get_all_pets()