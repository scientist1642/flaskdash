"""Instantiate a Dash app."""

import dash
from flask import Flask
from dash import  dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = [
    "https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"
]
external_scripts = [
    "https://code.jquery.com/jquery-3.3.1.slim.min.js",
    "https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.bundle.min.js",
]


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    app = dash.Dash(
        "dash_tutorial",
        server=server,
        routes_pathname_prefix="/dashapp/",
        external_stylesheets=external_stylesheets,
        external_scripts=external_scripts,
    )

    # Custom HTML layout
    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv"
    )

    app.scripts.config.serve_locally = False
    dcc._js_dist[0]["external_url"] = "https://cdn.plot.ly/plotly-basic-latest.min.js"

    app.layout = html.Div(
        [
            html.H1("Stock Tickers"),
            dcc.Dropdown(
                id="my-dropdown",
                options=[
                    {"label": "Tesla", "value": "TSLA"},
                    {"label": "Apple", "value": "AAPL"},
                    {"label": "Coke", "value": "COKE"},
                ],
                value="TSLA",
            ),
            dcc.Graph(id="my-graph"),
        ],
        className="container",
    )

    @server.route("/")
    @app.callback(Output("my-graph", "figure"), [Input("my-dropdown", "value")])
    def update_graph(selected_dropdown_value):
        dff = df[df["Stock"] == selected_dropdown_value]
        return {
            "data": [
                {"x": dff.Date, "y": dff.Close, "line": {"width": 3, "shape": "spline"}}
            ],
            "layout": {"margin": {"l": 30, "r": 20, "b": 30, "t": 20}},
        }

    return server