import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown('#### Game Genre'), 
        dcc.Dropdown(
            id='Genre', 
            options = [
                {'label': 'Action', 'value': 'Action'}, 
                {'label': 'Sports', 'value': 'Sports'}, 
                {'label': 'Misc', 'value': 'Misc'}, 
                {'label': 'Adventure', 'value': 'Adventure'}, 
                {'label': 'Role-Playing', 'value': 'Role-Playing'},
                {'label': 'Shooter', 'value': 'Shooter'}, 
                {'label': 'Racing', 'value': 'Racing'}, 
                {'label': 'Simulation', 'value': 'Simulation'}, 
                {'label': 'Platform', 'value': 'Platform'}, 
                {'label': 'Fighting', 'value': 'Fighting'}, 
                {'label': 'Strategy', 'value': 'Strategy'}, 
                {'label': 'Puzzle', 'value': 'Puzzle'}, 
                {'label': 'Action-Adventure', 'value': 'Action-Adventure'}, 
                {'label': 'Music', 'value': 'Music'}, 
                {'label': 'Visual Novel', 'value': 'Visual Novel'}, 
                {'label': 'MMO', 'value': 'MMO'}, 
                {'label': 'Party', 'value': 'Party'}, 
                {'label': 'Sandbox', 'value': 'Sandbox'}, 
                {'label': 'Education', 'value': 'Education'}, 
                {'label': 'Board Game', 'value': 'Board Game'},  
            ], 
            value = 'Action', 
            className='mb-5', 
        ), 
        dcc.Markdown('#### ESRB Rating'), 
        dcc.Dropdown(
            id='ESRB_Rating', 
            options = [
                {'label': 'EC', 'value': 'EC'}, 
                {'label': 'E', 'value': 'E'}, 
                {'label': 'E10', 'value': 'E10'}, 
                {'label': 'T', 'value': 'T'}, 
                {'label': 'M', 'value': 'M'},
                {'label': 'RP', 'value': 'RP'},  
            ], 
            value = 'E', 
            className='mb-5', 
        ),
                dcc.Markdown('#### Platform'), 
        dcc.Dropdown(
            id='Platform', 
            options = [
                {'label': 'DS', 'value': 'DS'}, 
                {'label': 'PS2', 'value': 'PS2'}, 
                {'label': 'PC', 'value': 'PC'}, 
                {'label': 'PS3', 'value': 'PS3'}, 
                {'label': 'Wii', 'value': 'Wii'},
                {'label': 'PS', 'value': 'PS'},  
                {'label': 'PS4', 'value': 'PS4'},  
                {'label': 'GBA', 'value': 'GBA'},  
                {'label': 'XB', 'value': 'XB'},  
                {'label': 'PSV', 'value': 'PSV'},  
                {'label': '3DS', 'value': '3DS'},  
                {'label': 'XOne', 'value': 'XOne'},  
                {'label': 'N64', 'value': 'N64'},  
                {'label': 'NS', 'value': 'NS'},  
                {'label': 'SNES', 'value': 'SNES'},  
                {'label': 'SAT', 'value': 'SAT'}, 
                {'label': 'WiiU', 'value': 'WiiU'},  
                {'label': '2600', 'value': '2600'},  
                {'label': 'NES', 'value': 'NES'},  
                {'label': 'GB', 'value': 'GB'},  
                {'label': 'DC', 'value': 'DC'},  
                {'label': 'GEN', 'value': 'GEN'},  
                {'label': 'NG', 'value': 'NG'},  
                {'label': 'PSN', 'value': 'PSN'},  
                {'label': 'GBC', 'value': 'GBC'}, 
                {'label': 'XBL', 'value': 'XBL'}, 
                {'label': 'WS', 'value': 'WS'}, 
                {'label': 'SCD', 'value': 'SCD'}, 
                {'label': 'Mob', 'value': 'Mob'}, 
                {'label': '3DO', 'value': '3DO'}, 
                {'label': 'VC', 'value': 'VC'}, 
                {'label': 'PCE', 'value': 'PCE'}, 
                {'label': 'Amig', 'value': 'Amig'}, 
                {'label': 'OSX', 'value': 'OSX'}, 
                {'label': 'WW', 'value': 'MWW'}, 
                {'label': 'GG', 'value': 'GG'}, 
                {'label': 'PCFX', 'value': 'PCFX'},
            ], 
            value = 'DS', 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Year Released'), 
        dcc.Slider(
            id='Year', 
            min=1970, 
            max=2030, 
            step=1, 
            value=2010, 
            marks={n: str(n) for n in range(1970,2031,10)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Average Score'), 
        dcc.Slider(
            id='Average_Score', 
            min=0, 
            max=10, 
            step=0.1, 
            value=8, 
            marks={n: str(n) for n in range(0,11,1)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Game Available on X Platforms (including this one)'), 
        dcc.Slider(
            id='Number_Platforms', 
            min=1, 
            max=9, 
            step=1, 
            value=1, 
            marks={n: str(n) for n in range(1,10,1)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Number of Games Publisher of this Game Published'), 
        dcc.Slider(
            id='Number_Games_From_Publisher', 
            min=1, 
            max=1000, 
            step=1, 
            value=1, 
            marks={n: str(n) for n in range(0,1001,100)}, 
            className='mb-5', 
        ), 
    ],
    md=6,
)

from joblib import load
pipeline = load('assets/pipeline.joblib')

column2 = dbc.Col(
    [
        html.H2('Will this game sell over 100k?', className='mb-5'), 
        html.Div(id='prediction-content', className='lead') 
    ]
)

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Genre', 'value'), Input('ESRB_Rating', 'value'),Input('Platform', 'value'),Input('Year', 'value'),Input('Average_Score', 'value'),Input('Number_Platforms', 'value'),Input('Number_Games_From_Publisher', 'value')],
)
def predict(genre, esrb_rating, platform, year, average_score, number_platforms, number_games_from_publisher):
    df = pd.DataFrame(
        columns=['Genre', 'ESRB_Rating','Platform','Year','Average_Score','Number_Platforms','Number_Games_From_Publisher'], 
        data=[[genre, esrb_rating, platform, year, average_score, number_platforms, number_games_from_publisher]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.0f}'
    #return f'{'aaa':.0f}'

layout = dbc.Row([column1, column2])