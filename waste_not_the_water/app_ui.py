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

text_style = dict(fontFamily='sans-serif', fontWeight=300)

markdown_text = '''
### waste_not_the_water

waste_not_the_water utilizes the open [Urban Waste Water Treatment database](https://www.eea.europa.eu/data-and-maps/data/waterbase-uwwtd-urban-waste-water-treatment-directive-5)
 from [the European Environment Agency](https://www.eea.europa.eu/).
'''

app.layout = html.Div([
	dcc.Markdown(children=markdown_text)
])

dcc.Input(
	placeholder='Enter a value...', type='text', value=''

)

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