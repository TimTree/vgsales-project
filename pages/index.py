import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## What games become hits?

            Predict how likely a commercial video game will sell over 100,000 copies. Data inferred from a [VGChartz dataset](https://www.kaggle.com/ashaheedq/video-games-sales-2019).

            **Note:** All predictions are just for fun. Try not to take them seriously.

            """
        ),
        dcc.Link(dbc.Button('Let\'s Predict!', color='primary'), href='/predictions')
    ],
    md=6,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/MaxPixelGameController.jpg', className='img-fluid'),
        html.Span('Image taken from Max Pixel, Creative Commons CC0')
    ]
)

layout = dbc.Row([column1, column2])