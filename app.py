from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# 1. Load data
df = pd.read_csv("formatted_sales_data.csv")
df = df.sort_values(by="date")

# 2. Layout with Styling
app.layout = html.Div(style={
    'backgroundColor': '#f9f9f9', 
    'padding': '40px', 
    'fontFamily': 'sans-serif'
}, children=[
    
    html.H1(
        "Pink Morsel Sales Visualiser",
        style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}
    ),

    html.Div(style={'textAlign': 'center', 'marginBottom': '20px'}, children=[
        html.Label("Filter by Region:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"},
            ],
            value="all", # Default value
            inline=True,
            style={'display': 'inline-block'}
        ),
    ]),

    dcc.Graph(id="sales-graph")
])

# 3. Callback to handle the Filtering logic
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(region):
    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == region]

    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        title=f"Pink Morsel Sales - {region.title()} Region",
        template="plotly_white"
    )
    
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run(debug=True)