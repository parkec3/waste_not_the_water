
# waste_not_the_water

waste_not_the_water is data science tool for urban waste water treatment 
plants created through the [DIRECT courses](https://uwdirect.github.io/) at
 University of Washington. This tool can be used to predict capacity for a new 
European wastewater treatment plant and a visualization of the database from the 
Waste Water Treatment Directive. waste_not_the_water utilizes the open 
[Urban Waste Water Treatment database](https://www.eea.europa.eu/data-and-maps/data/waterbase-uwwtd-urban-waste-water-treatment-directive-5) from the 
[the European Environment Agency](https://www.eea.europa.eu/). 
Our primary use case is to create a data science tool that predicts capacity based 
on user inputs; this was done with the use of a user interface. waste_not_the_water 
also contains interactive data visualization showing the size and location of the 
existing waste water treatment infrastructure in Europe.

---

### Description of the model

#### Regression Model

The features of our model are the load entering and the location in latitude and 
longitude. There exists a linear relationship between the capacity and the load 
entering the treatment plant, and we implemented simple linear regression. However, 
after examining multilinear statistics, it can be seen that latitude and longitude 
also affect the capacity. A Ridge Regression model was used due to the high variance
 in the data. The R<sup>2</sup> statistic for Ridge Regression is 0.91. 

_Note on units: capacity and load entering are given in population equivalent, a 
common water treatment unit that is normalized based on the amount of water usage
 for one person in 24 hours._

#### Nearest Neighbors

To give the user more information, a nearest neighbor algorithm was implemented that
will return the two closest plants to the user's inputs. This is done through a simple 
distance calculation of weighted capacity and location coordinates. The phosphate and 
nitrogen removal are used as filters to further specify the treatment plants.

### Data Visualization

The interactive maps were created with folium and mpl_toolkits.basemap. The figures
 allow us to clearly identify the area where most waste water treatment plants
 are located in Europe.

Relative size by dot       |  Size by color
:-------------------------:|:-------------------------:
![](https://github.com/parkec3/waste_not_the_water/blob/master/waste_not_the_water/dotsMap.png)  |  ![](https://github.com/parkec3/waste_not_the_water/blob/master/waste_not_the_water/ColourgroupMap.png)

![Location relative to dot size](https://github.com/parkec3/waste_not_the_water/blob/master/waste_not_the_water/dotsMap.png) ![Color Map](https://github.com/parkec3/waste_not_the_water/blob/master/waste_not_the_water/ColourgroupMap.png)

### User Interface

The user interface was created with the use of Dash by Plotly. Dash uses a python
 background that is converted into html. Our app is run locally on the web. Users 
 can input their proposed plant feautures on the app, and it returns the capacity 
 through the Ridge Regression model. The app is called through the command
 `python app.py`. The app runs locally on the web through this
 [url](http://127.0.0.1:8050/). For more information on Dash, check out their
 awesome [website](https://dash.plot.ly/getting-started).

### Files setup

* The python modules are in `waste_not_the_water` directory.
* The useful data are organized into `data` directory.
* The unit test files are in the directory called `tests`.

### Dependencies you need

This is what dependencies you need:
* basemap
* folium
* sklearn
* statsmodels
* scipy
* dash by plotly

### Installation

This is how you install it:
* $conda install basemap / pip install basemap
* $conda install folium / pip install folium
* $conda install scilit-learn / pip install -U scikit-learn
* $conda install statsmodels / pip install --upgrade --no-deps statsmodels
* $conda install scipy / pip install scipy
* $conda install dash==0.21.0/ pip install dash==0.21.0
* $conda install dash-renderer==0.11.3 / pip install dash-renderer==0.11.3
* $conda install dash-html-components==0.9.0 / pip install dash-html-components==0.9.0
* $conda install dash-core-components==0.21.0 / pip install dash-core-components==0.21.0
* $conda install plotly --upgrade / pip install plotly --upgrade

### Examples

For more information on how to use our package, go to the `examples` folder.

### Acknowledgments

We would like to profusely thank our wonderful instructor, Prof. David Beck, and our 
amazing teaching assistants, Nick Montoni, Arushi Prakash, and Coco Mao.