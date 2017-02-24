import pandas as pd
import csv
from flask import Flask, render_template, request, redirect, url_for, make_response
import temperature_CO2_plotter
import sys
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/temperature/", methods=["GET", "POST"])
def temperature():
	df_temp = pd.read_csv("temperature.csv")
	year = df_temp["Year"].values
	month = df_temp.dtypes.index[1:]

	min_yr= df_temp["Year"].min()

	max_temp=df_temp["January"].max() 
	min_temp=df_temp["January"].min()
	for mn in month:       
	   if  df_temp[mn].values.max() > max_temp: 
		   max_temp=df_temp[mn].max()
	   if  df_temp[mn].min() < min_temp: 
		   min_temp=df_temp[mn].min()

	if request.method == "GET": 
		return render_template("temperature.html", month = month, year = year, min_temp=int(min_temp) ,max_temp=int(max_temp))
	elif request.method == "POST": 
		month = request.form["month"]
		from_year = int(request.form["from_year"])
		to_year = int(request.form["to_year"])
		y_axis_min = int(request.form["y_axis_min"])
		y_axis_max = int(request.form["y_axis_max"])	

		temperature_CO2_plotter.plot_temperature(month,from_year,to_year,y_axis_min,y_axis_max) 

		return render_template("image_generated.html", image_name="temperature.png" )


	
@app.route("/co2/", methods=["GET", "POST"])
def co2():
	df_co2 = pd.read_csv("co2.csv")
	year = df_co2["Year"].values

	min_co2=df_co2["Carbon"].min()
	max_co2=df_co2["Carbon"].max()

	if request.method == "GET":
	   return render_template("co2.html", year = year ,min_co2=int(min_co2), max_co2=int(max_co2) )
	elif request.method == 'POST' :
		from_year=int(request.form["from_year"])
		to_year=int(request.form["to_year"])
		y_axis_min=int(request.form["y_axis_min"])
		y_axis_max=int(request.form["y_axis_max"])	
		temperature_CO2_plotter.plot_CO2(from_year,to_year,y_axis_min,y_axis_max) 
		return render_template("image_generated.html", image_name="co2.png")
     
@app.route("/random_temp_plot/")
def random_temp_plot():
    temperature_CO2_plotter.plot_temperature("February",1864,2010,-5,5) 
    return render_template("image_generated.html", image_name="temperature.png")

	
@app.route("/random_co2_plot/")
def random_co2_plot():
	temperature_CO2_plotter.plot_CO2(1786,2012,8,800)
	return render_template("image_generated.html", image_name="co2.png")

	
@app.route("/co2_by_country/", methods=["GET", "POST"])
def co2_by_country():
    
	df = pd.read_csv("CO2_by_country.csv")
	year = df.dtypes.index[4:]		
	
	if request.method == "GET":
	   return render_template("co2_by_country.html", year = year)		
	elif request.method == 'POST' : 
		yr = int(request.form["yr"])      
		y_axis_min = float(request.form["y_axis_min"])
		y_axis_max = float(request.form["y_axis_max"])       
		temperature_CO2_plotter.plot_co2_by_country(yr,y_axis_min,y_axis_max)        
		return render_template("image_generated.html", image_name="co2_by_country.png")

@app.route("/help/")
def help():
	os.system("pydoc -w temperature_CO2_plotter")
	os.system("mv temprature_CO2_plotter.html ./templates")	#move to templates
	return render_template("temperature_CO2_plotter.html")

# avoiding  caching:
@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response
	
    
if __name__ == "__main__":
    app.run(debug=True)
