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

            This Web app is an assignment from Lambda School's Data Science program. The assignment asked to predict something given a dataset.

            In my case, I chose to predict video game sales.

            ### The Dataset

            In order to predict anything in data science, you need features - that is, ways we can influence the prediction. For instance, game genre is a feature because that could possibly impact game sales. As such, I needed a decent dataset with enough features.

            I found the needed dataset from this [Reddit post](https://old.reddit.com/r/datasets/comments/bco2rd/video_games_sales_2019_dataset/), which linked to it on Kaggle, a dataset-sharing website. The dataset contained over 50,000 video games, with game sales and relevant characteristics like genre, ESRB Rating, and critic scores.

            ### Cleaning the Dataset

            I loaded the dataset with Pandas, a python library that handles datasets. Here's a sample output of the dataset:
            """
        ),

        html.Img(src='assets/InitialDataset.png', className='img-fluid'),

        dcc.Markdown(
            """
            As you can see, there's a lot of data here, and some are irrelevant and/or need cleaning. For instance, `basename` is pretty much the same as `Name`. And while we have game sales, some are expressed in the column `Total_Shipped`, while others divide sales into various regions (`NA_Sales`, `EU_Sales`, `JP_Sales`).

            With some python magic, I removed completely irrelevant columns and merged total game sales in a single column. I also created a new column that said if the game sold over 100,000 copies and another column that averaged the critic and user scores (a form of feature engineering). In addition, I had to remove ~30,000 games from the list because they didn't have any game sales listed.

            ### Regression vs Classification

            You may be wondering, why predict if a game will sell over 100,000 copies instead of specifically saying how many copies the game will sell?

            To explain, have a look at this histogram:
            """
            ),

            html.Img(src='assets/SalesHistogram.png', className='img-fluid'),
            
            dcc.Markdown(
            """
            This dataset has many outliers. Many games don't sell 100,000 copies, and there are a few that sell tens of millions of copies. If I tried predicting exact game sales with mathematical models, it's very likely some predictions will shoot way higher than they should due to the extreme outliers.

            That's why I chose to go for a yes or no question (will the game sell 100k+). That way, I won't ever need to consider exact game sales in the model, and the results are more focused and less out of hand. In data science, this kind of question is a classification, while the former would be a regression.

            ### Making the Predictions

            With the dataset cleaned, it was time to decide which features to use for the prediction.

            Usually in data science, the more features, the better. But since this is a Web app, I needed to condense the features so the user wouldn't get overwhelmed. For instance, instead of having dropdowns for the critic, user, and vgchartz scores, there's just one dropdown for the averaged score.

            In the end, I chose the seven features you see in the predictions page. As for the prediction model, I chose the random forest classifier because it led to the highest accuracy score. I explain how accuracy scores work in the Insights page.
            """
        ),

    ],
)

layout = dbc.Row([column1])