from dash import Dash, html

app = Dash(__name__)
server = app.server

app.layout = [
    html.H1('Welcome in Dash public repo!'),
    html.Div('Test version 0.1')
]

if __name__ == '__main__':
    app.run(debug=True)
