from flask import Flask, request
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)  # connect to DB


@app.route("/")
def home():
    return "hello world"


@app.post("/api/job")
def create_job():
    # the following data is data from client
    data = request.get_json()
    # title = data["title"]
    # location = data["location"]
    # salary = data["salary"]
    # currency = data["currency"]
    ################################
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO jobs (title, location, salary, currency) VALUES (%s, %s, %s, %s)",
                (
                    data["title"],
                    data["location"],
                    data["salary"],
                    data["currency"],
                ),
            )
            # rows = cursor.fetchone()
            return {"value inserted": "success"}


if __name__ == "__main__":
    app.run(debug=True)
