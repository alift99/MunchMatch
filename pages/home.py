from dash import html, dcc, no_update
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
import plotly.express as px

from assets.components.restaurant_card import get_card, get_row, get_grid


home_layout = dbc.Container([
    html.Br(),
    html.H2('Trending'),
    get_grid(8),
    html.Br(),
    html.H2('Fine Dining'),
    get_grid(8),
    html.Br(),
    html.H2('Local Cuisine'),
    get_grid(8),
])