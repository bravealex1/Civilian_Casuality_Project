# import numpy as np
# import datetime
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import pandas as pd
# import plotly.graph_objs as go
# import plotly.express as px

# # Load the data using pandas from the specified CSV file path
# # This is the cleaned dataset
# df = pd.read_csv("C:\\Users\\Owner\\OneDrive\\Desktop\\Autogen_Project\\WarConflicts.csv")

# # Convert the 'country' column to string type for consistency
# df['country'] = df['country'].astype(str)

# # Get a sorted list of unique years from the 'year' column
# sorted_years = sorted(df['year'].unique())

# # Drop rows with any missing values to ensure clean data
# df = df.dropna()

# # Initialize the Dash app
# app = dash.Dash(__name__)

# # Define the layout of the app
# app.layout = html.Div([
#     # Main container for the first section
#     html.Div([
#         # Header for the first section
#         html.H1("Yearly Statistics for Nations in Conflicts",
#                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
#         # Dropdown for selecting a country
#         html.Div([
#             html.Label("Select a country"),
#             dcc.Dropdown(
#                 id='country-drop',
#                 options=[{'label': 'All Countries', 'value': 'All Countries'}] + 
#                         [{'label': country, 'value': country} for country in df['country'].unique()],
#                 value='All Countries',  # Default value
#                 placeholder='Select a country',
#                 style={'textAlign': 'left', 'width': '40%', 'padding': '3px', 'font-size': '20px'}
#             )
#         ]),
#         # Container to display the output based on selected country
#         html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
#     ], style={'width': '60%', 'float': 'left'}),

#     # Second section for selecting a year
#     html.Div([
#         # Header for the second section
#         html.H2("Count of Conflicts for Selected Year",
#                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
#         # Dropdown for selecting a year
#         html.Div([
#             html.Label("Select A Year"),
#             dcc.Dropdown(
#                 id='year-drop',
#                 options=[{'label': 'All Years', 'value': 'All Years'}] + 
#                         [{'label': year, 'value': year} for year in sorted_years],
#                 value='All Years',  # Default value
#                 placeholder='Select a Year',
#                 style={'textAlign': 'left', 'width': '100%', 'padding': '3px', 'font-size': '20px'})
#         ]),
#         # Container to display the output based on selected year
#         html.Div(id='output-container2', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '40%', 'float': 'right'}),

#     # Third section for displaying total deaths and types of violence for selected country and year
#     html.Div([
#         # Header for the third section
#         html.H3("Total Deaths and Types of Violence for Selected Country",
#                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
#         # Container to display the output based on selected country and year
#         html.Div(id='output-container3', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '60%', 'float': 'left'}),

#     # Fourth section for displaying total deaths for conflicts in selected country and year
#     html.Div([
#         # Header for the fourth section
#         html.H4("Total Deaths for Conflicts in selected country, year",
#                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
#         # Container to display the output based on selected country and year
#         html.Div(id='output-container4', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '40%', 'float': 'right'}),

#     # Fifth section for displaying types of deaths per region in selected country and year
#     html.Div([
#         # Header for the fifth section
#         html.H5("Types of Death per region in Selected Country and year",
#                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
#         # Container to display the output based on selected country and year
#         html.Div(id='output-container5', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '60%', 'float': 'left'}),

#     # Sixth section for displaying types of death per country with a map visualization
#     html.Div([
#         # Header for the sixth section
#         html.H6("Types of Death per Country (Map Visualization)",
#                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
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
#             value='All Sides',  # Default value
#             labelStyle={'display': 'inline-block'}
#         ),
#         # Container to display the output based on selected country, year, and type of deaths
#         html.Div(id='output-container6', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '40%', 'float': 'left'})
# ], style={'display': 'flex', 'flex-wrap': 'wrap'})

# # Callback to update the first section based on selected country
# @app.callback(
#     Output(component_id='output-container', component_property='children'),
#     Input(component_id='country-drop', component_property='value'))
# def update_input_container(selected_country):
#     # Print selected country for debugging purposes
#     print(f"Selected Country: {selected_country}")

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

#     # Return the bar chart wrapped in a div to be displayed in the output container
#     R_chart1 = dcc.Graph(figure=bar_fig)
#     return [html.Div(className='chart-item', children=[R_chart1], style={'display': 'flex'})]

# # Callback to update the second section based on selected year
# @app.callback(
#     Output(component_id='output-container2', component_property='children'),
#     Input(component_id='year-drop', component_property='value'))
# def update_input_container2(selected_year):
#     # Print selected year for debugging purposes
#     print(f"Selected Year: {selected_year}")

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
# def update_input_container3(selected_country, selected_year):
#     # Print selected country and year for debugging purposes
#     print(f"Selected Country: {selected_country}, Selected Year: {selected_year}")

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
#     bar3_fig.update_layout(barmode='stack', title='Sides and Types of Violence for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Type of Violence', yaxis_title='Total Deaths')

#     # Return the bar chart wrapped in a div to be displayed in the output container
#     R_chart3 = dcc.Graph(figure=bar3_fig)
#     return [html.Div(className='chart-item', children=[R_chart3], style={'display': 'flex'})]

# # Callback to update the fourth section based on selected country and year
# @app.callback(
#     Output(component_id='output-container4', component_property='children'),
#     Input(component_id='country-drop', component_property='value'),
#     Input(component_id='year-drop', component_property='value'))
# def update_input_container4(selected_country, selected_year):
#     # Print selected country and year for debugging purposes
#     print(f"Selected Country: {selected_country}, Selected Year: {selected_year}")

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
#     bar4_fig.update_layout(title='Count of Deaths for conflicts for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Conflict Name', yaxis_title='Total Deaths')

#     # Return the bar chart wrapped in a div to be displayed in the output container
#     R_chart4 = dcc.Graph(figure=bar4_fig)
#     return [html.Div(className='chart-item', children=[R_chart4], style={'display': 'flex'})]

# # Callback to update the fifth section based on selected country and year
# @app.callback(
#     Output(component_id='output-container5', component_property='children'),
#     Input(component_id='country-drop', component_property='value'),
#     Input(component_id='year-drop', component_property='value'))
# def update_input_container5(selected_country, selected_year):
#     # Print selected country and year for debugging purposes
#     print(f"Selected Country: {selected_country}, Selected Year: {selected_year}")

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
#     bar5_fig.update_layout(title='Count of Deaths per region for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Region', yaxis_title='Total Deaths')

#     # Return the bar chart wrapped in a div to be displayed in the output container
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
# def update_input_container6(selected_country, selected_year, selected_button):
#     # Print selected country, year, and button for debugging purposes
#     print(f"Selected Country: {selected_country}, Selected Year: {selected_year}, Selected Button: {selected_button}")

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

#     # Create a choropleth map to display the deaths by country with a color scale from green (low casualties) to red (high casualties)
#     map_fig = go.Figure(data=go.Choropleth(
#         locations=sides['ISO_Code'],
#         z=z_values,
#         text=sides['country'],
#         colorscale=[[0, 'green'], [1, 'red']],  # Custom color scale
#         autocolorscale=False,
#         reversescale=False,
#         marker_line_color='darkgray',
#         marker_line_width=0.5,
#         colorbar_title='Deaths',
#     ))

#     # Return the map wrapped in a div to be displayed in the output container
#     R_chart6 = dcc.Graph(figure=map_fig)
#     return [html.Div(className='chart-item', children=[R_chart6], style={'display': 'flex'})]

# # Run the Dash app
# if __name__ == '__main__':
#     app.run_server(debug=True)





# import numpy as np
# import datetime
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import pandas as pd
# import plotly.graph_objs as go
# import plotly.express as px

# # Load the data using pandas from the specified CSV file path
# # This is the cleaned dataset
# df = pd.read_csv("C:\\Users\\Owner\\OneDrive\\Desktop\\Autogen_Project\\WarConflicts.csv")

# # Convert the 'country' column to string type for consistency
# df['country'] = df['country'].astype(str)

# # Get a sorted list of unique years from the 'year' column
# sorted_years = sorted(df['year'].unique())

# # Drop rows with any missing values to ensure clean data
# df = df.dropna()

# # Initialize the Dash app
# app = dash.Dash(__name__)

# # Define the layout of the app
# app.layout = html.Div([
#     # Main container for the first section
#     html.Div([
#         # Header for the first section
#         html.H1("Yearly Statistics for Nations in Conflicts",
#                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
#         # Dropdown for selecting a country
#         html.Div([
#             html.Label("Select a country"),
#             dcc.Dropdown(
#                 id='country-drop',
#                 options=[{'label': 'All Countries', 'value': 'All Countries'}] + 
#                         [{'label': country, 'value': country} for country in df['country'].unique()],
#                 value='All Countries',  # Default value
#                 placeholder='Select a country',
#                 style={'textAlign': 'left', 'width': '40%', 'padding': '3px', 'font-size': '20px'}
#             )
#         ]),
#         # Container to display the output based on selected country
#         html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
#     ], style={'width': '60%', 'float': 'left'}),

#     # Second section for selecting a year
#     html.Div([
#         # Header for the second section
#         html.H2("Count of Conflicts for Selected Year",
#                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
#         # Dropdown for selecting a year
#         html.Div([
#             html.Label("Select A Year"),
#             dcc.Dropdown(
#                 id='year-drop',
#                 options=[{'label': 'All Years', 'value': 'All Years'}] + 
#                         [{'label': year, 'value': year} for year in sorted_years],
#                 value='All Years',  # Default value
#                 placeholder='Select a Year',
#                 style={'textAlign': 'left', 'width': '100%', 'padding': '3px', 'font-size': '20px'})
#         ]),
#         # Container to display the output based on selected year
#         html.Div(id='output-container2', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '40%', 'float': 'right'}),

#     # Third section for displaying total deaths and types of violence for selected country and year
#     html.Div([
#         # Header for the third section
#         html.H3("Total Deaths and Types of Violence for Selected Country",
#                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
#         # Container to display the output based on selected country and year
#         html.Div(id='output-container3', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '60%', 'float': 'left'}),

#     # Fourth section for displaying total deaths for conflicts in selected country and year
#     html.Div([
#         # Header for the fourth section
#         html.H4("Total Deaths for Conflicts in selected country, year",
#                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
#         # Container to display the output based on selected country and year
#         html.Div(id='output-container4', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '40%', 'float': 'right'}),

#     # Fifth section for displaying types of deaths per region in selected country and year
#     html.Div([
#         # Header for the fifth section
#         html.H5("Types of Death per region in Selected Country and year",
#                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
#         # Container to display the output based on selected country and year
#         html.Div(id='output-container5', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '60%', 'float': 'left'}),

#     # Sixth section for displaying types of death per country with a map visualization
#     html.Div([
#         # Header for the sixth section
#         html.H6("Types of Death per Country (Map Visualization)",
#                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
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
#             value='All Sides',  # Default value
#             labelStyle={'display': 'inline-block'}
#         ),
#         # Container to display the output based on selected country, year, and type of deaths
#         html.Div(id='output-container6', className='chart-grid', style={'display': 'flex'})
#     ], style={'width': '40%', 'float': 'left'})
# ], style={'display': 'flex', 'flex-wrap': 'wrap'})

# # Callback to update the first section based on selected country
# @app.callback(
#     Output(component_id='output-container', component_property='children'),
#     Input(component_id='country-drop', component_property='value'))
# def update_input_container(selected_country):
#     # Print selected country for debugging purposes
#     print(f"Selected Country: {selected_country}")

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

#     # Return the bar chart wrapped in a div to be displayed in the output container
#     R_chart1 = dcc.Graph(figure=bar_fig)
#     return [html.Div(className='chart-item', children=[R_chart1], style={'display': 'flex'})]

# # Callback to update the second section based on selected year
# @app.callback(
#     Output(component_id='output-container2', component_property='children'),
#     Input(component_id='year-drop', component_property='value'))
# def update_input_container2(selected_year):
#     # Print selected year for debugging purposes
#     print(f"Selected Year: {selected_year}")

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
# def update_input_container3(selected_country, selected_year):
#     # Print selected country and year for debugging purposes
#     print(f"Selected Country: {selected_country}, Selected Year: {selected_year}")

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
#     bar3_fig.update_layout(barmode='stack', title='Sides and Types of Violence for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Type of Violence', yaxis_title='Total Deaths')

#     # Return the bar chart wrapped in a div to be displayed in the output container
#     R_chart3 = dcc.Graph(figure=bar3_fig)
#     return [html.Div(className='chart-item', children=[R_chart3], style={'display': 'flex'})]

# # Callback to update the fourth section based on selected country and year
# @app.callback(
#     Output(component_id='output-container4', component_property='children'),
#     Input(component_id='country-drop', component_property='value'),
#     Input(component_id='year-drop', component_property='value'))
# def update_input_container4(selected_country, selected_year):
#     # Print selected country and year for debugging purposes
#     print(f"Selected Country: {selected_country}, Selected Year: {selected_year}")

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
#     bar4_fig.update_layout(title='Count of Deaths for conflicts for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Conflict Name', yaxis_title='Total Deaths')

#     # Return the bar chart wrapped in a div to be displayed in the output container
#     R_chart4 = dcc.Graph(figure=bar4_fig)
#     return [html.Div(className='chart-item', children=[R_chart4], style={'display': 'flex'})]

# # Callback to update the fifth section based on selected country and year
# @app.callback(
#     Output(component_id='output-container5', component_property='children'),
#     Input(component_id='country-drop', component_property='value'),
#     Input(component_id='year-drop', component_property='value'))
# def update_input_container5(selected_country, selected_year):
#     # Print selected country and year for debugging purposes
#     print(f"Selected Country: {selected_country}, Selected Year: {selected_year}")

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
#     bar5_fig.add_trace(go.Bar(x=sides['region'], y=sides['deaths_civilians'], name='Civilians Deaths', text=sides['deaths_civilians'], textposition='outside', marker=dict(color='red')))
#     bar5_fig.update_layout(title='Count of Deaths per region for ' + selected_country + ' in ' + str(selected_year), xaxis_title='Region', yaxis_title='Total Deaths')

#     # Return the bar chart wrapped in a div to be displayed in the output container
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
# def update_input_container6(selected_country, selected_year, selected_button):
#     # Print selected country, year, and button for debugging purposes
#     print(f"Selected Country: {selected_country}, Selected Year: {selected_year}, Selected Button: {selected_button}")

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

#     # Create a choropleth map to display the deaths by country with a color scale from green (low casualties) to red (high casualties)
#     map_fig = go.Figure(data=go.Choropleth(
#         locations=sides['ISO_Code'],
#         z=z_values,
#         text=sides['country'],
#         colorscale=[[0, 'green'], [1, 'red']],  # Custom color scale
#         autocolorscale=False,
#         reversescale=False,
#         marker_line_color='darkgray',
#         marker_line_width=0.5,
#         colorbar_title='Deaths',
#     ))

#     # Return the map wrapped in a div to be displayed in the output container
#     R_chart6 = dcc.Graph(figure=map_fig)
#     return [html.Div(className='chart-item', children=[R_chart6], style={'display': 'flex'})]

# # Run the Dash app
# if __name__ == '__main__':
#     app.run_server(debug=True)





# import pandas as pd
# import streamlit as st
# import plotly.graph_objs as go
# import plotly.express as px
# from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
# import speech_recognition as sr
# import streamlit_mic_recorder

# # Function to load and clean the dataset
# def load_data():
#     df = pd.read_csv("C:\\Users\\Owner\\OneDrive\\Desktop\\Autogen_Project\\WarConflicts.csv")
#     df['country'] = df['country'].astype(str)
#     df = df.dropna()
#     return df

# # Function to handle speech-to-text conversion using streamlit-mic-recorder
# def recognize_speech():
#     result = streamlit_mic_recorder.mic_recorder()
#     if result:
#         st.write("You said:", result['transcript'])
#         return result['transcript']
#     return ""

# # Main function for the Streamlit app
# def main():
#     st.title("Yearly Statistics for Nations in Conflicts")

#     # Load data
#     df = load_data()

#     # Sidebar for user input
#     st.sidebar.title("User Input")

#     # Dropdown for selecting a country
#     country = st.sidebar.selectbox(
#         "Select a country",
#         ["All Countries"] + list(df['country'].unique())
#     )

#     # Voice input for selecting a country
#     if st.sidebar.button("Use Voice Input for Country"):
#         recognized_text = recognize_speech()
#         if recognized_text in df['country'].unique() or recognized_text.lower() == "all countries":
#             country = recognized_text
#             st.sidebar.write(f"Country selected: {country}")
#         else:
#             st.sidebar.write(f"Invalid country: {recognized_text}")

#     # Dropdown for selecting a year
#     year = st.sidebar.selectbox(
#         "Select a Year",
#         ["All Years"] + sorted(df['year'].unique())
#     )

#     # Voice input for selecting a year
#     if st.sidebar.button("Use Voice Input for Year"):
#         recognized_text = recognize_speech()
#         if recognized_text.isdigit() and int(recognized_text) in df['year'].unique():
#             year = int(recognized_text)
#             st.sidebar.write(f"Year selected: {year}")
#         else:
#             st.sidebar.write(f"Invalid year: {recognized_text}")

#     # Filter the data based on the selected country
#     if country == 'All Countries':
#         df_country = df.copy()
#     else:
#         df_country = df[df['country'] == country]
    
#     # Filter the data based on the selected year
#     if year == 'All Years':
#         df_filtered = df_country
#     else:
#         df_filtered = df_country[df_country['year'] == year]
    
#     # Section 1: Count of conflicts per year for the selected country
#     st.header("Counts of Conflicts by Year")
#     counts_by_year = df_country['year'].value_counts().sort_index()
#     fig1 = go.Figure(data=[go.Bar(x=counts_by_year.index, y=counts_by_year.values)])
#     fig1.update_layout(title="Counts of Conflicts by Year for " + country)
#     st.plotly_chart(fig1)
    
#     # Section 2: Count of conflicts for the selected year
#     st.header("Count of Conflicts for Selected Year")
#     counts_by_conflict = df_filtered['conflict_name'].value_counts().head(15)
#     fig2 = px.bar(counts_by_conflict, x=counts_by_conflict.index, y=counts_by_conflict.values, title="Counts of Conflicts for Year " + str(year))
#     st.plotly_chart(fig2)

#     # Section 3: Total deaths and types of violence for selected country and year
#     st.header("Total Deaths and Types of Violence")
#     deaths_by_type = df_filtered.groupby('type_of_violence')['deaths_total'].sum().reset_index()
#     fig3 = go.Figure(data=[go.Bar(x=deaths_by_type['type_of_violence'], y=deaths_by_type['deaths_total'])])
#     fig3.update_layout(title="Total Deaths by Type of Violence in " + country + " for " + str(year))
#     st.plotly_chart(fig3)
    
#     # Section 4: Total deaths for conflicts in selected country and year
#     st.header("Total Deaths for Conflicts")
#     deaths_by_conflict = df_filtered.groupby('conflict_name')['deaths_total'].sum().sort_values(ascending=False).head(20)
#     fig4 = go.Figure(data=[go.Bar(x=deaths_by_conflict.index, y=deaths_by_conflict.values)])
#     fig4.update_layout(title="Total Deaths for Conflicts in " + country + " for " + str(year))
#     st.plotly_chart(fig4)
    
#     # Section 5: Types of deaths per region in selected country and year
#     st.header("Types of Death per Region")
#     deaths_by_region = df_filtered.groupby('region')[['deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown']].sum().reset_index()
#     fig5 = go.Figure()
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_unknown'], name='Unknown Deaths'))
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_a'], name='Side A Deaths'))
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_b'], name='Side B Deaths'))
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_civilians'], name='Civilians Deaths', marker=dict(color='red')))
#     fig5.update_layout(title='Count of Deaths per Region in ' + country + ' for ' + str(year), barmode='stack')
#     st.plotly_chart(fig5)

#     # Section 6: Types of death per country with a map visualization
#     st.header("Types of Death per Country (Map Visualization)")
#     deaths_type = st.radio(
#         "Select type of death to display",
#         ('All Sides', 'deaths_a', 'deaths_b', 'deaths_unknown', 'deaths_civilians')
#     )
#     if deaths_type == 'All Sides':
#         deaths_by_country = df_filtered.groupby(['country', 'ISO_Code'])['deaths_total'].sum().reset_index()
#         z_values = deaths_by_country['deaths_total']
#     else:
#         deaths_by_country = df_filtered.groupby(['country', 'ISO_Code'])[deaths_type].sum().reset_index()
#         z_values = deaths_by_country[deaths_type]

#     fig6 = go.Figure(data=go.Choropleth(
#         locations=deaths_by_country['ISO_Code'],
#         z=z_values,
#         text=deaths_by_country['country'],
#         colorscale=[[0, 'green'], [1, 'red']],
#         autocolorscale=False,
#         reversescale=False,
#         marker_line_color='darkgray',
#         marker_line_width=0.5,
#         colorbar_title='Deaths',
#     ))
#     fig6.update_layout(title='Types of Death per Country')
#     st.plotly_chart(fig6)

# if __name__ == "__main__":
#     main()



# import pandas as pd
# import streamlit as st
# import plotly.graph_objs as go
# import plotly.express as px
# import speech_recognition as sr

# # Function to load and clean the dataset
# def load_data():
#     df = pd.read_csv("C:\\Users\\Owner\\OneDrive\\Desktop\\Autogen_Project\\WarConflicts.csv")
#     df['country'] = df['country'].astype(str)
#     df = df.dropna()
#     return df

# # Function to handle speech-to-text conversion using speech_recognition
# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening...")
#         audio = recognizer.listen(source)
#     try:
#         text = recognizer.recognize_google(audio)
#         st.write("You said:", text)
#         return text
#     except sr.UnknownValueError:
#         st.write("Sorry, I did not understand that.")
#     except sr.RequestError:
#         st.write("Could not request results from the speech recognition service.")
#     return ""

# # Function to parse speech input for country and year
# def parse_speech_input(speech, countries, years):
#     country = None
#     year = None
    
#     # Split the speech by "and" to handle both country and year
#     parts = speech.lower().split(" and ")
    
#     for part in parts:
#         for c in countries:
#             if c.lower() in part:
#                 country = c
#                 break
        
#         for y in years:
#             if str(y) in part:
#                 year = y
#                 break
    
#     return country, year

# # Main function for the Streamlit app
# def main():
#     st.title("Yearly Statistics for Nations in Conflicts")

#     # Load data
#     df = load_data()

#     # Sidebar for user input
#     st.sidebar.title("User Input")

#     # Initialize country and year
#     country = 'All Countries'
#     year = 'All Years'

#     # Get unique countries and years from the dataset
#     countries = list(df['country'].unique())
#     years = sorted(df['year'].unique())

#     # Dropdown for selecting a country
#     country_dropdown = st.sidebar.selectbox(
#         "Select a country",
#         ["All Countries"] + countries,
#         key="country"
#     )

#     # Set country to the value selected by the dropdown if voice input was not used
#     if country == 'All Countries':
#         country = country_dropdown

#     # Filter the data based on the selected country
#     if country == 'All Countries':
#         df_country = df.copy()
#     else:
#         df_country = df[df['country'] == country]

#     # Dropdown for selecting a year (only show relevant years based on the selected country)
#     year_dropdown = st.sidebar.selectbox(
#         "Select a Year",
#         ["All Years"] + sorted(df_country['year'].unique()),
#         key="year"
#     )

#     # Set year to the value selected by the dropdown if voice input was not used
#     if year == 'All Years':
#         year = year_dropdown

#     # Voice input for selecting country and year
#     if st.sidebar.button("Use Voice Input for Country and Year"):
#         recognized_text = recognize_speech()
#         recognized_country, recognized_year = parse_speech_input(recognized_text, countries, years)
        
#         if recognized_country:
#             country = recognized_country
#         else:
#             st.sidebar.write(f"Invalid country in the speech: {recognized_text}")
        
#         if recognized_year:
#             year = recognized_year
#         else:
#             st.sidebar.write(f"Invalid year in the speech: {recognized_text}")

#         st.sidebar.write(f"Country selected: {country}")
#         st.sidebar.write(f"Year selected: {year}")

#     # Filter the data based on the selected year
#     if year == 'All Years':
#         df_filtered = df_country
#     else:
#         df_filtered = df_country[df_country['year'] == year]

#     # Section 1: Count of conflicts per year for the selected country
#     st.header("Counts of Conflicts by Year")
#     counts_by_year = df_country['year'].value_counts().sort_index()
#     fig1 = go.Figure(data=[go.Bar(x=counts_by_year.index, y=counts_by_year.values)])
#     fig1.update_layout(title="Counts of Conflicts by Year for " + country)
#     st.plotly_chart(fig1)

#     # Section 2: Count of conflicts for the selected year
#     st.header("Count of Conflicts for Selected Year")
#     counts_by_conflict = df_filtered['conflict_name'].value_counts().head(15)
#     fig2 = px.bar(counts_by_conflict, x=counts_by_conflict.index, y=counts_by_conflict.values, title="Counts of Conflicts for Year " + str(year))
#     st.plotly_chart(fig2)

#     # Section 3: Total deaths and types of violence for selected country and year
#     st.header("Total Deaths and Types of Violence")
#     deaths_by_type = df_filtered.groupby('type_of_violence')['deaths_total'].sum().reset_index()
#     fig3 = go.Figure(data=[go.Bar(x=deaths_by_type['type_of_violence'], y=deaths_by_type['deaths_total'])])
#     fig3.update_layout(title="Total Deaths by Type of Violence in " + country + " for " + str(year))
#     st.plotly_chart(fig3)

#     # Section 4: Total deaths for conflicts in selected country and year
#     st.header("Total Deaths for Conflicts")
#     deaths_by_conflict = df_filtered.groupby('conflict_name')['deaths_total'].sum().sort_values(ascending=False).head(20)
#     fig4 = go.Figure(data=[go.Bar(x=deaths_by_conflict.index, y=deaths_by_conflict.values)])
#     fig4.update_layout(title="Total Deaths for Conflicts in " + country + " for " + str(year))
#     st.plotly_chart(fig4)

#     # Section 5: Types of deaths per region in selected country and year
#     st.header("Types of Death per Region")
#     deaths_by_region = df_filtered.groupby('region')[['deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown']].sum().reset_index()
#     fig5 = go.Figure()
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_unknown'], name='Unknown Deaths'))
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_a'], name='Side A Deaths'))
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_b'], name='Side B Deaths'))
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_civilians'], name='Civilians Deaths', marker=dict(color='red')))
#     fig5.update_layout(title='Count of Deaths per Region in ' + country + ' for ' + str(year), barmode='stack')
#     st.plotly_chart(fig5)

#     # Section 6: Types of death per country with a map visualization
#     st.header("Types of Death per Country (Map Visualization)")
#     deaths_type = st.radio(
#         "Select type of death to display",
#         ('All Sides', 'deaths_a', 'deaths_b', 'deaths_unknown', 'deaths_civilians')
#     )
#     if deaths_type == 'All Sides':
#         deaths_by_country = df_filtered.groupby(['country', 'ISO_Code'])['deaths_total'].sum().reset_index()
#         z_values = deaths_by_country['deaths_total']
#     else:
#         deaths_by_country = df_filtered.groupby(['country', 'ISO_Code'])[deaths_type].sum().reset_index()
#         z_values = deaths_by_country[deaths_type]

#     fig6 = go.Figure(data=go.Choropleth(
#         locations=deaths_by_country['ISO_Code'],
#         z=z_values,
#         text=deaths_by_country['country'],
#         colorscale=[[0, 'green'], [1, 'red']],
#         autocolorscale=False,
#         reversescale=False,
#         marker_line_color='darkgray',
#         marker_line_width=0.5,
#         colorbar_title='Deaths',
#     ))
#     fig6.update_layout(title='Types of Death per Country')
#     st.plotly_chart(fig6)

# if __name__ == "__main__":
#     main()



# import pandas as pd
# import streamlit as st
# import plotly.graph_objs as go
# import plotly.express as px
# import speech_recognition as sr
# from newspaper import Article
# from transformers import pipeline

# # Load pre-trained summarization and NER models
# summarizer = pipeline("summarization")
# ner = pipeline("ner", grouped_entities=True)

# # Function to load and clean the dataset
# def load_data():
#     df = pd.read_csv("C:\\Users\\Owner\\OneDrive\\Desktop\\Autogen_Project\\WarConflicts.csv")
#     df['country'] = df['country'].astype(str)
#     df = df.dropna()
#     return df

# # Function to handle speech-to-text conversion using speech_recognition
# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening...")
#         audio = recognizer.listen(source)
#     try:
#         text = recognizer.recognize_google(audio)
#         st.write("You said:", text)
#         return text
#     except sr.UnknownValueError:
#         st.write("Sorry, I did not understand that.")
#     except sr.RequestError:
#         st.write("Could not request results from the speech recognition service.")
#     return ""

# # Function to parse speech input for country and year
# def parse_speech_input(speech, countries, years):
#     country = None
#     year = None
    
#     # Split the speech by "and" to handle both country and year
#     parts = speech.lower().split(" and ")
    
#     for part in parts:
#         for c in countries:
#             if c.lower() in part:
#                 country = c
#                 break
        
#         for y in years:
#             if str(y) in part:
#                 year = y
#                 break
    
#     return country, year

# # Function to fetch and summarize news articles for a given conflict
# def fetch_news(conflict_name):
#     query = conflict_name + " news"
#     articles = []
#     # Use newspaper3k to scrape news articles (This is just a placeholder for actual news scraping logic)
#     article = Article(f'https://example.com/{query}')
#     article.download()
#     article.parse()
#     article.nlp()
#     summary = summarizer(article.text, max_length=150, min_length=50, do_sample=False)
#     entities = ner(article.text)
#     articles.append({
#         'title': article.title,
#         'summary': summary[0]['summary_text'],
#         'entities': entities,
#         'source': article.source_url
#     })
#     return articles

# # Main function for the Streamlit app
# def main():
#     st.title("Yearly Statistics for Nations in Conflicts")

#     # Load data
#     df = load_data()

#     # Sidebar for user input
#     st.sidebar.title("User Input")

#     # Initialize country and year
#     country = 'All Countries'
#     year = 'All Years'

#     # Get unique countries and years from the dataset
#     countries = list(df['country'].unique())
#     years = sorted(df['year'].unique())

#     # Dropdown for selecting a country
#     country_dropdown = st.sidebar.selectbox(
#         "Select a country",
#         ["All Countries"] + countries,
#         key="country"
#     )

#     # Set country to the value selected by the dropdown if voice input was not used
#     if country == 'All Countries':
#         country = country_dropdown

#     # Filter the data based on the selected country
#     if country == 'All Countries':
#         df_country = df.copy()
#     else:
#         df_country = df[df['country'] == country]

#     # Dropdown for selecting a year (only show relevant years based on the selected country)
#     year_dropdown = st.sidebar.selectbox(
#         "Select a Year",
#         ["All Years"] + sorted(df_country['year'].unique()),
#         key="year"
#     )

#     # Set year to the value selected by the dropdown if voice input was not used
#     if year == 'All Years':
#         year = year_dropdown

#     # Voice input for selecting country and year
#     if st.sidebar.button("Use Voice Input for Country and Year"):
#         recognized_text = recognize_speech()
#         recognized_country, recognized_year = parse_speech_input(recognized_text, countries, years)
        
#         if recognized_country:
#             country = recognized_country
#         else:
#             st.sidebar.write(f"Invalid country in the speech: {recognized_text}")
        
#         if recognized_year:
#             year = recognized_year
#         else:
#             st.sidebar.write(f"Invalid year in the speech: {recognized_text}")

#         st.sidebar.write(f"Country selected: {country}")
#         st.sidebar.write(f"Year selected: {year}")

#     # Filter the data based on the selected year
#     if year == 'All Years':
#         df_filtered = df_country
#     else:
#         df_filtered = df_country[df_country['year'] == year]

#     # Section 1: Count of conflicts per year for the selected country
#     st.header("Counts of Conflicts by Year")
#     counts_by_year = df_country['year'].value_counts().sort_index()
#     fig1 = go.Figure(data=[go.Bar(x=counts_by_year.index, y=counts_by_year.values)])
#     fig1.update_layout(title="Counts of Conflicts by Year for " + country)
#     st.plotly_chart(fig1)

#     # Section 2: Count of conflicts for the selected year
#     st.header("Count of Conflicts for Selected Year")
#     counts_by_conflict = df_filtered['conflict_name'].value_counts().head(15)
#     fig2 = px.bar(counts_by_conflict, x=counts_by_conflict.index, y=counts_by_conflict.values, title="Counts of Conflicts for Year " + str(year))
#     st.plotly_chart(fig2)

#     # Section 3: Total deaths and types of violence for selected country and year
#     st.header("Total Deaths and Types of Violence")
#     deaths_by_type = df_filtered.groupby('type_of_violence')['deaths_total'].sum().reset_index()
#     fig3 = go.Figure(data=[go.Bar(x=deaths_by_type['type_of_violence'], y=deaths_by_type['deaths_total'])])
#     fig3.update_layout(title="Total Deaths by Type of Violence in " + country + " for " + str(year))
#     st.plotly_chart(fig3)

#     # Section 4: Total deaths for conflicts in selected country and year
#     st.header("Total Deaths for Conflicts")
#     deaths_by_conflict = df_filtered.groupby('conflict_name')['deaths_total'].sum().sort_values(ascending=False).head(20)
#     fig4 = go.Figure(data=[go.Bar(x=deaths_by_conflict.index, y=deaths_by_conflict.values)])
#     fig4.update_layout(title="Total Deaths for Conflicts in " + country + " for " + str(year))
#     st.plotly_chart(fig4)

#     # Section 5: Types of deaths per region in selected country and year
#     st.header("Types of Death per Region")
#     deaths_by_region = df_filtered.groupby('region')[['deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown']].sum().reset_index()
#     fig5 = go.Figure()
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_unknown'], name='Unknown Deaths'))
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_a'], name='Side A Deaths'))
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_b'], name='Side B Deaths'))
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_civilians'], name='Civilians Deaths', marker=dict(color='red')))
#     fig5.update_layout(title='Count of Deaths per Region in ' + country + ' for ' + str(year), barmode='stack')
#     st.plotly_chart(fig5)

#     # Section 6: Types of death per country with a map visualization
#     st.header("Types of Death per Country (Map Visualization)")
#     deaths_type = st.radio(
#         "Select type of death to display",
#         ('All Sides', 'deaths_a', 'deaths_b', 'deaths_unknown', 'deaths_civilians')
#     )
#     if deaths_type == 'All Sides':
#         deaths_by_country = df_filtered.groupby(['country', 'ISO_Code'])['deaths_total'].sum().reset_index()
#         z_values = deaths_by_country['deaths_total']
#     else:
#         deaths_by_country = df_filtered.groupby(['country', 'ISO_Code'])[deaths_type].sum().reset_index()
#         z_values = deaths_by_country[deaths_type]

#     fig6 = go.Figure(data=go.Choropleth(
#         locations=deaths_by_country['ISO_Code'],
#         z=z_values,
#         text=deaths_by_country['country'],
#         colorscale=[[0, 'green'], [1, 'red']],
#         autocolorscale=False,
#         reversescale=False,
#         marker_line_color='darkgray',
#         marker_line_width=0.5,
#         colorbar_title='Deaths',
#     ))
#     fig6.update_layout(title='Types of Death per Country')
#     st.plotly_chart(fig6)

#     # Section 7: News reports for major conflicts
#     st.header("News Reports for Major Conflicts")
#     for conflict in df_filtered['conflict_name'].unique():
#         st.subheader(conflict)
#         articles = fetch_news(conflict)
#         for article in articles:
#             st.markdown(f"**Title:** {article['title']}")
#             st.markdown(f"**Summary:** {article['summary']}")
#             st.markdown(f"**Entities:** {', '.join([entity['word'] for entity in article['entities']])}")
#             st.markdown(f"**Source:** [Link]({article['source']})")

# if __name__ == "__main__":
#     main()


# import pandas as pd
# import streamlit as st
# import plotly.graph_objs as go
# import plotly.express as px
# import speech_recognition as sr
# import requests
# from transformers import pipeline

# # Load pre-trained summarization and NER models
# summarizer = pipeline("summarization")
# ner = pipeline("ner", grouped_entities=True)

# # Function to load and clean the dataset
# def load_data():
#     # Load the CSV data into a DataFrame
#     df = pd.read_csv("C:\\Users\\Owner\\OneDrive\\Desktop\\Autogen_Project\\WarConflicts.csv")
#     df['country'] = df['country'].astype(str)  # Ensure 'country' column is of type string
#     df = df.dropna()  # Drop rows with missing values
#     return df

# # Function to handle speech-to-text conversion using speech_recognition
# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening...")
#         audio = recognizer.listen(source)  # Capture audio from the microphone
#     try:
#         text = recognizer.recognize_google(audio)  # Convert speech to text using Google API
#         st.write("You said:", text)
#         return text
#     except sr.UnknownValueError:
#         st.write("Sorry, I did not understand that.")  # Handle unrecognized speech
#     except sr.RequestError:
#         st.write("Could not request results from the speech recognition service.")  # Handle API request failure
#     return ""

# # Function to parse speech input for country and year
# def parse_speech_input(speech, countries, years):
#     country = None
#     year = None
    
#     # Split the speech by "and" to handle both country and year
#     parts = speech.lower().split(" and ")
    
#     for part in parts:
#         for c in countries:
#             if c.lower() in part:
#                 country = c
#                 break
        
#         for y in years:
#             if str(y) in part:
#                 year = y
#                 break
    
#     return country, year

# # Function to fetch and summarize news articles for a given conflict using NewsAPI
# def fetch_news(country, year=None):
#     api_key = 'ed5e38f530134429aa5110a67ae09b95'  # Replace with your NewsAPI key
#     query = f'{country} conflict'
#     articles = []
    
#     # Construct the API URL
#     url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
#     if year:
#         url += f'&from={year}-01-01&to={year}-12-31'

#     try:
#         # Fetch articles from NewsAPI
#         response = requests.get(url)
#         data = response.json()
        
#         if data['status'] != 'ok':
#             st.write(f"Failed to fetch news articles: {data['message']}")
#             return articles
        
#         # Process each article
#         for article_data in data['articles']:
#             title = article_data['title']
#             content = article_data['content']
#             source_url = article_data['url']
            
#             # Summarize the article content
#             summary = summarizer(content, max_length=150, min_length=50, do_sample=False)
#             entities = ner(content)
            
#             articles.append({
#                 'title': title,
#                 'summary': summary[0]['summary_text'],
#                 'entities': entities,
#                 'source': source_url
#             })
#     except Exception as e:
#         st.write(f"An error occurred: {e}")
    
#     return articles

# # Main function for the Streamlit app
# def main():
#     st.title("Yearly Statistics for Nations in Conflicts")

#     # Load data
#     df = load_data()

#     # Sidebar for user input
#     st.sidebar.title("User Input")

#     # Initialize country and year
#     country = 'All Countries'
#     year = 'All Years'

#     # Get unique countries and years from the dataset
#     countries = list(df['country'].unique())
#     years = sorted(df['year'].unique())

#     # Dropdown for selecting a country
#     country_dropdown = st.sidebar.selectbox(
#         "Select a country",
#         ["All Countries"] + countries,
#         key="country"
#     )

#     # Set country to the value selected by the dropdown if voice input was not used
#     if country == 'All Countries':
#         country = country_dropdown

#     # Filter the data based on the selected country
#     if country == 'All Countries':
#         df_country = df.copy()
#     else:
#         df_country = df[df['country'] == country]

#     # Dropdown for selecting a year (only show relevant years based on the selected country)
#     year_dropdown = st.sidebar.selectbox(
#         "Select a Year",
#         ["All Years"] + sorted(df_country['year'].unique()),
#         key="year"
#     )

#     # Set year to the value selected by the dropdown if voice input was not used
#     if year == 'All Years':
#         year = year_dropdown

#     # Voice input for selecting country and year
#     if st.sidebar.button("Use Voice Input for Country and Year"):
#         recognized_text = recognize_speech()
#         recognized_country, recognized_year = parse_speech_input(recognized_text, countries, years)
        
#         if recognized_country:
#             country = recognized_country
#         else:
#             st.sidebar.write(f"Invalid country in the speech: {recognized_text}")
        
#         if recognized_year:
#             year = recognized_year
#         else:
#             st.sidebar.write(f"Invalid year in the speech: {recognized_text}")

#         st.sidebar.write(f"Country selected: {country}")
#         st.sidebar.write(f"Year selected: {year}")

#     # Filter the data based on the selected year
#     if year == 'All Years':
#         df_filtered = df_country
#     else:
#         df_filtered = df_country[df_country['year'] == year]

#     # Section 1: Count of conflicts per year for the selected country
#     st.header("Counts of Conflicts by Year")
#     counts_by_year = df_country['year'].value_counts().sort_index()
#     fig1 = go.Figure(data=[go.Bar(x=counts_by_year.index, y=counts_by_year.values)])
#     fig1.update_layout(title="Counts of Conflicts by Year for " + country)
#     st.plotly_chart(fig1)

#     # Section 2: Count of conflicts for the selected year
#     st.header("Count of Conflicts for Selected Year")
#     counts_by_conflict = df_filtered['conflict_name'].value_counts().head(15)
#     fig2 = px.bar(counts_by_conflict, x=counts_by_conflict.index, y=counts_by_conflict.values, title="Counts of Conflicts for Year " + str(year))
#     st.plotly_chart(fig2)

#     # Section 3: Total deaths and types of violence for selected country and year
#     st.header("Total Deaths and Types of Violence")
#     deaths_by_type = df_filtered.groupby('type_of_violence')['deaths_total'].sum().reset_index()
#     fig3 = go.Figure(data=[go.Bar(x=deaths_by_type['type_of_violence'], y=deaths_by_type['deaths_total'])])
#     fig3.update_layout(title="Total Deaths by Type of Violence in " + country + " for " + str(year))
#     st.plotly_chart(fig3)

#     # Section 4: Total deaths for conflicts in selected country and year
#     st.header("Total Deaths for Conflicts")
#     deaths_by_conflict = df_filtered.groupby('conflict_name')['deaths_total'].sum().sort_values(ascending=False).head(20)
#     fig4 = go.Figure(data=[go.Bar(x=deaths_by_conflict.index, y=deaths_by_conflict.values)])
#     fig4.update_layout(title="Total Deaths for Conflicts in " + country + " for " + str(year))
#     st.plotly_chart(fig4)

#     # Section 5: Types of deaths per region in selected country and year
#     st.header("Types of Death per Region")
#     deaths_by_region = df_filtered.groupby('region')[['deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown']].sum().reset_index()
#     fig5 = go.Figure()
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_unknown'], name='Unknown Deaths'))
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_a'], name='Side A Deaths'))
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_b'], name='Side B Deaths'))
#     fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_civilians'], name='Civilians Deaths', marker=dict(color='red')))
#     fig5.update_layout(title='Count of Deaths per Region in ' + country + ' for ' + str(year), barmode='stack')
#     st.plotly_chart(fig5)

#     # Section 6: Types of death per country with a map visualization
#     st.header("Types of Death per Country (Map Visualization)")
#     deaths_type = st.radio(
#         "Select type of death to display",
#         ('All Sides', 'deaths_a', 'deaths_b', 'deaths_unknown', 'deaths_civilians')
#     )
#     if deaths_type == 'All Sides':
#         deaths_by_country = df_filtered.groupby(['country', 'ISO_Code'])['deaths_total'].sum().reset_index()
#         z_values = deaths_by_country['deaths_total']
#     else:
#         deaths_by_country = df_filtered.groupby(['country', 'ISO_Code'])[deaths_type].sum().reset_index()
#         z_values = deaths_by_country[deaths_type]

#     fig6 = go.Figure(data=go.Choropleth(
#         locations=deaths_by_country['ISO_Code'],
#         z=z_values,
#         text=deaths_by_country['country'],
#         colorscale=[[0, 'green'], [1, 'red']],
#         autocolorscale=False,
#         reversescale=False,
#         marker_line_color='darkgray',
#         marker_line_width=0.5,
#         colorbar_title='Deaths',
#     ))
#     fig6.update_layout(title='Types of Death per Country')
#     st.plotly_chart(fig6)

#     # Section 7: News reports for major conflicts
#     st.header("News Reports for Major Conflicts")
#     if country != 'All Countries':  # Ensure news is only fetched when a specific country is selected
#         articles = fetch_news(country, year if year != 'All Years' else None)
#         for article in articles:
#             st.subheader(article['title'])
#             st.markdown(f"**Summary:** {article['summary']}")
#             st.markdown(f"**Entities:** {', '.join([entity['word'] for entity in article['entities']])}")
#             st.markdown(f"**Source:** [Link]({article['source']})")

# if __name__ == "__main__":
#     main()





import os
# Disable oneDNN custom operations to avoid numerical differences due to floating-point round-off errors
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf  # Import TensorFlow
import pandas as pd  # Import pandas for data manipulation
import streamlit as st  # Import Streamlit for creating the web app
import plotly.graph_objs as go  # Import Plotly graph objects for data visualization
import plotly.express as px  # Import Plotly Express for simpler plotting
import speech_recognition as sr  # Import speech_recognition for speech-to-text functionality
import requests  # Import requests for making API calls
from transformers import pipeline  # Import pipeline from transformers for NLP tasks

# Load pre-trained summarization and NER models with specified model names and revisions
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")
ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", revision="f2482bf", aggregation_strategy="simple")

# # Load pre-trained summarization and NER models
# summarizer = pipeline("summarization")
# ner = pipeline("ner", grouped_entities=True)

# Load pre-trained summarization and NER models with specified model names and revisions
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")
ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", revision="f2482bf", aggregation_strategy="simple")

# Function to load and clean the dataset
def load_data():
    # Load the CSV data into a DataFrame
    df = pd.read_csv("C:\\Users\\Owner\\OneDrive\\Desktop\\Autogen_Project\\WarConflicts.csv")
    df['country'] = df['country'].astype(str)  # Ensure 'country' column is of type string
    df = df.dropna()  # Drop rows with missing values
    return df

# Function to handle speech-to-text conversion using speech_recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)  # Capture audio from the microphone
    try:
        text = recognizer.recognize_google(audio)  # Convert speech to text using Google API
        st.write("You said:", text)
        return text
    except sr.UnknownValueError:
        st.write("Sorry, I did not understand that.")  # Handle unrecognized speech
    except sr.RequestError:
        st.write("Could not request results from the speech recognition service.")  # Handle API request failure
    return ""

# Function to parse speech input for country and year
def parse_speech_input(speech, countries, years):
    country = None
    year = None
    
    # Split the speech by "and" to handle both country and year
    parts = speech.lower().split(" and ")
    
    for part in parts:
        for c in countries:
            if c.lower() in part:
                country = c
                break
        
        for y in years:
            if str(y) in part:
                year = y
                break
    
    return country, year

# # Function to fetch and summarize news articles for a given conflict using NewsData.io API
# def fetch_news(country, year=None):
#     # Replace with your NewsData.io API key
#     api_key = 'pub_49597a12e3858f27b4e6866710ef8634dfa59'
#     query = f'{country} conflict'  # Query to search for news articles about the country's conflict
#     articles = []

#     # Construct the API URL
#     url = f'https://newsdata.io/api/1/news?apikey={api_key}&q={query}'
#     if year:  # If the year is specified, add date range parameters to the URL
#         url += f'&from_date={year}-01-01&to_date={year}-12-31'

#     try:
#         # Fetch articles from NewsData.io API
#         response = requests.get(url)
#         data = response.json()
        
#         # Check if the API response is successful
#         if data['status'] != 'success':
#             st.write(f"Failed to fetch news articles: {data['message']}")
#             return articles
        
#         # Process each article in the API response
#         for article_data in data['results']:
#             title = article_data['title']  # Extract the article title
#             content = article_data['description'] or article_data['content']  # Extract the article content
#             source_url = article_data['link']  # Extract the article source URL
            
#             # Summarize the article content using the summarizer model
#             summary = summarizer(content, max_length=150, min_length=50, do_sample=False)
#             entities = ner(content)  # Perform named entity recognition on the content
            
#             # Append the article details to the articles list
#             articles.append({
#                 'title': title,
#                 'summary': summary[0]['summary_text'],
#                 'entities': entities,
#                 'source': source_url
#             })
#     except Exception as e:
#         # Handle any exceptions that occur during the API request or processing
#         st.write(f"An error occurred: {e}")
    
#     return articles  # Return the list of processed articles





# Function to determine appropriate max_length for summarization based on input length
def dynamic_max_length(input_length):
    return max(16, int(input_length * 0.5))


# Function to fetch and summarize news articles for a given conflict using NewsData.io API
def fetch_news(country, year=None):
    api_key = 'pub_49597a12e3858f27b4e6866710ef8634dfa59'  # Replace with your NewsData.io API key
    query = f'{country} conflict'  # Query to search for news articles about the country's conflict
    articles = []

    url = f'https://newsdata.io/api/1/news?apikey={api_key}&q={query}'
    if year:  # If the year is specified, add date range parameters to the URL
        url += f'&from_date={year}-01-01&to_date={year}-12-31'

    try:
        response = requests.get(url)
        data = response.json()
        
        if data['status'] != 'success':
            st.write(f"Failed to fetch news articles: {data['message']}")
            return articles
        
        for article_data in data['results']:
            title = article_data['title']  # Extract the article title
            content = article_data['description'] or article_data['content']  # Extract the article content
            source_url = article_data['link']  # Extract the article source URL
            
            summary = summarizer(content, max_length=dynamic_max_length(len(content.split())), min_length=50, do_sample=False)
            entities = ner(content)  # Perform named entity recognition on the content
            
            articles.append({
                'title': title,
                'summary': summary[0]['summary_text'],
                'entities': entities,
                'source': source_url
            })
    except Exception as e:
        st.write(f"An error occurred: {e}")
    
    return articles  # Return the list of processed articles


# Main function for the Streamlit app
def main():
    st.title("Yearly Statistics for Nations in Conflicts")

    # Load data
    df = load_data()

    # Sidebar for user input
    st.sidebar.title("User Input")

    # Initialize country and year
    country = 'All Countries'
    year = 'All Years'

    # Get unique countries and years from the dataset
    countries = list(df['country'].unique())
    years = sorted(df['year'].unique())

    # Dropdown for selecting a country
    country_dropdown = st.sidebar.selectbox(
        "Select a country",
        ["All Countries"] + countries,
        key="country"
    )

    # Set country to the value selected by the dropdown if voice input was not used
    if country == 'All Countries':
        country = country_dropdown

    # Filter the data based on the selected country
    if country == 'All Countries':
        df_country = df.copy()
    else:
        df_country = df[df['country'] == country]

    # Dropdown for selecting a year (only show relevant years based on the selected country)
    year_dropdown = st.sidebar.selectbox(
        "Select a Year",
        ["All Years"] + sorted(df_country['year'].unique()),
        key="year"
    )

    # Set year to the value selected by the dropdown if voice input was not used
    if year == 'All Years':
        year = year_dropdown

    # Voice input for selecting country and year
    if st.sidebar.button("Use Voice Input for Country and Year"):
        recognized_text = recognize_speech()
        recognized_country, recognized_year = parse_speech_input(recognized_text, countries, years)
        
        if recognized_country:
            country = recognized_country
        else:
            st.sidebar.write(f"Invalid country in the speech: {recognized_text}")
        
        if recognized_year:
            year = recognized_year
        else:
            st.sidebar.write(f"Invalid year in the speech: {recognized_text}")

        st.sidebar.write(f"Country selected: {country}")
        st.sidebar.write(f"Year selected: {year}")

    # Filter the data based on the selected year
    if year == 'All Years':
        df_filtered = df_country
    else:
        df_filtered = df_country[df_country['year'] == year]

    # Section 1: Count of conflicts per year for the selected country
    st.header("Counts of Conflicts by Year")
    counts_by_year = df_country['year'].value_counts().sort_index()
    fig1 = go.Figure(data=[go.Bar(x=counts_by_year.index, y=counts_by_year.values)])
    fig1.update_layout(title="Counts of Conflicts by Year for " + country)
    st.plotly_chart(fig1)

    # Section 2: Count of conflicts for the selected year
    st.header("Count of Conflicts for Selected Year")
    counts_by_conflict = df_filtered['conflict_name'].value_counts().head(15)
    fig2 = px.bar(counts_by_conflict, x=counts_by_conflict.index, y=counts_by_conflict.values, title="Counts of Conflicts for Year " + str(year))
    st.plotly_chart(fig2)

    # Section 3: Total deaths and types of violence for selected country and year
    st.header("Total Deaths and Types of Violence")
    deaths_by_type = df_filtered.groupby('type_of_violence')['deaths_total'].sum().reset_index()
    fig3 = go.Figure(data=[go.Bar(x=deaths_by_type['type_of_violence'], y=deaths_by_type['deaths_total'])])
    fig3.update_layout(title="Total Deaths by Type of Violence in " + country + " for " + str(year))
    st.plotly_chart(fig3)

    # Section 4: Total deaths for conflicts in selected country and year
    st.header("Total Deaths for Conflicts")
    deaths_by_conflict = df_filtered.groupby('conflict_name')['deaths_total'].sum().sort_values(ascending=False).head(20)
    fig4 = go.Figure(data=[go.Bar(x=deaths_by_conflict.index, y=deaths_by_conflict.values)])
    fig4.update_layout(title="Total Deaths for Conflicts in " + country + " for " + str(year))
    st.plotly_chart(fig4)

    # Section 5: Types of deaths per region in selected country and year
    st.header("Types of Death per Region")
    deaths_by_region = df_filtered.groupby('region')[['deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown']].sum().reset_index()
    fig5 = go.Figure()
    fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_unknown'], name='Unknown Deaths'))
    fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_a'], name='Side A Deaths'))
    fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_b'], name='Side B Deaths'))
    fig5.add_trace(go.Bar(x=deaths_by_region['region'], y=deaths_by_region['deaths_civilians'], name='Civilians Deaths', marker=dict(color='red')))
    fig5.update_layout(title='Count of Deaths per Region in ' + country + ' for ' + str(year), barmode='stack')
    st.plotly_chart(fig5)

    # Section 6: Types of death per country with a map visualization
    st.header("Types of Death per Country (Map Visualization)")
    deaths_type = st.radio(
        "Select type of death to display",
        ('All Sides', 'deaths_a', 'deaths_b', 'deaths_unknown', 'deaths_civilians')
    )
    if deaths_type == 'All Sides':
        deaths_by_country = df_filtered.groupby(['country', 'ISO_Code'])['deaths_total'].sum().reset_index()
        z_values = deaths_by_country['deaths_total']
    else:
        deaths_by_country = df_filtered.groupby(['country', 'ISO_Code'])[deaths_type].sum().reset_index()
        z_values = deaths_by_country[deaths_type]

    fig6 = go.Figure(data=go.Choropleth(
        locations=deaths_by_country['ISO_Code'],
        z=z_values,
        text=deaths_by_country['country'],
        colorscale=[[0, 'green'], [1, 'red']],
        autocolorscale=False,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title='Deaths',
    ))
    fig6.update_layout(title='Types of Death per Country')
    st.plotly_chart(fig6)

    # Section 7: News reports for major conflicts
    st.header("News Reports for Major Conflicts")
    if country != 'All Countries':  # Ensure news is only fetched when a specific country is selected
        articles = fetch_news(country, year if year != 'All Years' else None)
        for article in articles:
            st.subheader(article['title'])
            st.markdown(f"**Summary:** {article['summary']}")
            st.markdown(f"**Entities:** {', '.join([entity['word'] for entity in article['entities']])}")
            st.markdown(f"**Source:** [Link]({article['source']})")

if __name__ == "__main__":
    main()