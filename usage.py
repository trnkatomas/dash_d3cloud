from collections import Counter
import re

import dash_d3cloud
import dash
from dash.dependencies import Input, Output

if dash.__version__.startswith("2."):
    from dash import dcc
    from dash import html
else:
    import dash_html_components as html
    import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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

app.layout = html.Div(children=[
        html.H2(children="""Showcase of the d3-cloud wrapped as Dash component"""),
        dcc.Markdown("""For further reference look at the original page of the [d3-cloud](https://www.jasondavies.com/wordcloud/)
        """),
        html.Div(children=["""Choose the input (predefined, i.e. constitution) or custom input""",
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
        ]),
        html.Span(children=["Count of most occuring words: ", dcc.Input(id="count", value=100, type="number")]),        
        html.Div(children=[html.Div(children=["Scale: ",
            dcc.RadioItems(id="scale",  options=[
                {'label': '√n', 'value': 'sqrt'},
                {'label': 'n', 'value': 'linear'},
                {'label': 'log n', 'value': 'log'},
            ],
            value='sqrt', style={'display':'inline-flex'})], style={'width':'49%'}),
            html.Div(children=["Spiral",
            dcc.RadioItems(id="spiral",  options=[
                {'label': 'archimedean', 'value': 'archimedean'},
                {'label': 'rectangular', 'value': 'rectangular'},
            ],
            value='archimedean', style={'display':'inline-flex'})], style={'width':'49%'}),
        ]),
        html.Span(children=[
            "Orientations: ",
            dcc.Input(id="n-rotations", value=2, type="number"),
            "From: ",
            dcc.Input(id="rotations-from", value=-60, type="number"),
            "° To: ",
            dcc.Input(id="rotations-to", value=60, type="number"),
            "°"
        ]),
        dash_d3cloud.WordCloud(
            id='wordcloud',
            words=word_for_wordclouds(100),
            options={},
        )            
])

@app.callback([Output('wordcloud', 'words'),Output('wordcloud', 'options')],    
             [Input('count', 'value'),
              Input('custom_input', 'value'),
              Input('choice', 'value'),
              Input('spiral', 'value'),
              Input('scale', 'value'),
              Input('n-rotations', 'value'),
              Input('rotations-from', 'value'),
              Input('rotations-to', 'value')])
def display_output(count, custom_input, choice, spiral, scale, n_rotations, rotations_from, rotations_to):
    if choice == "constitution":
        text = word_for_wordclouds(count)
    elif choice == "input":
        text_data = prepare_input(custom_input)
        text = word_for_wordclouds(count, text_data)
    else:
        text = Counter({"text": "empty", "value": 1})

    options = {'spiral': spiral,
                'scale': scale,
                'rotations': n_rotations,
                'rotationAngles': [rotations_from, rotations_to]
                }
    return text, options

if __name__ == '__main__':
    app.run_server(debug=True)
