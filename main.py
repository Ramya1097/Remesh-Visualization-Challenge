# Twitter analytics showing relationship between user engagement, length of the tweet and hashtags.
# Developed by Ramya Malladi
# Date: 03/05/2021

# import dependencies
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import pandas as pd
import plotly.graph_objects as go

import requests
from dash.dependencies import Input, Output
import json

url = 'C:/Users/ramya/Desktop/twitter_data.json'

# initializing the dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
# load data using Python JSON module
with open(url, 'r') as f:
    data = json.loads(f.read())
# Flatten data
df_nested_list = pd.json_normalize(data)['users']
url = 'https://raw.githubusercontent.com/Remesh/tweet-data/master/data.json'
r = requests.get(url)
users = r.json()['users']
user_df = pd.DataFrame(users)

# the following block of code is to get a dataframe into place using the json data
table = pd.DataFrame(df_nested_list)
hashtags = r.json()['hashtags']
hash_df = pd.DataFrame(hashtags)
tweets = r.json()['tweets']
tweets_df = pd.DataFrame(tweets)
new = [user_df, tweets_df, hash_df]
new_df = pd.concat(new, axis=1)
new_df = new_df.fillna(value=0)
new_df = new_df.loc[:, ~new_df.columns.duplicated()]

length = []
for i in new_df['text']:
    length.append(len(i))

new_df.loc[:, 'Length'] = length
hash_length = []
list_likes = np.array(new_df['likes'])
new_list = []
for i in list_likes:
    a = np.sum(i)
    new_list.append(a)

new_df['likes_total'] = new_list
list_hash = np.array(new_df['hashtags'])
new_hash = []
print(new_df['hashtags'])
for i in list_hash:
    b = np.sum(i)
    new_hash.append(b)
new_df['hash_total'] = new_hash
# new_df is the final dataframe we will be working on

# initialize the start and end ranges to update our bar charts
start = 0
end = 300


# helper function to filter the data based on the ranges provided
def filter_dataframe(start, end):
    filtered = (new_df['Length'] > start) & (new_df['Length'] <= end)
    location = new_df.loc[filtered]
    return location


# callback function to display our bar charts
@app.callback(
    Output(component_id='like_chart', component_property='figure'),
    [Input(component_id='start_range', component_property='value'),
     Input(component_id='end_range', component_property='value')
     ]
)
def likes_graph(start, end):
    # dff is a copy generated from the main dataframe filtered the start and end ranges
    dff = filter_dataframe(start, end)

    # creating the subplots to compare likes and hashtags
    fig = make_subplots(rows=2, cols=1, vertical_spacing=0.25)
    fig.append_trace(go.Bar(x=dff['Length'], y=dff['likes_total'], name='Number of likes'), row=1, col=1)
    fig.append_trace(go.Bar(x=dff['Length'], y=dff['hash_total'], name='Number of hashtags'), row=2, col=1)
    fig.update_layout(title="Relationship between tweet length, likes and hashtags", height=500,title_x=0.5)
    fig.update_xaxes(title_text="Tweet length", row=1, col=1)
    fig.update_yaxes(title_text="Number of likes", row=1, col=1)
    fig.update_xaxes(title_text="Tweet Length", row=2, col=1)
    fig.update_yaxes(title_text="Number of hashtags", row=2, col=1)

    return fig


# creating the main layout of our dashboard
app.layout = html.Div([

    html.Div([
        html.H1("Twitter Analytics",
                style={"text-align": "center", "color": "black"}),
        html.H3("Welcome to the Twitter Dashboard",
                style={"text-align": "center", "color": "black"}),
        html.P(
            "Enter a starting and ending range to see the relationship between tweet length, hashtags and user "
            "engagement. "
            "I have considered the number of likes for a tweet as a metric for user engagement. "
            "Enter a larger range of numbers to get an high level visualization proving that length of the tweet and "
            "hashtags have a direct relationship to user engagement. "
            "You can also drill down into the visualization by changing the number range")

    ]),

    html.Div([

        html.H5("Enter starting range"),
        dcc.Input(id="start_range", type="number", min=0, max=300),
        html.H5("Enter an ending range"),
        dcc.Input(id="end_range", type="number", min=0, max=300),

        html.Div([
            dcc.Graph(id='like_chart')
        ])
    ])])

# running the application locally on port 8000.
# Port can be set manually if required.
# Dash applications generally run on 8050 but I tried and ran on 8000
if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
