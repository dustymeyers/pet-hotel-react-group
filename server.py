from flask import Flask, jsonify
from flask import render_template
import psycopg2

app = Flask(__name__)

# Connect to your postgres DB
conn = psycopg2.connect(
  # Change this info to fit your DB
  """
  dbname=
  host=localhost
  user=patricknelson
  port=5432
  """
) 

cur = conn.cursor()

@app.route('/allconsoles', methods=['GET'])
def get_all_consoles():
  # conn = None
  # try:
    # params = config()
  # Execute a query
  cur.execute('SELECT * FROM "consoles"')
  # Retrieve query results
  records = cur.fetchall()
  print("The number of consoles: ", cur.rowcount)
  for row in records:
    print(row)
  return jsonify({'consoles': records})
  cur.close()

  # If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
    get_all_consoles()