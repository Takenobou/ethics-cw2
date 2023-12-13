import pandas as pd
import plotly.graph_objs as go


def load_dataset(filepath, encoding=None):
    try:
        return pd.read_csv(filepath, encoding=encoding)
    except UnicodeDecodeError:
        # If UnicodeDecodeError is raised, try loading with 'ISO-8859-1' encoding
        return pd.read_csv(filepath, encoding='ISO-8859-1')


def merge_datasets(df1, df2, merge_on):
    return pd.merge(df1, df2, on=merge_on)


def filter_data(df, filter_condition):
    return df.query(filter_condition)


def calculate_group_statistics(df, group_by, stat_column):
    return df.groupby(group_by)[stat_column].mean()


def map_countries_to_hdi_group(hdi_df):
    return dict(zip(hdi_df['Country'], hdi_df['Human Development Groups']))


def plot_data(data_dict, labels, global_data, annotations_df, country_hdi_map, colors):
    fig = go.Figure()

    # Add traces for each HDI group
    for group, data in data_dict.items():
        color_key = f'{group.lower()}_hdi_line'.replace(" ", "_")
        fig.add_trace(go.Scatter(
            x=data.index, y=data.values, mode='lines+markers', name=group,
            line=dict(color=colors[color_key], width=2),
            marker=dict(size=4, color=colors[color_key])
        ))

    # Add global average line
    fig.add_trace(go.Scatter(
        x=global_data.index, y=global_data.values, mode='lines', name='Global Average',
        line=dict(color='grey', dash='dash')
    ))

    # Add annotations if advancements data is provided
    if annotations_df is not None:
        annotation_positions = {}  # To adjust vertical positions of annotations
        for index, row in annotations_df.iterrows():
            hdi_group = country_hdi_map.get(row['Country'])
            if hdi_group and row['Year'] in data_dict[hdi_group].index:
                y_value = data_dict[hdi_group].loc[row['Year']]
                # Adjust annotation position for each year
                if row['Year'] in annotation_positions:
                    annotation_positions[row['Year']] += 80
                else:
                    annotation_positions[row['Year']] = -40

                fig.add_annotation(
                    x=row['Year'], y=y_value, text=row['Advancement'], showarrow=True,
                    arrowhead=2, font=dict(size=10), arrowcolor=colors['advancements_marker'],
                    ax=0, ay=annotation_positions[row['Year']]
                )

    # Set layout
    fig.update_layout(
        title=dict(
            text=labels["title"],
            x=0.5, xanchor='center',
            font=dict(size=20, color=colors['text'])
        ),
        xaxis=dict(
            title='Year',
            showgrid=True,
            gridwidth=1,
            gridcolor=colors['grid'],
            titlefont=dict(size=14, color=colors['text']),
            tickfont=dict(color=colors['text']),
            linecolor=colors['text']
        ),
        yaxis=dict(
            title=labels["yaxis"],
            showgrid=True,
            gridwidth=1,
            gridcolor=colors['grid'],
            titlefont=dict(size=14, color=colors['text']),
            tickfont=dict(color=colors['text']),
            linecolor=colors['text']
        ),
        legend=dict(
            x=0.01, y=0.99,
            borderwidth=1,
            font=dict(size=12, color=colors['text']),
            bgcolor=colors['background']
        ),
        paper_bgcolor=colors['background'],
        plot_bgcolor=colors['background'],
        hovermode='closest',
        margin=dict(l=60, r=60, t=60, b=100)
    )

    return fig


def generate_plot(data_filepath, hdi_filepath, labels, advancements_filepath=None):
    data_df = load_dataset(data_filepath)
    hdi_df = load_dataset(hdi_filepath)
    advancements_df = load_dataset(advancements_filepath) if advancements_filepath else None

    merged_df = merge_datasets(data_df, hdi_df, labels['merge_on'])
    filtered_df = filter_data(merged_df, labels['year_filter'])

    country_hdi_map = map_countries_to_hdi_group(hdi_df)

    data_dict = {
        group: calculate_group_statistics(filtered_df[filtered_df['Human Development Groups'] == group], 'Year',
                                          labels['data_column']) for group in ['Very High', 'High', 'Medium', 'Low']}
    global_avg_data = calculate_group_statistics(filtered_df, 'Year', labels['data_column'])

    colors = {
        'background': '#fcf6ee',
        'text': '#4e545d',
        'very_high_hdi_line': '#508eaf',
        'high_hdi_line': '#76c7c0',
        'medium_hdi_line': '#b6a2c2',
        'low_hdi_line': '#df7793',
        'advancements_marker': '#9467bd',
        'grid': '#555555'
    }

    fig = plot_data(data_dict, labels, global_avg_data, advancements_df, country_hdi_map, colors)
    fig.show()

