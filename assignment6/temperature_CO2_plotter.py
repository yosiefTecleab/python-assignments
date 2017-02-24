import csv
import matplotlib.pyplot as plt
import pandas as pd

def plot_temperature(month, from_year, to_year, y_axis_min, y_axis_max):
	"""
	function which plots the temperature from the data collected from file temperature.csv.
	arguements:
		month - month of the year
		from_year - starting year
		to_year - end year 
		y_axis_min - lower range temperature to plot
		y_axis_max - higher range temperature to plot
	"""
	plt.clf()
	df_temperature = pd.read_csv("temperature.csv")
	year = df_temperature["Year"].values
	temperature = df_temperature[month]
	plt.plot(year, temperature, color='black')
	coordinates = [from_year, to_year, y_axis_min, y_axis_max]
	plt.axis(coordinates)
	plt.title(month + " "+ str(from_year) + "-" + str(to_year))
	plt.xlabel("Year")
	plt.ylabel("Temperature")	
	plt.ylim(y_axis_min,y_axis_max) 
	plt.savefig('static/temperature.png') 
	
	

def plot_CO2(from_year, to_year, y_axis_min, y_axis_max):
	"""
	function that plots emitted co2 ,data collected from co2.csv file
	arguements:
		from_year - starting year
		to_year - end year 
		y_axis_min - lower range co2 to plot
		y_axis_max - higher range co2 to plot
	"""
	plt.clf()
	df_co2 = pd.read_csv("co2.csv")
	co2 = df_co2["Carbon"].values
	year = df_co2["Year"].values
	plt.plot(year, co2, color='black')
	coordinates = [from_year, to_year, y_axis_min, y_axis_max]
	plt.axis(coordinates)
	plt.title(" Amount of Cabon dioxide emitted in "+ str(from_year) + "-" + str(to_year)) 
	plt.ylabel("Carbon")
	plt.xlabel("Year")	
	plt.ylim(y_axis_min,y_axis_max) 
	plt.savefig('static/co2.png')
	#plt.clf()	
	#plt.show()
	
def plot_co2_by_country(year, upper_threshold, lower_threshold):
	"""
	function plots co2 emitted by different countries in the threshold range for given year.
	data are collected from the file co2_by_country.csv
	arguements:
		year-specific year to plot
		upper_threshold- the upper co2 threshold 
		lower_threshold- the lower co2 threshold
	"""
	plt.clf()
	with open("CO2_by_country.csv") as file:
		data = list(csv.reader(file)) 
		co2=[float(i[year-1960+4]) for i in data[1::] if i[year-1960+4]!="" and (float(i[year-1960+4])<=lower_threshold and float(i[year-1960+4])>=upper_threshold)  ] #  pass within threshold range 
		countries = [i[0] for i in data[1::] if i[year-1960+4]!="" and (float(i[year-1960+4])<=lower_threshold and float(i[year-1960+4])>=upper_threshold) ] 

	plt.xticks(range(len(co2)), countries,rotation='45', rotation_mode='anchor',ha='right',fontsize=4 )
	plt.bar(range(len(co2)),co2, align='center', width=0.4, linewidth=0.6) # vertical value y axis
	plt.title("CO2 Emission for all Countries for the year " + str(year))
	plt.xlabel("Country")
	plt.ylabel("Carbon emitted")
	plt.ylim(0,25)
	plt.xlim(0,90)
	plt.savefig('static/co2_by_country.png',dpi=200, bbox_inches='tight')
   
if __name__ == "__main__":
	plot_temperature("February",1864,2010,-5,5)
	plt.show()
	plot_CO2(1786,2012,8,800)
	plt.show()
	

