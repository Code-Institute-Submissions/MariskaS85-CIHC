import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for
    )
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env 


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_words")
def get_words():
    words = mongo.db.words.find()
    return render_template("home.html", words=words)

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    words = list(mongo.db.words.find({"$text": {"$search": query}}))
    return render_template("home.html", words=words)



@app.route("/add_words", methods=["GET", "POST"])
def add_words():
    if request.method == "POST":
        words = {
            "word": request.form.get("word"),
            "translation": request.form.get("translation"),
            "category_name": request.form.get("category_name"),
            "slc": request.form.get("slc"),
            "tlc": request.form.get("tlc"),
            "meaning": request.form.get("meaning"),
            "usage": request.form.get("usage"),
            "created_on": request.form.getTimestamp("created_at"),
        }

        mongo.db.words.insert_one(words)
        flash("thanks for your contribution to the CIHC dictionairy")
        return redirect(url_for("get_words"))

    category = mongo.db.category.find().sort("category_name", 1)
    return render_template("add.html", category=category)




@app.route("/edit_words/", methods=["GET","POST"])
def edit_words(words_id):
    if request.method == "POST":
        words_id = {
            "word": request.form.get("word"),
            "translation": request.form.get("translation"),
            "category_name": request.form.get("category_name"),
            "slc": request.form.get("slc"),
            "tlc": request.form.get("tlc"),
            "meaning": request.form.get("meaning"),
            "usage": request.form.get("usage"),
            "created_on": request.form.getTimestamp("created_at"),
        }

    mongo.db.words.update({"_id": ObjectId(words_id)}, submit)

    task = mongo.db.tasks.find_one({"_id": ObjectId(words_id)})
    words = mongo.db.words.find().sort("word", 1)
    return render_template("edit.html", words=words)

@app.route("/delete_word")
def delete_word(words_id):
    mongo.db.words.remove({ "_id": ObjectId(words_id)})
    return redirect(url_for("edit_words"))



@app.route("/about_page")
def about_page():
    words = mongo.db.words.find()
    return render_template("about.html", words=words)

if __name__=="__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)