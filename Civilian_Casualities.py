# import numpy as np
# import datetime
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import pandas as pd
# import plotly.graph_objs as go
# import plotly.express as px

# # Load the data from a CSV file using pandas
# # Convert the 'country' column to string type for consistency
# # Get a sorted list of unique years from the 'year' column
# # Remove any rows with missing values
# df = pd.read_csv("C:\\Users\\Owner\\OneDrive\\Desktop\\Autogen_Project\\data_2024.csv")
# df['country'] = df['country'].astype(str)
# sorted_years = sorted(df['year'].unique())
# df = df.dropna()

# # Initialize the Dash app
# app = dash.Dash(__name__)

# # Define the layout of the app
# app.layout = html.Div([
#     # Main container for the first section
#     html.Div([
#         # Header for the first section
#         html.H1("Yearly Statistics for Nations in Conflicts",
#                 style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
#         # Dropdown for selecting a country
#         html.Div([
#             html.Label("Select a country"),
#             dcc.Dropdown(
#                 id='country-drop',
#                 options=[{'label': 'All Countries', 'value': 'All Countries'}] + 
#                         [{'label': country, 'value': country} for country in df['country'].unique()],
#                 value='All Countries',
#                 placeholder='Select a country',
#                 style={'textAlign': 'left', 'width': '40%', 'padding': '3px', 'fontSize': '20px'}
#             )
#         ]),
#         # Container to display the output based on selected country
#         html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
#     ], style={'width': '60%', 'float': 'left'}),
    
#     # Main container for the second section
#     html.Div([
#         # Header for the second section
#         html.H2("Count of Conflicts for Selected Year",
#                 style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
#         # Dropdown for selecting a year
#         html.Div([
#             html.Label("Select A Year"),
#             dcc.Dropdown(
#                 id='year-drop',
#                 options=[{'label': 'All Years', 'value': 'All Years'}] + 
#                         [{'label': year, 'value': year} for year in sorted(df['year'].unique())],
#                 value='All Years',
#                 placeholder='Select a Year',
#                 style={'textAlign': 'left', 'width': '100%', 'padding': '3px', 'fontSize': '20px'})
#         ]),
#         # Container to display the output based on selected year
#         html.Div(id='output-container2', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '40%', 'float': 'right'}),
    
#     # Main container for the third section
#     html.Div([
#         # Header for the third section
#         html.H3("Total Deaths and Types of Violence for Selected Country",
#                 style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
#         # Container to display the output based on selected country and year
#         html.Div(id='output-container3', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '60%', 'float': 'left'}),
    
#     # Main container for the fourth section
#     html.Div([
#         # Header for the fourth section
#         html.H4("Total Deaths for Conflicts in Selected Country, Year",
#                 style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
#         # Container to display the output based on selected country and year
#         html.Div(id='output-container4', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '40%', 'float': 'right'}),
    
#     # Main container for the fifth section
#     html.Div([
#         # Header for the fifth section
#         html.H5("Types of Death per Region in Selected Country and Year",
#                 style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
#         # Container to display the output based on selected country and year
#         html.Div(id='output-container5', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '60%', 'float': 'left'}),
    
#     # Main container for the sixth section
#     html.Div([
#         # Header for the sixth section
#         html.H6("Types of Death per Country (Map Visualization)",
#                 style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
#         # Radio buttons for selecting the type of deaths to display
#         dcc.RadioItems(
#             id='deaths-type-radio',
#             options=[
#                 {'label': 'All Sides', 'value': 'All Sides'},
#                 {'label': 'Deaths Side A', 'value': 'deaths_a'},
#                 {'label': 'Deaths Side B', 'value': 'deaths_b'},
#                 {'label': 'Deaths Unknown', 'value': 'deaths_unknown'},
#                 {'label': 'Civilians Deaths', 'value': 'deaths_civilians'}
#             ],
#             value='All Sides',
#             labelStyle={'display': 'inline-block'}
#         ),
#         # Container to display the output based on selected country, year, and type of deaths
#         html.Div(id='output-container6', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '40%', 'float': 'left'})
# ], style={'display': 'flex', 'flexWrap': 'wrap'})

# # Callback to update the first section based on selected country
# @app.callback(
#     Output(component_id='output-container', component_property='children'),
#     Input(component_id='country-drop', component_property='value'))
# def update_country_container(selected_country):
#     # Filter the data based on the selected country
#     if selected_country == 'All Countries':
#         dfcountry = df.copy()
#     else:
#         dfcountry = df[df['country'] == selected_country]
    
#     # Count the number of conflicts per year for the selected country
#     dfcountry = dfcountry['year'].value_counts().to_frame().reset_index()
#     dfcountry.columns = ['Year', 'Count']
#     dfcountry = dfcountry.sort_values(by="Year")

#     # Create a bar chart to display the counts of conflicts by year
#     bar_fig = go.Figure()
#     bar_fig.add_trace(go.Bar(x=dfcountry['Year'], y=dfcountry['Count']))
#     bar_fig.update_layout(title="Counts of Conflicts by Year for " + selected_country)

#     R_chart1 = dcc.Graph(figure=bar_fig)
#     return [html.Div(className='chart-item', children=[R_chart1], style={'display': 'flex'})]

# # Callback to update the second section based on selected year
# @app.callback(
#     Output(component_id='output-container2', component_property='children'),
#     Input(component_id='year-drop', component_property='value'))
# def update_year_container(selected_year):
#     # Filter the data based on the selected year
#     if selected_year == 'All Years':
#         dfyear = df.copy()
#         dfyear = dfyear.sort_values(by='year')
#     else:
#         dfyear = df[df['year'] == selected_year]
#         dfyear = dfyear.sort_values(by='year')

#     # Count the number of conflicts per conflict name for the selected year
#     conflicts = dfyear['conflict_name'].value_counts().to_frame().reset_index()
#     conflicts.columns = ['conflict_name', 'count']
#     conflicts = conflicts.sort_values(by='count', ascending=False)
#     conflicts = conflicts.head(15)

#     # Create a bar chart to display the counts of conflicts for the selected year
#     R_chart2 = dcc.Graph(
#         figure=px.bar(conflicts, x='conflict_name', y='count',
#                       title="Counts of Conflicts for Year " + str(selected_year))
#     )
#     return [html.Div(className='chart-item', children=[R_chart2], style={'display': 'flex'})]

# # Callback to update the third section based on selected country and year
# @app.callback(
#     Output(component_id='output-container3', component_property='children'),
#     Input(component_id='country-drop', component_property='value'),
#     Input(component_id='year-drop', component_property='value'))
# def update_violence_container(selected_country, selected_year):
#     # Filter the data based on the selected country and year
#     if selected_year == 'All Years':
#         df_filtered = df[df['country'] == selected_country] if selected_country != 'All Countries' else df
#     else:
#         df_filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)] if selected_country != 'All Countries' else df[df['year'] == selected_year]

#     # Group the data by type of violence and sum the total deaths
#     tov = df_filtered.groupby('type_of_violence')['deaths_total'].sum().reset_index()

#     # Create a bar chart to display the total deaths by type of violence
#     bar3_fig = go.Figure()
#     bar3_fig.add_trace(go.Bar(x=tov['type_of_violence'], y=tov['deaths_total'], text=tov['deaths_total'], textposition='outside'))
#     bar3_fig.update_layout(barmode='stack', title='Types of Violence for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Type of Violence', yaxis_title='Total Deaths')

#     R_chart3 = dcc.Graph(figure=bar3_fig)
#     return [html.Div(className='chart-item', children=[R_chart3], style={'display': 'flex'})]

# # Callback to update the fourth section based on selected country and year
# @app.callback(
#     Output(component_id='output-container4', component_property='children'),
#     Input(component_id='country-drop', component_property='value'),
#     Input(component_id='year-drop', component_property='value'))
# def update_conflicts_container(selected_country, selected_year):
#     # Filter the data based on the selected country and year
#     if selected_year == 'All Years':
#         df_filtered = df[df['country'] == selected_country] if selected_country != 'All Countries' else df
#     else:
#         df_filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)] if selected_country != 'All Countries' else df[df['year'] == selected_year]

#     # Group the data by conflict name and sum the total deaths
#     dpc = df_filtered.groupby('conflict_name')['deaths_total'].sum().reset_index()
#     dpc = dpc.sort_values(by='deaths_total', ascending=False)
#     dpc = dpc.head(20)

#     # Create a bar chart to display the total deaths by conflict name
#     bar4_fig = go.Figure()
#     bar4_fig.add_trace(go.Bar(x=dpc['conflict_name'], y=dpc['deaths_total'], text=dpc['deaths_total'], textposition='outside'))
#     bar4_fig.update_layout(title='Count of Deaths for Conflicts for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Conflict Name', yaxis_title='Total Deaths')
    
#     R_chart4 = dcc.Graph(figure=bar4_fig)
#     return [html.Div(className='chart-item', children=[R_chart4], style={'display': 'flex'})]

# # Callback to update the fifth section based on selected country and year
# @app.callback(
#     Output(component_id='output-container5', component_property='children'),
#     Input(component_id='country-drop', component_property='value'),
#     Input(component_id='year-drop', component_property='value'))
# def update_region_container(selected_country, selected_year):
#     # Filter the data based on the selected country and year
#     if selected_year == 'All Years':
#         df_filtered = df[df['country'] == selected_country] if selected_country != 'All Countries' else df
#     else:
#         df_filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)] if selected_country != 'All Countries' else df[df['year'] == selected_year]

#     # Group the data by region and sum the deaths for each category
#     sides = df_filtered.groupby('region')[['deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown']].sum().reset_index()
#     sides = sides.sort_values(by='region')

#     # Create a bar chart to display the total deaths per region
#     bar5_fig = go.Figure()
#     bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_unknown'], name='Unknown Deaths', text=sides['deaths_unknown'], textposition='outside'))
#     bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_a'], name='Side A Deaths', text=sides['deaths_a'], textposition='outside'))
#     bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_b'], name='Side B Deaths', text=sides['deaths_b'], textposition='outside'))
#     bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_civilians'], name='Civilians Deaths', text=sides['deaths_civilians'], textposition='outside'))
#     bar5_fig.update_layout(title='Count of Deaths per Region for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Region', yaxis_title='Total Deaths')
    
#     R_chart5 = dcc.Graph(figure=bar5_fig)
#     return [html.Div(className='chart-item', children=[R_chart5], style={'display': 'flex'})]

# # Callback to update the sixth section based on selected country, year, and type of deaths
# @app.callback(
#     Output(component_id='output-container6', component_property='children'),
#     [
#         Input(component_id='country-drop', component_property='value'),
#         Input(component_id='year-drop', component_property='value'),
#         Input(component_id='deaths-type-radio', component_property='value')
#     ]
# )
# def update_map_container(selected_country, selected_year, selected_button):
#     # Filter the data based on the selected country and year
#     if selected_country == 'All Countries':
#         if selected_year == 'All Years':
#             df_filtered = df
#         else:
#             df_filtered = df[df['year'] == selected_year]
#     else:
#         if selected_year == 'All Years':
#             df_filtered = df[df['country'] == selected_country]
#         else:
#             df_filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)]

#     # Group the data by country and ISO code, and sum the deaths based on the selected button
#     if selected_button == 'All Sides':
#         sides = df_filtered.groupby(['country', 'ISO_Code'])['deaths_total'].sum().reset_index()
#         z_values = sides['deaths_total']
#     else:
#         sides = df_filtered.groupby(['country', 'ISO_Code'])[selected_button].sum().reset_index()
#         z_values = sides[selected_button]

#     # Create a choropleth map to display the deaths by country
#     map_fig = go.Figure(data=go.Choropleth(
#         locations=sides['ISO_Code'],
#         z=z_values,
#         text=sides['country'],
#         colorscale='Blues',
#         autocolorscale=False,
#         reversescale=True,
#         marker_line_color='darkgray',
#         marker_line_width=0.5,
#         colorbar_title='Value',
#     ))

#     R_chart6 = dcc.Graph(figure=map_fig)
#     return [html.Div(className='chart-item', children=[R_chart6], style={'display': 'flex'})]

# # Run the Dash app
# if __name__ == '__main__':
#     app.run_server(debug=True)


# import numpy as np
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import pandas as pd
# import plotly.graph_objs as go
# import plotly.express as px

# # Load the data from a CSV file using pandas
# # Convert the 'country' column to string type for consistency
# # Get a sorted list of unique years from the 'year' column
# # Remove any rows with missing values
# df = pd.read_csv("C:\\Users\\Owner\\OneDrive\\Desktop\\Autogen_Project\\data_2024.csv")
# df['country'] = df['country'].astype(str)
# sorted_years = sorted(df['year'].unique())
# df = df.dropna()

# # Initialize the Dash app
# app = dash.Dash(__name__)

# # Define the layout of the app
# app.layout = html.Div([
#     # Main container for the first section
#     html.Div([
#         # Header for the first section
#         html.H1("Yearly Statistics for Nations in Conflicts",
#                 style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
#         # Dropdown for selecting a country
#         html.Div([
#             html.Label("Select a country"),
#             dcc.Dropdown(
#                 id='country-drop',
#                 options=[{'label': 'All Countries', 'value': 'All Countries'}] + 
#                         [{'label': country, 'value': country} for country in df['country'].unique()],
#                 value='All Countries',
#                 placeholder='Select a country',
#                 style={'textAlign': 'left', 'width': '40%', 'padding': '3px', 'fontSize': '20px'}
#             )
#         ]),
#         # Container to display the output based on selected country
#         html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
#     ], style={'width': '60%', 'float': 'left'}),
    
#     # Main container for the second section
#     html.Div([
#         # Header for the second section
#         html.H2("Count of Conflicts for Selected Year",
#                 style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
#         # Dropdown for selecting a year
#         html.Div([
#             html.Label("Select A Year"),
#             dcc.Dropdown(
#                 id='year-drop',
#                 options=[{'label': 'All Years', 'value': 'All Years'}] + 
#                         [{'label': year, 'value': year} for year in sorted(df['year'].unique())],
#                 value='All Years',
#                 placeholder='Select a Year',
#                 style={'textAlign': 'left', 'width': '100%', 'padding': '3px', 'fontSize': '20px'})
#         ]),
#         # Container to display the output based on selected year
#         html.Div(id='output-container2', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '40%', 'float': 'right'}),
    
#     # Main container for the third section
#     html.Div([
#         # Header for the third section
#         html.H3("Total Deaths and Types of Violence for Selected Country",
#                 style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
#         # Container to display the output based on selected country and year
#         html.Div(id='output-container3', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '60%', 'float': 'left'}),
    
#     # Main container for the fourth section
#     html.Div([
#         # Header for the fourth section
#         html.H4("Total Deaths for Conflicts in Selected Country, Year",
#                 style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
#         # Container to display the output based on selected country and year
#         html.Div(id='output-container4', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '40%', 'float': 'right'}),
    
#     # Main container for the fifth section
#     html.Div([
#         # Header for the fifth section
#         html.H5("Types of Death per Region in Selected Country and Year",
#                 style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
#         # Container to display the output based on selected country and year
#         html.Div(id='output-container5', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '60%', 'float': 'left'}),
    
#     # Main container for the sixth section
#     html.Div([
#         # Header for the sixth section
#         html.H6("Types of Death per Country (Map Visualization)",
#                 style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
#         # Radio buttons for selecting the type of deaths to display
#         dcc.RadioItems(
#             id='deaths-type-radio',
#             options=[
#                 {'label': 'All Sides', 'value': 'All Sides'},
#                 {'label': 'Deaths Side A', 'value': 'deaths_a'},
#                 {'label': 'Deaths Side B', 'value': 'deaths_b'},
#                 {'label': 'Deaths Unknown', 'value': 'deaths_unknown'},
#                 {'label': 'Civilians Deaths', 'value': 'deaths_civilians'}
#             ],
#             value='All Sides',
#             labelStyle={'display': 'inline-block'}
#         ),
#         # Container to display the output based on selected country, year, and type of deaths
#         html.Div(id='output-container6', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '40%', 'float': 'left'})
# ], style={'display': 'flex', 'flexWrap': 'wrap'})

# # Callback to update the first section based on selected country
# @app.callback(
#     Output(component_id='output-container', component_property='children'),
#     Input(component_id='country-drop', component_property='value'))
# def update_country_container(selected_country):
#     print(f"Selected Country: {selected_country}")  # Debugging statement
#     try:
#         # Filter the data based on the selected country
#         if selected_country == 'All Countries':
#             dfcountry = df.copy()
#         else:
#             dfcountry = df[df['country'] == selected_country]

#         # Count the number of conflicts per year for the selected country
#         dfcountry = dfcountry['year'].value_counts().to_frame().reset_index()
#         dfcountry.columns = ['Year', 'Count']
#         dfcountry = dfcountry.sort_values(by="Year")

#         # Create a bar chart to display the counts of conflicts by year
#         bar_fig = go.Figure()
#         bar_fig.add_trace(go.Bar(x=dfcountry['Year'], y=dfcountry['Count']))
#         bar_fig.update_layout(title="Counts of Conflicts by Year for " + selected_country)

#         R_chart1 = dcc.Graph(figure=bar_fig)
#         return [html.Div(className='chart-item', children=[R_chart1], style={'display': 'flex'})]
#     except Exception as e:
#         print(f"Error in update_country_container: {e}")

# # Callback to update the second section based on selected year
# @app.callback(
#     Output(component_id='output-container2', component_property='children'),
#     Input(component_id='year-drop', component_property='value'))
# def update_year_container(selected_year):
#     print(f"Selected Year: {selected_year}")  # Debugging statement
#     try:
#         # Filter the data based on the selected year
#         if selected_year == 'All Years':
#             dfyear = df.copy()
#             dfyear = dfyear.sort_values(by='year')
#         else:
#             dfyear = df[df['year'] == selected_year]
#             dfyear = dfyear.sort_values(by='year')

#         # Count the number of conflicts per conflict name for the selected year
#         conflicts = dfyear['conflict_name'].value_counts().to_frame().reset_index()
#         conflicts.columns = ['conflict_name', 'count']
#         conflicts = conflicts.sort_values(by='count', ascending=False)
#         conflicts = conflicts.head(15)

#         # Create a bar chart to display the counts of conflicts for the selected year
#         R_chart2 = dcc.Graph(
#             figure=px.bar(conflicts, x='conflict_name', y='count',
#                           title="Counts of Conflicts for Year " + str(selected_year))
#         )
#         return [html.Div(className='chart-item', children=[R_chart2], style={'display': 'flex'})]
#     except Exception as e:
#         print(f"Error in update_year_container: {e}")

# # Callback to update the third section based on selected country and year
# @app.callback(
#     Output(component_id='output-container3', component_property='children'),
#     Input(component_id='country-drop', component_property='value'),
#     Input(component_id='year-drop', component_property='value'))
# def update_violence_container(selected_country, selected_year):
#     print(f"Selected Country: {selected_country}, Selected Year: {selected_year}")  # Debugging statement
#     try:
#         # Filter the data based on the selected country and year
#         if selected_year == 'All Years':
#             df_filtered = df[df['country'] == selected_country] if selected_country != 'All Countries' else df
#         else:
#             df_filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)] if selected_country != 'All Countries' else df[df['year'] == selected_year]

#         # Group the data by type of violence and sum the total deaths
#         tov = df_filtered.groupby('type_of_violence')['deaths_total'].sum().reset_index()

#         # Create a bar chart to display the total deaths by type of violence
#         bar3_fig = go.Figure()
#         bar3_fig.add_trace(go.Bar(x=tov['type_of_violence'], y=tov['deaths_total'], text=tov['deaths_total'], textposition='outside'))
#         bar3_fig.update_layout(barmode='stack', title='Types of Violence for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Type of Violence', yaxis_title='Total Deaths')

#         R_chart3 = dcc.Graph(figure=bar3_fig)
#         return [html.Div(className='chart-item', children=[R_chart3], style={'display': 'flex'})]
#     except Exception as e:
#         print(f"Error in update_violence_container: {e}")

# # Callback to update the fourth section based on selected country and year
# @app.callback(
#     Output(component_id='output-container4', component_property='children'),
#     Input(component_id='country-drop', component_property='value'),
#     Input(component_id='year-drop', component_property='value'))
# def update_conflicts_container(selected_country, selected_year):
#     print(f"Selected Country: {selected_country}, Selected Year: {selected_year}")  # Debugging statement
#     try:
#         # Filter the data based on the selected country and year
#         if selected_year == 'All Years':
#             df_filtered = df[df['country'] == selected_country] if selected_country != 'All Countries' else df
#         else:
#             df_filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)] if selected_country != 'All Countries' else df[df['year'] == selected_year]

#         # Group the data by conflict name and sum the total deaths
#         dpc = df_filtered.groupby('conflict_name')['deaths_total'].sum().reset_index()
#         dpc = dpc.sort_values(by='deaths_total', ascending=False)
#         dpc = dpc.head(20)

#         # Create a bar chart to display the total deaths by conflict name
#         bar4_fig = go.Figure()
#         bar4_fig.add_trace(go.Bar(x=dpc['conflict_name'], y=dpc['deaths_total'], text=dpc['deaths_total'], textposition='outside'))
#         bar4_fig.update_layout(title='Count of Deaths for Conflicts for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Conflict Name', yaxis_title='Total Deaths')
        
#         R_chart4 = dcc.Graph(figure=bar4_fig)
#         return [html.Div(className='chart-item', children=[R_chart4], style={'display': 'flex'})]
#     except Exception as e:
#         print(f"Error in update_conflicts_container: {e}")

# # Callback to update the fifth section based on selected country and year
# @app.callback(
#     Output(component_id='output-container5', component_property='children'),
#     Input(component_id='country-drop', component_property='value'),
#     Input(component_id='year-drop', component_property='value'))
# def update_region_container(selected_country, selected_year):
#     print(f"Selected Country: {selected_country}, Selected Year: {selected_year}")  # Debugging statement
#     try:
#         # Filter the data based on the selected country and year
#         if selected_year == 'All Years':
#             df_filtered = df[df['country'] == selected_country] if selected_country != 'All Countries' else df
#         else:
#             df_filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)] if selected_country != 'All Countries' else df[df['year'] == selected_year]

#         # Group the data by region and sum the deaths for each category
#         sides = df_filtered.groupby('region')[['deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown']].sum().reset_index()
#         sides = sides.sort_values(by='region')

#         # Create a bar chart to display the total deaths per region
#         bar5_fig = go.Figure()
#         bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_unknown'], name='Unknown Deaths', text=sides['deaths_unknown'], textposition='outside'))
#         bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_a'], name='Side A Deaths', text=sides['deaths_a'], textposition='outside'))
#         bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_b'], name='Side B Deaths', text=sides['deaths_b'], textposition='outside'))
#         bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_civilians'], name='Civilians Deaths', text=sides['deaths_civilians'], textposition='outside'))
#         bar5_fig.update_layout(title='Count of Deaths per Region for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Region', yaxis_title='Total Deaths')
        
#         R_chart5 = dcc.Graph(figure=bar5_fig)
#         return [html.Div(className='chart-item', children=[R_chart5], style={'display': 'flex'})]
#     except Exception as e:
#         print(f"Error in update_region_container: {e}")

# # Callback to update the sixth section based on selected country, year, and type of deaths
# @app.callback(
#     Output(component_id='output-container6', component_property='children'),
#     [
#         Input(component_id='country-drop', component_property='value'),
#         Input(component_id='year-drop', component_property='value'),
#         Input(component_id='deaths-type-radio', component_property='value')
#     ]
# )
# def update_map_container(selected_country, selected_year, selected_button):
#     print(f"Selected Country: {selected_country}, Selected Year: {selected_year}, Selected Button: {selected_button}")  # Debugging statement
#     try:
#         # Filter the data based on the selected country and year
#         if selected_country == 'All Countries':
#             if selected_year == 'All Years':
#                 df_filtered = df
#             else:
#                 df_filtered = df[df['year'] == selected_year]
#         else:
#             if selected_year == 'All Years':
#                 df_filtered = df[df['country'] == selected_country]
#             else:
#                 df_filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)]

#         # Group the data by country and ISO code, and sum the deaths based on the selected button
#         if selected_button == 'All Sides':
#             sides = df_filtered.groupby(['country', 'ISO_Code'])['deaths_total'].sum().reset_index()
#             z_values = sides['deaths_total']
#         else:
#             sides = df_filtered.groupby(['country', 'ISO_Code'])[selected_button].sum().reset_index()
#             z_values = sides[selected_button]

#         # Create a choropleth map to display the deaths by country
#         map_fig = go.Figure(data=go.Choropleth(
#             locations=sides['ISO_Code'],
#             z=z_values,
#             text=sides['country'],
#             colorscale='Blues',
#             autocolorscale=False,
#             reversescale=True,
#             marker_line_color='darkgray',
#             marker_line_width=0.5,
#             colorbar_title='Value',
#         ))

#         R_chart6 = dcc.Graph(figure=map_fig)
#         return [html.Div(className='chart-item', children=[R_chart6], style={'display': 'flex'})]
#     except Exception as e:
#         print(f"Error in update_map_container: {e}")

# # Run the Dash app
# if __name__ == '__main__':
#     app.run_server(debug=True)




import numpy as np
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

import numpy as np
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data from a CSV file using pandas
# Convert the 'country' column to string type for consistency
# Get a sorted list of unique years from the 'year' column
# Remove any rows with missing values
df = pd.read_csv("C:\\Users\\Owner\\OneDrive\\Desktop\\Autogen_Project\\data_2024.csv")
df['country'] = df['country'].astype(str)
sorted_years = sorted(df['year'].unique())
df = df.dropna()

# Calculate 'deaths_total' by summing relevant columns
df['deaths_total'] = df['deaths_a'] + df['deaths_b'] + df['deaths_civilians'] + df['deaths_unknown']

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    # Main container for the first section
    html.Div([
        # Header for the first section
        html.H1("Yearly Statistics for Nations in Conflicts",
                style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
        # Dropdown for selecting a country
        html.Div([
            html.Label("Select a country"),
            dcc.Dropdown(
                id='country-drop',
                options=[{'label': 'All Countries', 'value': 'All Countries'}] + 
                        [{'label': country, 'value': country} for country in df['country'].unique()],
                value='All Countries',
                placeholder='Select a country',
                style={'textAlign': 'left', 'width': '40%', 'padding': '3px', 'fontSize': '20px'}
            )
        ]),
        # Container to display the output based on selected country
        html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
    ], style={'width': '60%', 'float': 'left'}),
    
    # Main container for the second section
    html.Div([
        # Header for the second section
        html.H2("Count of Conflicts for Selected Year",
                style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
        # Dropdown for selecting a year
        html.Div([
            html.Label("Select A Year"),
            dcc.Dropdown(
                id='year-drop',
                options=[{'label': 'All Years', 'value': 'All Years'}] + 
                        [{'label': year, 'value': year} for year in sorted(df['year'].unique())],
                value='All Years',
                placeholder='Select a Year',
                style={'textAlign': 'left', 'width': '100%', 'padding': '3px', 'fontSize': '20px'})
        ]),
        # Container to display the output based on selected year
        html.Div(id='output-container2', className='chart-grid', style={'display': 'flex'})
    ], style={'width': '40%', 'float': 'right'}),
    
    # Main container for the third section
    html.Div([
        # Header for the third section
        html.H3("Total Deaths and Types of Violence for Selected Country",
                style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
        # Container to display the output based on selected country and year
        html.Div(id='output-container3', className='chart-grid', style={'display': 'flex'})
    ], style={'width': '60%', 'float': 'left'}),
    
    # Main container for the fourth section
    html.Div([
        # Header for the fourth section
        html.H4("Total Deaths for Conflicts in Selected Country, Year",
                style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
        # Container to display the output based on selected country and year
        html.Div(id='output-container4', className='chart-grid', style={'display': 'flex'})
    ], style={'width': '40%', 'float': 'right'}),
    
    # Main container for the fifth section
    html.Div([
        # Header for the fifth section
        html.H5("Types of Death per Region in Selected Country and Year",
                style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
        # Container to display the output based on selected country and year
        html.Div(id='output-container5', className='chart-grid', style={'display': 'flex'})
    ], style={'width': '60%', 'float': 'left'}),
    
    # Main container for the sixth section
    html.Div([
        # Header for the sixth section
        html.H6("Types of Death per Country (Map Visualization)",
                style={'textAlign': 'left', 'color': '#503D36', 'fontSize': 24}),
        # Radio buttons for selecting the type of deaths to display
        dcc.RadioItems(
            id='deaths-type-radio',
            options=[
                {'label': 'All Sides', 'value': 'All Sides'},
                {'label': 'Deaths Side A', 'value': 'deaths_a'},
                {'label': 'Deaths Side B', 'value': 'deaths_b'},
                {'label': 'Deaths Unknown', 'value': 'deaths_unknown'},
                {'label': 'Civilians Deaths', 'value': 'deaths_civilians'}
            ],
            value='All Sides',
            labelStyle={'display': 'inline-block'}
        ),
        # Container to display the output based on selected country, year, and type of deaths
        html.Div(id='output-container6', className='chart-grid', style={'display': 'flex'})
    ], style={'width': '40%', 'float': 'left'})
], style={'display': 'flex', 'flexWrap': 'wrap'})

# Callback to update the first section based on selected country
@app.callback(
    Output(component_id='output-container', component_property='children'),
    Input(component_id='country-drop', component_property='value'))
def update_country_container(selected_country):
    print(f"Selected Country: {selected_country}")  # Debugging statement
    try:
        # Handle NoneType for selected_country
        if not selected_country:
            selected_country = 'All Countries'
        
        # Filter the data based on the selected country
        if selected_country == 'All Countries':
            dfcountry = df.copy()
        else:
            dfcountry = df[df['country'] == selected_country]

        # Count the number of conflicts per year for the selected country
        dfcountry = dfcountry['year'].value_counts().to_frame().reset_index()
        dfcountry.columns = ['Year', 'Count']
        dfcountry = dfcountry.sort_values(by="Year")

        # Create a bar chart to display the counts of conflicts by year
        bar_fig = go.Figure()
        bar_fig.add_trace(go.Bar(x=dfcountry['Year'], y=dfcountry['Count']))
        bar_fig.update_layout(title="Counts of Conflicts by Year for " + selected_country)

        R_chart1 = dcc.Graph(figure=bar_fig)
        return [html.Div(className='chart-item', children=[R_chart1], style={'display': 'flex'})]
    except Exception as e:
        print(f"Error in update_country_container: {e}")

# Callback to update the second section based on selected year
@app.callback(
    Output(component_id='output-container2', component_property='children'),
    Input(component_id='year-drop', component_property='value'))
def update_year_container(selected_year):
    print(f"Selected Year: {selected_year}")  # Debugging statement
    try:
        # Handle NoneType for selected_year
        if not selected_year:
            selected_year = 'All Years'
        
        # Filter the data based on the selected year
        if selected_year == 'All Years':
            dfyear = df.copy()
            dfyear = dfyear.sort_values(by='year')
        else:
            dfyear = df[df['year'] == selected_year]
            dfyear = dfyear.sort_values(by='year')

        # Count the number of conflicts per conflict name for the selected year
        conflicts = dfyear['conflict_name'].value_counts().to_frame().reset_index()
        conflicts.columns = ['conflict_name', 'count']
        conflicts = conflicts.sort_values(by='count', ascending=False)
        conflicts = conflicts.head(15)

        # Create a bar chart to display the counts of conflicts for the selected year
        R_chart2 = dcc.Graph(
            figure=px.bar(conflicts, x='conflict_name', y='count',
                          title="Counts of Conflicts for Year " + str(selected_year))
        )
        return [html.Div(className='chart-item', children=[R_chart2], style={'display': 'flex'})]
    except Exception as e:
        print(f"Error in update_year_container: {e}")

# Callback to update the third section based on selected country and year
@app.callback(
    Output(component_id='output-container3', component_property='children'),
    Input(component_id='country-drop', component_property='value'),
    Input(component_id='year-drop', component_property='value'))
def update_violence_container(selected_country, selected_year):
    print(f"Selected Country: {selected_country}, Selected Year: {selected_year}")  # Debugging statement
    try:
        # Handle NoneType for selected_country and selected_year
        if not selected_country:
            selected_country = 'All Countries'
        if not selected_year:
            selected_year = 'All Years'

        # Filter the data based on the selected country and year
        if selected_year == 'All Years':
            df_filtered = df[df['country'] == selected_country] if selected_country != 'All Countries' else df
        else:
            df_filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)] if selected_country != 'All Countries' else df[df['year'] == selected_year]

        # Group the data by type of violence and sum the total deaths
        tov = df_filtered.groupby('type_of_violence')['deaths_total'].sum().reset_index()

        # Create a bar chart to display the total deaths by type of violence
        bar3_fig = go.Figure()
        bar3_fig.add_trace(go.Bar(x=tov['type_of_violence'], y=tov['deaths_total'], text=tov['deaths_total'], textposition='outside'))
        bar3_fig.update_layout(barmode='stack', title='Types of Violence for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Type of Violence', yaxis_title='Total Deaths')

        R_chart3 = dcc.Graph(figure=bar3_fig)
        return [html.Div(className='chart-item', children=[R_chart3], style={'display': 'flex'})]
    except Exception as e:
        print(f"Error in update_violence_container: {e}")

# Callback to update the fourth section based on selected country and year
@app.callback(
    Output(component_id='output-container4', component_property='children'),
    Input(component_id='country-drop', component_property='value'),
    Input(component_id='year-drop', component_property='value'))
def update_conflicts_container(selected_country, selected_year):
    print(f"Selected Country: {selected_country}, Selected Year: {selected_year}")  # Debugging statement
    try:
        # Handle NoneType for selected_country and selected_year
        if not selected_country:
            selected_country = 'All Countries'
        if not selected_year:
            selected_year = 'All Years'

        # Filter the data based on the selected country and year
        if selected_year == 'All Years':
            df_filtered = df[df['country'] == selected_country] if selected_country != 'All Countries' else df
        else:
            df_filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)] if selected_country != 'All Countries' else df[df['year'] == selected_year]

        # Group the data by conflict name and sum the total deaths
        dpc = df_filtered.groupby('conflict_name')['deaths_total'].sum().reset_index()
        dpc = dpc.sort_values(by='deaths_total', ascending=False)
        dpc = dpc.head(20)

        # Create a bar chart to display the total deaths by conflict name
        bar4_fig = go.Figure()
        bar4_fig.add_trace(go.Bar(x=dpc['conflict_name'], y=dpc['deaths_total'], text=dpc['deaths_total'], textposition='outside'))
        bar4_fig.update_layout(title='Count of Deaths for Conflicts for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Conflict Name', yaxis_title='Total Deaths')
        
        R_chart4 = dcc.Graph(figure=bar4_fig)
        return [html.Div(className='chart-item', children=[R_chart4], style={'display': 'flex'})]
    except Exception as e:
        print(f"Error in update_conflicts_container: {e}")

# Callback to update the fifth section based on selected country and year
@app.callback(
    Output(component_id='output-container5', component_property='children'),
    Input(component_id='country-drop', component_property='value'),
    Input(component_id='year-drop', component_property='value'))
def update_region_container(selected_country, selected_year):
    print(f"Selected Country: {selected_country}, Selected Year: {selected_year}")  # Debugging statement
    try:
        # Handle NoneType for selected_country and selected_year
        if not selected_country:
            selected_country = 'All Countries'
        if not selected_year:
            selected_year = 'All Years'

        # Filter the data based on the selected country and year
        if selected_year == 'All Years':
            df_filtered = df[df['country'] == selected_country] if selected_country != 'All Countries' else df
        else:
            df_filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)] if selected_country != 'All Countries' else df[df['year'] == selected_year]

        # Group the data by region and sum the deaths for each category
        sides = df_filtered.groupby('region')[['deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown']].sum().reset_index()
        sides = sides.sort_values(by='region')

        # Create a bar chart to display the total deaths per region
        bar5_fig = go.Figure()
        bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_unknown'], name='Unknown Deaths', text=sides['deaths_unknown'], textposition='outside'))
        bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_a'], name='Side A Deaths', text=sides['deaths_a'], textposition='outside'))
        bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_b'], name='Side B Deaths', text=sides['deaths_b'], textposition='outside'))
        bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_civilians'], name='Civilians Deaths', text=sides['deaths_civilians'], textposition='outside'))
        bar5_fig.update_layout(title='Count of Deaths per Region for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Region', yaxis_title='Total Deaths')
        
        R_chart5 = dcc.Graph(figure=bar5_fig)
        return [html.Div(className='chart-item', children=[R_chart5], style={'display': 'flex'})]
    except Exception as e:
        print(f"Error in update_region_container: {e}")

# Callback to update the sixth section based on selected country, year, and type of deaths
@app.callback(
    Output(component_id='output-container6', component_property='children'),
    [
        Input(component_id='country-drop', component_property='value'),
        Input(component_id='year-drop', component_property='value'),
        Input(component_id='deaths-type-radio', component_property='value')
    ]
)
def update_map_container(selected_country, selected_year, selected_button):
    print(f"Selected Country: {selected_country}, Selected Year: {selected_year}, Selected Button: {selected_button}")  # Debugging statement
    try:
        # Handle NoneType for selected_country and selected_year
        if not selected_country:
            selected_country = 'All Countries'
        if not selected_year:
            selected_year = 'All Years'

        # Filter the data based on the selected country and year
        if selected_country == 'All Countries':
            if selected_year == 'All Years':
                df_filtered = df
            else:
                df_filtered = df[df['year'] == selected_year]
        else:
            if selected_year == 'All Years':
                df_filtered = df[df['country'] == selected_country]
            else:
                df_filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)]

        # Group the data by country and ISO code, and sum the deaths based on the selected button
        if selected_button == 'All Sides':
            sides = df_filtered.groupby(['country', 'iso_alpha'])['deaths_total'].sum().reset_index()
            z_values = sides['deaths_total']
        else:
            sides = df_filtered.groupby(['country', 'iso_alpha'])[selected_button].sum().reset_index()
            z_values = sides[selected_button]

        # Create a choropleth map to display the deaths by country with a color scale from green (low casualties) to red (high casualties)
        map_fig = go.Figure(data=go.Choropleth(
            locations=sides['iso_alpha'],
            z=z_values,
            text=sides['country'],
            colorscale=[[0, 'green'], [1, 'red']],  # Custom color scale
            autocolorscale=False,
            reversescale=False,
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_title='Deaths',
        ))

        R_chart6 = dcc.Graph(figure=map_fig)
        return [html.Div(className='chart-item', children=[R_chart6], style={'display': 'flex'})]
    except Exception as e:
        print(f"Error in update_map_container: {e}")

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

