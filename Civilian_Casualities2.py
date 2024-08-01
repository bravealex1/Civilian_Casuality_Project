# Import necessary libraries
import pandas as pd  # For data manipulation
import dash  # For creating the web app
from dash import dcc, html  # For core components and HTML components
from dash.dependencies import Input, Output  # For linking components with callbacks
import plotly.graph_objs as go  # For complex visualizations
import plotly.express as px  # For easy-to-use plotting
import speech_recognition as sr  # For speech recognition

# Load and clean the dataset
def load_data():
    df = pd.read_csv("C:\\Users\\Owner\\OneDrive\\Desktop\\Autogen_Project\\WarConflicts.csv")  # Read CSV file
    df['country'] = df['country'].astype(str)  # Ensure country column is of string type
    df = df.dropna()  # Drop rows with missing values
    return df  # Return cleaned dataframe

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Yearly Statistics for Nations in Conflicts"  # Set the title of the web app

# Load data
df = load_data()

# Get unique countries and years from the dataset
countries = list(df['country'].unique())  # List of unique countries
years = sorted(df['year'].unique())  # Sorted list of unique years

# Define the layout of the app
app.layout = html.Div([
    # App title
    html.H1("Yearly Statistics for Nations in Conflicts"),
    
    # Dropdown for selecting a country
    html.Div([
        html.Label("Select a country"),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': 'All Countries', 'value': 'All Countries'}] + [{'label': country, 'value': country} for country in countries],
            value='All Countries'  # Default value
        )
    ]),
    
    # Dropdown for selecting a year
    html.Div([
        html.Label("Select a Year"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': 'All Years', 'value': 'All Years'}] + [{'label': str(year), 'value': str(year)} for year in years],
            value='All Years'  # Default value
        )
    ]),
    
    # Section 1: Counts of Conflicts by Year
    html.Div([
        html.H2("Counts of Conflicts by Year"),
        dcc.Graph(id='counts-by-year')
    ]),
    
    # Section 2: Counts of Conflicts for Selected Year
    html.Div([
        html.H2("Counts of Conflicts for Selected Year"),
        dcc.Graph(id='counts-by-conflict')
    ]),
    
    # Section 3: Total Deaths by Type of Violence
    html.Div([
        html.H2("Total Deaths and Types of Violence"),
        dcc.Graph(id='deaths-by-type')
    ]),
    
    # Section 4: Total Deaths for Conflicts
    html.Div([
        html.H2("Total Deaths for Conflicts"),
        dcc.Graph(id='deaths-by-conflict')
    ]),
    
    # Section 5: Types of Death per Region
    html.Div([
        html.H2("Types of Death per Region"),
        dcc.Graph(id='deaths-by-region')
    ]),
    
    # Section 6: Types of Death per Country (Map Visualization)
    html.Div([
        html.H2("Types of Death per Country (Map Visualization)"),
        dcc.RadioItems(
            id='death-type-radio',
            options=[
                {'label': 'All Sides', 'value': 'All Sides'},
                {'label': 'Side A Deaths', 'value': 'deaths_a'},
                {'label': 'Side B Deaths', 'value': 'deaths_b'},
                {'label': 'Unknown Deaths', 'value': 'deaths_unknown'},
                {'label': 'Civilians Deaths', 'value': 'deaths_civilians'}
            ],
            value='All Sides'  # Default value
        ),
        dcc.Graph(id='deaths-by-country-map')
    ])
])

# Callback to update graphs based on selected country and year
@app.callback(
    [Output('counts-by-year', 'figure'),
     Output('counts-by-conflict', 'figure'),
     Output('deaths-by-type', 'figure'),
     Output('deaths-by-conflict', 'figure'),
     Output('deaths-by-region', 'figure'),
     Output('deaths-by-country-map', 'figure')],
    [Input('country-dropdown', 'value'),
     Input('year-dropdown', 'value'),
     Input('death-type-radio', 'value')]
)
def update_graphs(selected_country, selected_year, death_type):
    # Filter data based on selected country
    if selected_country == 'All Countries':
        df_country = df.copy()
    else:
        df_country = df[df['country'] == selected_country]
    
    # Filter data based on selected year
    if selected_year == 'All Years':
        df_filtered = df_country
    else:
        df_filtered = df_country[df_country['year'] == int(selected_year)]
    
    # Section 1: Counts of Conflicts by Year
    counts_by_year = df_country['year'].value_counts().sort_index()
    fig1 = go.Figure(data=[go.Bar(x=counts_by_year.index, y=counts_by_year.values)])
    fig1.update_layout(title="Counts of Conflicts by Year for " + selected_country)
    
    # Section 2: Counts of Conflicts for Selected Year
    counts_by_conflict = df_filtered['conflict_name'].value_counts().head(15)
    fig2 = px.bar(counts_by_conflict, x=counts_by_conflict.index, y=counts_by_conflict.values, title="Counts of Conflicts for Year " + selected_year)
    
    # Section 3: Total Deaths by Type of Violence
    deaths_by_type = df_filtered.groupby('type_of_violence')['deaths_total'].sum().reset_index()
    fig3 = go.Figure(data=[go.Bar(x=deaths_by_type['type_of_violence'], y=deaths_by_type['deaths_total'])])
    fig3.update_layout(title="Total Deaths by Type of Violence in " + selected_country + " for " + selected_year)
    
    # Section 4: Total Deaths for Conflicts
    deaths_by_conflict = df_filtered.groupby('conflict_name')['deaths_total'].sum().sort_values(ascending=False).head(20)
    fig4 = go.Figure(data=[go.Bar(x=deaths_by_conflict.index, y=deaths_by_conflict.values)])
    fig4.update_layout(title="Total Deaths for Conflicts in " + selected_country + " for " + selected_year)
    
    # Section 5: Types of Death per Region
    deaths_by_region = df_filtered.groupby('region')[['deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown']].sum().reset_index()
    fig5 = go.Figure()
    fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_unknown'], name='Unknown Deaths'))
    fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_a'], name='Side A Deaths'))
    fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_b'], name='Side B Deaths'))
    fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_civilians'], name='Civilians Deaths', marker=dict(color='red')))
    fig5.update_layout(title='Count of Deaths per Region in ' + selected_country + ' for ' + selected_year, barmode='stack')
    
    # Section 6: Types of Death per Country (Map Visualization)
    if death_type == 'All Sides':
        deaths_by_country = df_filtered.groupby(['country', 'ISO_Code'])['deaths_total'].sum().reset_index()
        z_values = deaths_by_country['deaths_total']
    else:
        deaths_by_country = df_filtered.groupby(['country', 'ISO_Code'])[death_type].sum().reset_index()
        z_values = deaths_by_country[death_type]
    
    fig6 = go.Figure(data=go.Choropleth(
        locations=deaths_by_country['ISO_Code'],
        z=z_values,
        text=deaths_by_country['country'],
        colorscale=[[0, 'green'], [1, 'red']],
        autocolorscale=False,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title='Deaths'
    ))
    fig6.update_layout(title='Types of Death per Country')
    
    return fig1, fig2, fig3, fig4, fig5, fig6

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
