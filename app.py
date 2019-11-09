from flask import Flask, render_template, redirect

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo


# Create an instance of our Flask app.
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/UFO"
mongo = PyMongo(app)


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    ufo_data = mongo.db.alien_data.find_one()

      console.log(ufo_data)

# render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", ufo_data=ufo_data)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

