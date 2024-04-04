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
        for column in self.__table__.columns: # The self.__table__.columns is a list that contains the list available in the table "Cafe" such as [cafe.id, cafe.location, etc.]
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name) # The column.name prints the name of the columns in string format
            print(column.name)
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
        cafe_table = random.choice(db.session.execute(db.select(Cafe)).scalars().all())
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


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
