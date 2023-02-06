from dash import html, dcc, no_update
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
import plotly.express as px

from assets.components.restaurant_card import get_card, get_row, get_grid, get_cards
from assets.restaurant_metadata import get_restaurants_by_name
# from search.search import search_restaurants


def search_result_layout(pathname):
    # SEMANTIC SEARCH COULD NOT BE IMPLEMENTED PROPERLY IN TIME :C
    # search_query = pathname[9:].replace('+', ' ')
    # search_results = search_restaurants(search_query)
    # print(search_results)
    # restaurants = get_restaurants_by_name(search_results)
    # for restaurant in restaurants:
    #     print(restaurant.name)
    return dbc.Container([
        dbc.Row([
            html.H2('Search results'),
            html.Div(f'Showing results for "{pathname[9:]}"...'),
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    get_grid(16)
                ])
            ], width=10),
            dbc.Col([
                html.Div('Only show restaurants with the following tags:'),
                dcc.Dropdown(
                    ['Japanese', 'Chinese', 'Halal', 'Local'],
                    [],
                    multi=True,
                )
            ], width=2, style={'overflow-y':'hidden'})
        ])
    ], style={'margin-top': '20px', 'margin-bottom':'20px', 'margin-left': '50px', 'margin-right':'50px'})
