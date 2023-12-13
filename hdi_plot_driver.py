from hdi_grouped_grapher import generate_plot

# task 1
generate_plot(
    'task1_datasets/CO2 emission by countries.csv',
    'Human Development Index - Full.csv',
    {
        'title': 'CO2 Emissions and Technological Milestones by HDI Group (1930 Onwards)',
        'yaxis': 'Average CO2 Emissions (Tons)',
        'merge_on': 'Country',
        'year_filter': 'Year >= 1930',
        'data_column': 'CO2 emission (Tons)'
    },
    'task1_datasets/Advancements.csv')

# task 2
generate_plot(
    'task2_datasets/broadband-penetration-by-country.csv',
    'Human Development Index - Full.csv',
    {
        'title': 'Broadband Subscriptions by HDI Group (1990 Onwards)',
        'yaxis': 'Average Fixed Broadband Subscriptions (per 100 people)',
        'merge_on': 'Country',
        'year_filter': 'Year >= 1990',
        'data_column': 'Fixed broadband subscriptions (per 100 people)'
    }
)

generate_plot(
    'task2_datasets/mobile-cellular-subscriptions-per-100-people.csv',
    'Human Development Index - Full.csv',
    {
        'title': 'Mobile Cellular Subscriptions by HDI Group (1990 Onwards)',
        'yaxis': 'Average Mobile Cellular Subscriptions (per 100 people)',
        'merge_on': 'Country',
        'year_filter': 'Year >= 1990',
        'data_column': 'Mobile cellular subscriptions (per 100 people)'
    }
)

generate_plot(
    'task2_datasets/number-of-internet-users-by-country.csv',
    'Human Development Index - Full.csv',
    {
        'title': 'Number of Internet Users by HDI Group (1990 Onwards)',
        'yaxis': 'Average Number of internet users (OWID based on WB & UN)',
        'merge_on': 'Country',
        'year_filter': 'Year >= 1990',
        'data_column': 'Number of internet users (OWID based on WB & UN)'
    }
)

generate_plot(
    'task2_datasets/share-of-individuals-using-the-internet.csv',
    'Human Development Index - Full.csv',
    {
        'title': 'Mobile Cellular Subscriptions by HDI Group (1990 Onwards)',
        'yaxis': 'Average Individuals using the Internet (% of population)',
        'merge_on': 'Country',
        'year_filter': 'Year >= 1990',
        'data_column': 'Individuals using the Internet (% of population)'
    }
)

# task 3

generate_plot(
    'task3_datasets/AI_index_db.csv',
    'Human Development Index - Full.csv',
    {
        'title': 'AI Index by HDI Group (1990 Onwards)',
        'yaxis': 'Average Individuals using the Internet (% of population)',
        'merge_on': 'Country',
        'year_filter': 'Year >= 1990',
        'data_column': 'Individuals using the Internet (% of population)'
    }
)

