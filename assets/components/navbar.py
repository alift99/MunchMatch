from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app

def get_navbar():
    logo = dbc.Col([
        html.Img(
            src='assets/images/munchmatch_logo.jpeg', 
            width=176, 
            height=36, 
            style={
                'margin-top': '10px',
                'margin-bottom': '10px', 
                'margin-left': '10px',
                'margin-right':'10px'
            }
        ),
    ], width=2)
    search_bar = dbc.Col(
        dbc.InputGroup(
            [
                dbc.Input(placeholder="e.g. An aesthetic cafe with Korean cuisine and good dessert", type="search", id='search-input'),
                dbc.Button(
                    html.I(className='fas fa-search'),
                    id="search-button",
                    style={'background-color':"#FF8A01", 'color':'white', 'border':'1px solid #FF8A01'}
                ),
            ]
        ),
        width=8,
        align="center"
    )
    navbar = dbc.Navbar(
        [
            logo,
            search_bar
        ],
        color="white",
        light=True,
        sticky="top",
    )
    return navbar

@app.callback(
    Output('url', 'pathname'),
    [Input('search-button', 'n_clicks')],
    [State('search-input', 'value')]
)
def update_output(n_clicks, search_query):
    if n_clicks:
        search_query = search_query.replace(' ', '+')
        return f'/results/{search_query}'