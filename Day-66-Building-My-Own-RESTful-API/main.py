from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
""""
So basically the class below created is for a row of data 
and for every row that is created is a new instance of the "Cafe" class
"""


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            """
            The self.__table__.columns is a list 
            that contains the columns available in the table "Cafe" such as [cafe.id, cafe.location, etc.] 
            for a particular row of data
            Create a new dictionary entry;
            where the key is the name of the column
            and the value is the value of the column 
            """
            dictionary[column.name] = getattr(self, column.name)  # The column.name prints the name of the columns in
            # string format
            print(dictionary[column.name])
        print(dictionary)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_cafe():
    if request.method == "GET":
        cafe_table = random.choice(
            db.session.execute(db.select(Cafe)).scalars().all())  # The selects all the rows of data in the table
        print(cafe_table)
        return jsonify(cafe=cafe_table.to_dict()
                       # "id": cafe_table.id,
                       # "name": cafe_table.name,
                       # "map_url": cafe_table.map_url,
                       # "location": cafe_table.location,
                       #
                       # # The below is a sub-category
                       # "amenities": {
                       #     "has_sockets": cafe_table.has_sockets,
                       #     "has_toilet": cafe_table.has_toilet,
                       #     "has_wifi": cafe_table.has_wifi,
                       #     "can_take_calls": cafe_table.can_take_calls,
                       #     "seats": cafe_table.seats,
                       #     "coffee_price": cafe_table.coffee_price
                       # }
                       )
        # print(result)


@app.route("/all")
def all_cafe():
    # select the table
    # get the list of the rows of data
    # create a loop that applies the to_dict function to each of the row objects in that list
    if request.method == "GET":
        cafe_data = db.session.execute(db.select(Cafe)).scalars().all()
        return jsonify(cafe=[data.to_dict() for data in cafe_data]) # Lists seem to be the best method for getting groups of method


@app.route("/search")
def locate_cafe():
    # select the table
    # apply a filter of some sorts
    # return it as a JSON
    user_input = request.args.get('loc')
    table_data = db.session.execute(db.select(Cafe).where(Cafe.location == user_input)).scalars().all()
    print(user_input)
    print(table_data)
    # filtered_data = table_data.where(table_data.c.location == user_input).scalars().all()
    if table_data:
        return jsonify(cafe=[data.to_dict() for data in table_data])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
