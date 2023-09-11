from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
import create_data


@app.route("/")
def home():
    data = create_data.generate_data()
    return render_template("table.html", data= data)


if __name__ == "__main__":
    app.run(debug=True)