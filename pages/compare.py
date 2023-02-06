from dash import html, dcc, no_update
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
import plotly.express as px

from assets.components.restaurant_card import get_stars, get_column, get_grid
from assets.restaurant_metadata import RestaurantMetadata, DATABASE, get_restaurants_by_name


def get_restaurant_desc(pathname):
    if len(pathname[9:].split('/')) > 1:
        restaurant_names = pathname[9:].split('/')
        data1 = get_restaurants_by_name([restaurant_names[0].replace('%20', ' ')])[0]
        data2 = get_restaurants_by_name([restaurant_names[1].replace('%20', ' ')])[0]
        component2 = dbc.Col([
            html.Img(src=data2.img_link, height='270px', width='480px'),
            dbc.Row([
                dbc.Col([
                    html.H3(data2.name),
                ], width={"size": 9}),
                dbc.Col([
                    html.A('Change', href=pathname.rsplit('/', 1)[0])
                ], width={'size': 3})
            ]),
            dbc.Row([
                dbc.Col([
                    get_stars(data2.rating, data2.n_ratings)
                ], width=12)
            ]),
            html.Br(),
            dbc.Row([
                html.B('Location'),
                html.Div(data2.address)
            ]),
            html.Br(),
            dbc.Row([
                html.B('Price Range'),
                html.Div(data2.cost)
            ]),
            html.Br(),
            dbc.Row([
                html.B('Specialties'),
                html.Div([html.Span(specialty, style={
                                'background-color':'#ff8a01',
                                'margin':'5px',
                                'padding':'5px',
                                'color':'white',
                                'border-radius':'5px', 
                                'display':'inline-block'
                            }) for specialty in data2.sentiments])
            ]),
        ], width={"size": 4, 'offset': 1})
    else:
        restaurant_name = pathname[9:]
        data1 = get_restaurants_by_name([restaurant_name.replace('%20', ' ')])[0]
        component2 = get_column(5, pathname)
    # read route string
    # if only 1 restaurant name, second column is compare options
    # if two restaurant names, second column is another restaurant description
    return dbc.Container([
        html.Br(),
        dbc.Row([
            dbc.Col([
                html.Img(src=data1.img_link, height='270px', width='480px'),
                dbc.Row([
                    dbc.Col([
                        html.H3(data1.name),
                    ]),
                ]),
                dbc.Row([
                    dbc.Col([
                        get_stars(data1.rating, data1.n_ratings)
                    ], width=12)
                ]),
                html.Br(),
                dbc.Row([
                    html.B('Location'),
                    html.Div(data1.address)
                ]),
                html.Br(),
                dbc.Row([
                    html.B('Price Range'),
                    html.Div(data1.cost)
                ]),
                html.Br(),
                dbc.Row([
                    html.B('Specialties'),
                    html.Div([html.Span(specialty, style={
                                    'background-color':'#ff8a01',
                                    'margin':'5px',
                                    'padding':'5px',
                                    'color':'white',
                                    'border-radius':'5px', 
                                    'display':'inline-block'
                                }) for specialty in data1.sentiments])
                ])
            ], width={"size": 4, 'offset': 1}),
            component2
        ])
    ])
