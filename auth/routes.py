from flask import (
    render_template,
    request,
    redirect,
    flash,
    session
)
from auth.utils import verify_password
from database.db import get_connection
from auth.utils import hash_password
def register_user():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_connection()

        existing = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()

        if existing:

            flash(
                "Email already exists",
                "danger"
            )

            return render_template(
                "register.html"
            )

        hashed = hash_password(password)

        conn.execute(
            """
            INSERT INTO users
            (
                fullname,
                email,
                password
            )
            VALUES(?,?,?)
            """,
            (
                fullname,
                email,
                hashed
            )
        )

        conn.commit()

        flash(
            "Registration Successful",
            "success"
        )

        return redirect("/login")

    return render_template(
        "register.html"
    )

def login_user():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()

        conn.close()

        if user and verify_password(
            user["password"],
            password
        ):

            session["user_id"] = user["id"]
            session["fullname"] = user["fullname"]
            session["email"] = user["email"]

            flash(
                "Login Successful",
                "success"
            )

            return redirect("/dashboard")

        flash(
            "Invalid Email or Password",
            "danger"
        )

    return render_template("login.html")

def logout_user():

    session.clear()

    flash(
        "Logged Out Successfully",
        "info"
    )

    return redirect("/")