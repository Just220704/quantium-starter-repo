from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Initialize the Dash app
app = Dash(__name__)

# 1. Load and sort the data from Task 2
df = pd.read_csv("formatted_sales_data.csv")
df = df.sort_values(by="date")

# 2. Create the line chart with labels
fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)

# 3. Define the layout (Header + Graph)
app.layout = html.Div(style={'font-family': 'Arial'}, children=[
    html.H1(
        children='Pink Morsel Sales Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)