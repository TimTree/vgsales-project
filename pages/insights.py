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
        
            ## Insights

            ### Accuracy Score

            How good are the Web app's predictions? Are you better off completely guessing if a game will sell over 100,000 copies?

            In the dataset, 63.6% of games sold over 100,000 copies. That's the **mean baseline**: you have a 63.6% chance of predicting correctly if you guessed that every game sells 100k.

            So for this project to be worth something, it needs to correctly guess sales more than 63.6% of the time. To find out, I split the dataset of ~20,000 games into two sets: a training set with ~16,000 games and a validation set with ~4,000 games.

            I use the training set to create the Web app's prediction model. I then validate how good the generated prediction model is with the validation set. How many times out of 4,000 does the prediction model make the correct guess? That's the accuracy score.

            Thankfully, the accuracy score was **77.8%**, well above 63.6%. So you'll be pleased to know these predictions aren't a pile of BS (yes, I went there).

            ### Feature Weights

            This Web app lets you toggle seven different features - that is, seven different ways to affect the prediction. But which of the seven predictions most influence the prediction?

            In Data Science, we can find this out through a permutation importance table. The higher the feature, the bigger influence it has on video game sales.
            """
            ),

            html.Img(src='assets/PermutationImportance.png', className='img-fluid'),

            dcc.Markdown(
            """

            As shown, the number of games the publisher of the given game has published, the year released, and platform play the biggest role in selling 100,000 copies. Thankfully genre is low on the list, so feel free to develop different types of games without worrying about sales!

            ### Partial Dependence Plots

            We now know which features influence the prediction the most, but by how much and in which direction? That's where partial dependence plots come in.
            """
            ),

            html.Img(src='assets/PDPYear.png', className='img-fluid'),

            dcc.Markdown(
            """

            Between 2000 to 2005, game sales on average drop. They rebound up to 2012 then drop a bit again.
            """
            ),

            html.Img(src='assets/PDPScore.png', className='img-fluid'),

            dcc.Markdown(
            """

            The higher review score a game gets, the more likely that game will sell 100k up to around 8/10 where it plateaus.
            """
            ),

            html.Img(src='assets/PDP_Publisher.png', className='img-fluid'),

            dcc.Markdown(
            """

            Publishing a game with a publisher with many released games considerably increases the likelihood of selling 100k copies, which makes sense since these publishers have more visibility. Such publishers include EA, Activision, and Nintendo.








            ### The Early Childhood Dilemma

            If you scratched your head wondering why changing the ESRB rating to EC (Early Childhood) doesn't lower the probability too much, you're not alone. EC games are obscure and don't sell well, right?

            Well, it's true that EC games rarely hit the top charts, but **this Web app simply predicts if a game will sell 100,000 copies**. So while you'll almost never see an EC game sell in the millions, they still do a decent job at selling 100,000 copies.



            """
        ),
    ],
    md=12,
)


column2 = dbc.Col(
    [
        
    ]
)

layout = dbc.Row([column1, column2])