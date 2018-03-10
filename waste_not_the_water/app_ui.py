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

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
	dcc.Location(id='url', refresh=False),
	html.Div(id='page-content')	
])

######################################################################
# Home page
######################################################################

markdown_text = '''
### waste_not_the_water

waste_not_the_water utilizes the open [Urban Waste Water Treatment database](https://www.eea.europa.eu/data-and-maps/data/waterbase-uwwtd-urban-waste-water-treatment-directive-5)
 from [the European Environment Agency](https://www.eea.europa.eu/).
'''

index_page = html.Div([
	dcc.Link('Go to Data Visualization', href='/data-vis'),
	hmtl.Br(),
	dcc.Link('Go to Machine Learning Model', href='/ml-model'),
	html.Br(),
	dcc.Markdown(children=markdown_text)
])

######################################################################
# Page 2: Data Visualization
######################################################################

data_vis_layout = html.Div([
	html.H1('Data Visualization'),
	html.Div(id='')
])

######################################################################
# Page 3: Machine Learning Model
######################################################################

######################################################################
# Interactive part
######################################################################

######################################################################
# For nicer text
######################################################################

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

######################################################################
# Run the app locally
######################################################################

if __name__ == '__main__':
	app.run_server(debug=True)