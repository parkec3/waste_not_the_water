
# waste_not_the_water

This repository is used for our group project for the DIRECT class as a tool for 
wastewater treatment plants. This tool can be used to predict capacity for a new 
European wastewater treatment plant and a visualization of the database from the Waste Water Treatment Directive. waste_not_the_water utilizes the open [Urban Waste Water Treatment database](https://www.eea.europa.eu/data-and-maps/data/waterbase-uwwtd-urban-waste-water-treatment-directive-5) from the [the European Environment Agency](https://www.eea.europa.eu/). Our primary use case is to create a data science tool that predicts capacity based on user inputs.

### Description of the model

Simple linear regression, ridge regression

### User Interface

Dash user interface

### Data Visualization

Done in folium

### Files setup

* The python modules are in waste_not_the_water directory.
* The useful data are organized into data directory
* The unit test files are in the directory called tests

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

For more information on how to use our tool, go to the examples folder.
