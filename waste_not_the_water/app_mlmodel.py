######################################################################
# imports
######################################################################

import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import linear_regression

######################################################################
# this is what goes into the app
######################################################################

# Features: Member State, latitude, longitude, load entering, NRemoval,
# PRemoval
# Inputs for agglomeration - text input
# goes as inpput to function for machine learning model
# checkboxes for yes/no features
# latitude/longitude data - inputs
# inputs for average temperature - text input
# temperature could be optional since we can use the temp database

app = dash.Dash()

app.layout = html.Div(children=[
	html.H2(children='Predictive Urban Waste Water Treament Model'),
	html.Div([
		html.P('The model takes five inputs: size of load entering, latitude,'
		' longitude, nitrogen removal, and phosphorous removal. To predict'
		' capacity size, fill out the form below and press submit.'
		' For more information on model details, see the README page.')
	]),
	html.Hr(),
	html.Div([
		html.P('What is the size of the load entering?'
	)]),
	# text input for agglomeration
	dcc.Input(
		id='input-load-box',
		placeholder='Enter a value...',
		type='text',
		value=''
	),
	html.Br(),
	html.Br(),
	html.Div([
		html.P('What is the latitude coordinate?'
	)]),
	# text input for latitude
	dcc.Input(
		id='input-lat-box',
		placeholder='Enter a value...',
		type='text',
		value=''
	),
	html.Br(),
	html.Br(),
	html.Div([
		html.P('What is the longitude coordinate?'
	)]),
	# text input for longitude
	dcc.Input(
		id='input-lon-box',
		placeholder='Enter a value...',
		type='text',
		value=''
	),
	html.Br(),
	html.Br(),
	# checkboxes for the yes/no input for Nitrogen and Phosphorous
	# removal
	dcc.Checklist(
		id='checklist',
		options=[
			{'label': 'Nitrogren Removal', 'value': 'NRemoval'},
			{'label': 'Phosphorous Removal', 'value': 'PRemoval'}
		],
		values=[] # do I need this for no check boxes or will it raise an error?
	),
	html.Br(),
	# Submit button, make the model only run after it's pressed
	html.Button('Submit', id='button'),
	html.Br(),
	html.Div(id='output-container-button',
			 children='Press submit after desired values have been input.')
])

######################################################################
# Interactive part
######################################################################

@app.callback(
	# Output after the button is pressed. just text.
	dash.dependencies.Output('output-container-button', 'children'),
	# Input from the button, number of clicks
	[dash.dependencies.Input('button', 'n_clicks')],
	# Input from the load text box
	[dash.dependencies.State('input-load-box', 'value'),
	# Input from the lat text box
	dash.dependencies.State('input-lat-box', 'value'),
	# Input from the lon text boxt
	dash.dependencies.State('input-lon-box', 'value'),
	# Input from the checkboxes, is it one or more inputs because it's
	# multiple values?
	dash.dependencies.State('checklist', 'values')])
def output_model(n_clicks, value_load, value_lat, value_lon,
	checkboxes_values):
	"""
	This function updates the user interface with the output from the
	Ridge Linear Regression model with the user-supplied inputs.
	"""
	##### if user inputs values other than numbers, print an error
	##### telling them to give numeric values
	try:
		float(value_lat)
		float(value_load)
		float(value_lon)
	except (Exception):
		return 'Error: input values must be numeric values. Try again.'
	else:
		dataframe_dict = {
			'Latitude': [float(value_lat)], 'Longitude': [float(value_lon)],
			'LoadEntering': [float(value_load)]
		}
		user_input_df = pd.DataFrame(data=dataframe_dict)
		filename_rr = "ridge_result.sav"
		filename_lr = "linear_result.sav"
		answer = linear_regression.customer_inter(
	 		user_input_df, filename_lr, filename_rr
		)
		return 'Capacity size for these inputs is predicted to be {}'.format(
		round(answer[1][0]))

######################################################################
# For nicer text
######################################################################

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

######################################################################
# Run the app locally
######################################################################

if __name__ == '__main__':
	app.run_server(debug=True)