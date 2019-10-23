import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            **Warning: Technical jargon ahead!**

            This Web app is an assignment from Lambda School's Data Science program. The assignment asked to predict something given a dataset.

            In my case, I chose to predict video game sales.

            ### The Dataset

            In order to predict anything in data science, you typically need a math function. A function takes in inputs to generate an output.

            Recall this math function from Algebra:

            `y=2x+w`

            Here, the inputs are `x` and `w`. When we give `x` and `w` values, the function can provide the output `y`. `y` can change if we change `x` and `w`.

            For this project, the inputs are various game characteristics (game genre, year released, etc) and the output is whether or not the game will sell over 100,000 copies. If one released an action game instead of an adventure game, would that impact game sales?

            I found the needed dataset from this [Reddit post](https://old.reddit.com/r/datasets/comments/bco2rd/video_games_sales_2019_dataset/), which linked to it on Kaggle, a dataset-sharing website. The dataset contained over 55,000 video games, with game sales and relevant characteristics.

            ### Cleaning the Dataset

            I loaded the dataset with Pandas, a python library that handles datasets. Here's a sample output of the dataset:

            (img)

            As you can see, there's a lot of data here, and some are irrelevant and/or need cleaning. For instance, the `Status` column only has 1's and seems pointless. And while we have game sales, some are expressed in the column `Total_Shipped`, while others divide sales into various regions (`NA_Sales`, `EU_Sales`, `JP_Sales`).

            With some python magic, I removed completely irrelevant columns and merged total game sales in a single column. I also created a new column that said if the game sold over 100,000 copies and another column that averaged the critic and user scores (a form of feature engineering).

            ### Regression vs Classification

            You may be wondering, why predict if a game will sell over 100,000 copies instead of specifically saying how many copies the game will sell?

            To explain, have a look at this histogram:

            (img)

            This dataset has many outliers. Many games don't sell 100,000 copies, and there are a few that sell tens of millions of copies. If I tried predicting exact game sales with mathematical models, it's very likely some predictions will shoot way higher than they should due to the extreme outliers.

            That's why I chose to go for a yes or no question (will the game sell 100k+). That way, I won't ever need to consider exact game sales in the model, and the results are more focused and less out of hand. In data science, this kind of question is a classification, while the former would be a regression.

            ### Making the Predictions

            With the dataset cleaned, it was time to decide which inputs (features) to use for the prediction.

            Usually in data science, the more inputs, the better. But since this is a Web app, I'd rather not have the user get overwhelmed with too many input boxes. As such, 

            """
        ),

    ],
)

layout = dbc.Row([column1])