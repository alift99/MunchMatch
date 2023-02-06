from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from pages import home, search_results, compare
from assets.components.navbar import get_navbar


app.layout = html.Div(children=[
    get_navbar(),
    dcc.Location(id="url", refresh=False),
    html.Div(id="output-div")
])


@app.callback(
    Output(component_id="output-div",component_property="children"),
    Input(component_id="url",component_property="pathname")
)
def update_output_div(pathname):
    if pathname[:8] == '/results':
        return search_results.search_result_layout(pathname)
    elif pathname[:8] == '/compare':
        return compare.get_restaurant_desc(pathname)
    else:
        return home.home_layout


if __name__ == "__main__":
    app.run_server(debug=True)