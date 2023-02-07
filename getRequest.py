import pandas as pd

afad_pd_param = pd.read_csv('afad_dataFile.csv', usecols=[
    'id', 'date',
    'timestamp',
    'latitude', 'longitude',
    'depth',
    'size',
    'location',
    'attribute',
])
kandilli_pd_param = pd.read_csv('kandilli_dataFile.csv', usecols=[
    'id', 'date',
    'timestamp',
    'latitude', 'longitude',
    'depth',
    'size',
    'location',
    'attribute',
])

earthquake_pd_param = pd.read_csv('earthquake_final.csv')

adana_pd_param = pd.read_csv('adana_dataFile.csv', usecols=[
    'id', 'date',
    'timestamp',
    'latitude', 'longitude',
    'depth',
    'size',
    'location',
    'attribute',
])

kahramanM_pd_param = pd.read_csv('kahramanM_dataFile.csv', usecols=[
    'id', 'date',
    'timestamp',
    'latitude', 'longitude',
    'depth',
    'size',
    'location',
    'attribute',
])

hatay_pd_param = pd.read_csv('hatay_dataFile.csv', usecols=[
    'id', 'date',
    'timestamp',
    'latitude', 'longitude',
    'depth',
    'size',
    'location',
    'attribute',
])
