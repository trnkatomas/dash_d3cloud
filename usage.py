from collections import Counter
import re

import dash_d3cloud
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True


def prepare_input(text_data):
    tokens = re.split("\W+", text_data)
    tokens_with_counts = Counter(tokens)
    return tokens_with_counts

with open('constitution.txt') as text_source_file:
    text = text_source_file.read()
    token_with_counts = prepare_input(text)

def word_for_wordclouds(n, data=token_with_counts):
    tokens_wordcloud = [{"text": a, "value":b} for a, b in data.most_common(n)]
    return tokens_wordcloud

app.layout = html.Div([
    dcc.Input(id="count", value=100, type="number"),
    dcc.RadioItems(id="choice",  options=[
        {'label': 'predefined', 'value': 'constitution'},
        {'label': 'custom input', 'value': 'input'},
    ],
    value='constitution'),
    dcc.Textarea(
        id="custom_input",
        placeholder='Enter a value...',
        value='This is a TextArea component',
        style={'width': '100%'}
    ),
    dash_d3cloud.WordCloud(
        id='wordcloud',
        words=word_for_wordclouds(100)
    )
])

@app.callback(Output('wordcloud', 'words'),
             [Input('count', 'value'),
              Input('custom_input', 'value'),
              Input('choice', 'value')])
def display_output(count, custom_input, choice):
    if choice == "constitution":
        return word_for_wordclouds(count)
    elif choice == "input":
        text_data = prepare_input(custom_input)
        return word_for_wordclouds(count, text_data)
    else:
        return Counter({"text": "empty", "value": 1})

if __name__ == '__main__':
    app.run_server(debug=True)
