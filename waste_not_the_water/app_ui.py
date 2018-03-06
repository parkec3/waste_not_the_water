import dash
import dash_core_components as dcc
import dash_html_components as html

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

if __name__ == '__main__':
    app.run_server(debug=False)