from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)")

@app.route("/items", methods=["GET"])
def get_items():
    cursor.execute("SELECT * FROM items")
    return jsonify(cursor.fetchall())

@app.route("/items", methods=["POST"])
def add_item():
    data = request.json
    cursor.execute("INSERT INTO items (name) VALUES (?)", (data["name"],))
    conn.commit()
    return {"message": "Item added!"}

if __name__ == "__main__":
    app.run(debug=True)
