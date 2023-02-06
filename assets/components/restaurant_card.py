from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

from assets.restaurant_metadata import RestaurantMetadata, DATABASE


CARD_STYLE = {
    'margin-top': '10px',
    'margin-bottom': '10px', 
    # "width": "18rem",
}

def get_stars(rating, n_ratings):
    stars = []
    stars.append(html.Span("{:.1f}".format(rating) + ' '))
    for i in range(5):
        if i + 1 <= rating:
            stars.append(html.I(className='fa-solid fa-star', style={'color':'#ff8a01'}))
        else:
            stars.append(html.I(className='fa-regular fa-star', style={'color':'#ff8a01'}))
    stars.append(html.Span(f' ({n_ratings})'))
    return html.Div(stars)

def get_card(data):
    return dbc.Card(
    [
        dbc.CardImg(src=data.img_link, top=True, style={'height': '180px'}),
        dbc.CardBody(
            [
                dbc.Row([
                    html.H4(
                        html.A(
                            data.name, href='/compare/' + data.name, className="card-title", style={'color': 'black'}
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col([
                        get_stars(data.rating, data.n_ratings)
                    ], width=12)
                ], className='d-flex justify-content-between'),
                dbc.Row([
                    html.Div(str(data.cuisine) + ' | ' + str(data.cost))
                ]),
                dbc.Row(
                    html.Div(
                        [
                            html.Span(
                                sentiment, 
                                style={
                                    'background-color':'#ff8a01',
                                    'margin':'5px',
                                    'padding':'5px',
                                    'color':'white',
                                    'border-radius':'5px', 
                                    'display':'inline-block'
                                }
                            ) 
                            for sentiment in data.sentiments
                        ],
                    ), 
                    style={'margin-top':'10px'}
                )
            ]
        ),
    ],
    style=CARD_STYLE
)

def get_card_x(data, pathname):
    return dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(
                            src=data.img_link,
                            className="img-fluid rounded-start",
                        ),
                        className="col-md-4",
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [
                                html.H4(
                                    html.A(
                                        data.name, href=pathname + '/' + data.name, className="card-title", style={'color': 'black'}
                                    )
                                ),
                                get_stars(data.rating, data.n_ratings),
                                html.Div(
                                    [
                                        html.Span(
                                            sentiment, 
                                            style={
                                                'background-color':'#ff8a01',
                                                'margin':'5px',
                                                'padding':'5px',
                                                'color':'white',
                                                'border-radius':'5px', 
                                                'display':'inline-block'
                                            }
                                        ) 
                                        for sentiment in data.sentiments
                                    ],
                                ), 
                            ]
                        ),
                        className="col-md-8",
                    ),
                ],
                className="g-0 d-flex align-items-center",
            )
        ],
        className="mb-3",
        style={"maxWidth": "540px"},
    )

def get_grid(n_restaurants):
    sample = DATABASE.sample(n_restaurants).to_dict('records')
    metadata = [RestaurantMetadata(**restaurant) for restaurant in sample]
    n_rows = n_restaurants // 4
    return html.Div([
        dbc.Row(
            [dbc.Col(get_card(metadata[r*4 + c])) for c in range(4)]
        ) for r in range(n_rows)
    ])

def get_cards(metadata):
    n_rows = len(metadata) // 4
    return html.Div([
        dbc.Row(
            [dbc.Col(get_card(metadata[r*4 + c])) for c in range(4)]
        ) for r in range(n_rows)
    ])

def get_row(n_restaurants):
    sample = DATABASE.sample(n_restaurants).to_dict('records')
    sample = [RestaurantMetadata(**restaurant) for restaurant in sample]
    card_row = dbc.Row(
        [
            dbc.Col(get_card(restaurant)) for restaurant in sample
        ],
        style={'max-width':'100%', 'max-height': '200px', 'overflow-x':'scroll'},
    )
    return card_row

def get_column(n_restaurants, pathname):
    sample = DATABASE.sample(n_restaurants).to_dict('records')
    sample = [RestaurantMetadata(**restaurant) for restaurant in sample]
    card_col = dbc.Col(
        [get_card_x(restaurant, pathname) for restaurant in sample],
        width={"size": 4, 'offset': 1}
    )
    return card_col