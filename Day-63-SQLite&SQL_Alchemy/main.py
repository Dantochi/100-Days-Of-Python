from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap4


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Bootstrap4(app)

all_books = []

# class Books(FlaskForm):
#     book_name = StringField("Book Name", validators=[DataRequired()])
#     book_author = StringField("Book Author", validators=[DataRequired()])
#     book_rating = StringField("Rating", validators=[DataRequired()])
#     submit = SubmitField('Add Book')
@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_name = request.form.get("book_name")
        book_author = request.form.get("book_author")
        book_rating = request.form.get("book_rating")
        all_books.append({
            "title": book_name,
            "author": book_author,
            "rating": book_rating
        })
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

