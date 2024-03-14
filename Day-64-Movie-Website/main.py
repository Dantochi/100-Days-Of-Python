from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
# Create the app
app = Flask(__name__)
# Create the app
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
# initialize the app with the extension
db.init_app(app)

Bootstrap5(app)


class MyForm(FlaskForm):
    rating = FloatField(label="Your rating out of ten", validators=[DataRequired()])
    review = StringField(label="Your review", validators=[DataRequired(), Length(min=0, max=250)])
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    movie_title = StringField(label="Movie Title 🎬", validators=[DataRequired(), Length(min=0, max=250)])
    submit = SubmitField("Add movie")


# CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


# with app.app_context():
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )

# db.session.add(second_movie)
# db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit(user_id):
    form = MyForm()
    if form.validate_on_submit():
        movie = db.get_or_404(Movie, user_id)  # This is to get the movie record by the user id from the "Movie" table
        # print(movie.title)
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect("/")

    return render_template("edit.html", form=form)


@app.route("/delete_movie/<user_id>")
def delete(user_id):
    movie = db.get_or_404(Movie, user_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add")
def add():
    add_form = AddForm()
    return render_template('add.html', form=add_form)


if __name__ == '__main__':
    app.run(debug=True)
