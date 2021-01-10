from flask import Flask, request, render_template
from flask_cors import cross_origin
import os
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        

        
        # latitude
        latitude = eval(request.form["latitude"])
        # print(latitude)
        
        # minimum_nights
        longitude = eval(request.form["longitude"])
        # print(longitude)

        # minimum_nights
        minimum_nights = int(request.form["minimum_nights"])
        # print(minimum_nights)
        
        # availability_365
        #availability_365 = eval(request.form["availability_365"])
        # print(availability_365)
        
        # calculated_host_listings_count
        calculated_host_listings_count = int(request.form["calculated_host_listings_count"])
        # print(calculated_host_listings_count)

        # Neighbourhood group
        # Neighbourhood group = 0 (not in column)
        neighbourhood_group=request.form['neighbourhood_group']
        if(neighbourhood_group=='Brooklyn'):
            Brooklyn = 1
            Manhattan = 0
            Queens = 0
            Staten_Island = 0
            Bronx = 0
            

        elif (neighbourhood_group=='Manhattan'):
            Brooklyn = 0
            Manhattan = 1
            Queens = 0
            Staten_Island = 0
            Bronx = 0 

        elif (neighbourhood_group=='Queens'):
            Brooklyn = 0
            Manhattan = 0
            Queens = 1
            Staten_Island = 0
            Bronx = 0 
            
        elif (neighbourhood_group=='Staten Island'):
            Brooklyn = 0
            Manhattan = 0
            Queens = 0
            Staten_Island = 1
            Bronx = 0 

        else:
            Brooklyn = 0
            Manhattan = 0
            Queens = 0
            Staten_Island = 0
            Bronx = 0 
            

       
        room_type = request.form["room_type"]
        if (room_type == 'Private room'):
            Private_room = 1
            Entire_home_apt = 0
            Shared_room = 0
            

        elif (room_type == 'Entire home/apt'):
            Private_room = 0
            Entire_home_apt = 1
            Shared_room = 0

      
        else:
            Private_room = 0
            Entire_home_apt = 0
            Shared_room = 0


        
        prediction=model.predict([[
            latitude,
            longitude,
            minimum_nights,
            calculated_host_listings_count,
            Brooklyn,
            Manhattan,
            Queens,
            Staten_Island,
            Bronx,
            Private_room,
            Entire_home_apt,
            Shared_room
           
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Room price is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
