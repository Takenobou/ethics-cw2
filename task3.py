import pandas as pd
import plotly.express as px

# Load the data into a pandas DataFrame
df = pd.read_csv('task3_datasets/AI_index_db.csv')

color_scheme = {
    'background': '#fcf6ee',
    'text': '#333333',
    'Americas': '#3a7ca5',
    'Asia-Pacific': '#5bc0be',
    'Europe': '#9673a6',
    'Africa': '#e85d75',
    'Middle East': '#f4b400',
    'grid': '#444444'
}

# Create the bubble chart using the color sequence
fig = px.scatter(df,
                 x='Government Strategy',
                 y='Total score',
                 size='Research',
                 color='Region',
                 hover_name='Country',
                 color_discrete_map=color_scheme,
                 size_max=60)


fig.update_layout(
    title='Government Strategy vs. Total AI Score',
    xaxis_title='Government Strategy',
    yaxis_title='Total AI Score',
    paper_bgcolor=color_scheme['background'],
    plot_bgcolor=color_scheme['background'],
    font_color=color_scheme['text'],
    xaxis_gridcolor=color_scheme['grid'],
    yaxis_gridcolor=color_scheme['grid']
)

# Show the figure
fig.show()
