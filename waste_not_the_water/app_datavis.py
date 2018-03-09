######################################################################
# imports
######################################################################

import dash
import dash_html_components as html
import dash_core_components as dcc

######################################################################
# this is what goes into the app
######################################################################

app = dash.Dash()

app.layout = html.Div([
	dcc.Checklist(
		options=[
			{'label': 'Agglomeration 1', 'value': '1'},
			{'label': 'Agglomeration 2', 'value': '2'},
			{'label': 'Agglomeration 3', 'value': '3'}
		],
		values=['1', '2'],
		labelStyle={'display': 'inline-block'}),
	html.Div(dcc.Input(id='input-box', type='text')),
	html.Button('Submit', id='button'),
	html.Div(id='output-container-button',
			 children='Enter a value and press submit')	
])

######################################################################
# Interactive part
######################################################################

# for the button
@app.callback(
	dash.dependencies.Output('output-container-button', 'children'),
	[dash.dependencies.Input('button', 'n_clicks')],
	[dash.dependencies.State('input-box', 'value')])
def update_button(n_clicks, value):
	return 'The input value was "{}" and the button has been clicked {} time(s)'.format(
		value, n_clicks)

######################################################################
# For nicer text
######################################################################

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

######################################################################
# Run the app locally
######################################################################

if __name__ == '__main__':
	app.run_server(debug=True)