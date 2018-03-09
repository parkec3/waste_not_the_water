######################################################################
# imports
######################################################################

import dash
import dash_html_components as html
import dash_core_components as dcc

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
	html.H1(children='Machine Learning Model'),
	html.Div([
		html.P('The model takes five inputs: agglomeration size, latitude,'
		' longitude, nitrogen removal, and phosphorous removal. To predict'
		' capacity size, fill out the form below and press submit.')
	]),
#	html.Br,
	html.Div([
		html.P('Input the agglomeration size.'
	)]),
	# text input for agglomeration
	dcc.Input(
		id='input-agg-box',
		placeholder='Enter a value...',
		type='text',
		value=''
	),
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
	# Submit button, make the model only run after it's pressed
	html.Button('Submit', id='button'),
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
	# Input from the agg text box
	[dash.dependencies.State('input-agg-box', 'value'),
	# Input from the lat text box
	dash.dependencies.State('input-lat-box', 'value'),
	# Input from the lon text box
	dash.dependencies.State('input-lon-box', 'value'),
	# Input from the checkboxes, is it one or more inputs because it's
	# multiple values?
	dash.dependencies.State('checklist', 'values')])
def update_output(n_clicks, value_agg, value_lat, value_lon,
 checkboxes_values):
	return '{}, {}, {}, {}'.format(value_agg, value_lat, value_lon,
 checkboxes_values)

######################################################################
# For nicer text
######################################################################

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

######################################################################
# Run the app locally
######################################################################

if __name__ == '__main__':
	app.run_server(debug=True)