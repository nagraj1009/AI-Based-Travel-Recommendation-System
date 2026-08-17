from flask import Flask, render_template
from auth.decorators import login_required
from services.gemini_service import generate_itinerary
from flask import request
from urllib.parse import quote
from database.db import initialize_database
from auth.utils import bcrypt
from flask import send_file
from services.pdf_service import generate_pdf
from auth.routes import register_user
from auth.routes import (
    register_user,
    login_user,
    logout_user
)

app = Flask(__name__)

app.config["SECRET_KEY"] = "travel_secret_key"

bcrypt.init_app(app)

initialize_database()

latest_trip = None
@app.route("/")
def home():
    return render_template("home.html")

@app.route(
    "/register",
    methods=["GET","POST"]
)
def register():
    return register_user()

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():
    return login_user()


@app.route("/logout")
def logout():
    return logout_user()

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template(
        "dashboard.html"
    )
@app.route("/planner", methods=["GET", "POST"])
@login_required
def planner():

    trip = None

    flight_link = None
    train_link = None
    bus_link = None
    maps_link = None

    if request.method == "POST":

        source = request.form["source"]
        destination = request.form["destination"]
        budget = request.form["budget"]
        days = request.form["days"]
        style = request.form["style"]

        try:

            trip = generate_itinerary(
                source,
                destination,
                budget,
                days,
                style
            )
            global latest_trip
            latest_trip = trip

        except Exception as e:

            trip = {
                "title": "Error",
                "overview": str(e),
                "days": [],
                "hotel": "",
                "food": "",
                "transport": "",
                "budget": ""
            }

        flight_link = "https://www.google.com/travel/flights"

        train_link = (
            f"https://www.google.com/search?q="
            f"{quote(source + ' to ' + destination + ' train')}"
        )

        bus_link = (
            f"https://www.google.com/search?q="
            f"{quote(source + ' to ' + destination + ' bus')}"
        )

        maps_link = (
            f"https://www.google.com/maps/search/"
            f"{quote(destination)}"
        )

    return render_template(
        "planner.html",
        trip=trip,
        flight_link=flight_link,
        train_link=train_link,
        bus_link=bus_link,
        maps_link=maps_link
    )

@app.route("/download-pdf")
@login_required
def download_pdf():

    global latest_trip

    if not latest_trip:

        return "Generate an itinerary first."

    filename = "exports/itinerary.pdf"

    generate_pdf(
        latest_trip,
        filename
    )

    return send_file(
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)