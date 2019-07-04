import pandas as pd
import numpy as np
import plotly.plotly as py

data = pd.read_csv('data/pollution_us_2000_2016.csv', encoding='utf8', engine='python')
data = data.drop(data.columns[0], axis=1)

groupedDataNO2 = data.groupby('State', as_index=False).agg({"NO2 Mean": "mean"})
groupedDataSO2 = data.groupby('State', as_index=False).agg({"SO2 Mean": "mean"})
groupedDataCO = data.groupby('State', as_index=False).agg({"CO Mean": "mean"})
groupedDataNO2['text'] = groupedDataNO2['State'] + ' NO2 mean '+ groupedDataNO2['NO2 Mean'].astype(str)
groupedDataSO2['text'] = groupedDataSO2['State'] + ' SO2 mean '+ groupedDataSO2['SO2 Mean'].astype(str)
groupedDataCO['text'] = groupedDataCO['State'] + ' CO mean '+ groupedDataCO['CO Mean'].astype(str)

code = ['AL','AK','AZ','AR','CA','CO','CT','MS','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MO','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VA','WA','WI','WY']
groupedDataNO2['code'] = code
groupedDataSO2['code'] = code
groupedDataCO['code'] = code

scl = [[0.0, 'rgb(142,240,247)'], [0.2, 'rgb(140,218,235)'], [0.4, 'rgb(138,189,220)'], [0.6, 'rgb(130,154,200)'],
       [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(100,39,143)']]
dataNO2 = [dict(
    type='choropleth',
    colorscale=scl,
    autocolorscale=False,
    locations=groupedDataNO2['code'],
    z=groupedDataNO2['NO2 Mean'].astype(float),
    locationmode='USA-states',
    text=groupedDataNO2['text'],
    marker=dict(
        line=dict(
            color='rgb(255,255,255)',
            width=2
        )),
    colorbar=dict(
        title="Millions USD")
)]

layoutNO2 = dict(
    title='NO2 mean for each and every state',
    geo=dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showlakes=True,
        lakecolor='rgb(255, 255, 255)'),
)

fig = dict(data=dataNO2, layout=layoutNO2)
py.iplot(fig, filename='d3-cloropleth-map')

scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'], [0.6, 'rgb(158,154,200)'],
       [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]
dataSO2 = [dict(
    type='choropleth',
    colorscale=scl,
    autocolorscale=False,
    locations=groupedDataSO2['code'],
    z=groupedDataSO2['SO2 Mean'].astype(float),
    locationmode='USA-states',
    text=groupedDataSO2['text'],
    marker=dict(
        line=dict(
            color='rgb(255,255,255)',
            width=2
        )),
    colorbar=dict(
        title="Millions USD")
)]

layoutSO2 = dict(
    title='SO2 mean for each and every state',
    geo=dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showlakes=True,
        lakecolor='rgb(255, 255, 255)'),
)

fig = dict(data=dataSO2, layout=layoutSO2)
py.iplot(fig, filename='d3-cloropleth-map')

date = pd.to_datetime(data['Date Local'])
year = date.dt.year
dfYearNO2Mean = pd.DataFrame()
dfYearSO2Mean = pd.DataFrame()
dfYearCOMean = pd.DataFrame()
dfYearNO2Mean['year'] = year
dfYearNO2Mean['NO2 mean'] = data['NO2 Mean']
dfYearSO2Mean['year'] = year
dfYearSO2Mean['SO2 mean'] = data['SO2 Mean']
dfYearCOMean['year'] = year
dfYearCOMean['CO mean'] = data['CO Mean']
groupedYearNO2 = dfYearNO2Mean.groupby('year', as_index=False).agg({"NO2 mean": "mean"})
groupedYearSO2 = dfYearSO2Mean.groupby('year', as_index=False).agg({"SO2 mean": "mean"})
groupedYearCO = dfYearCOMean.groupby('year', as_index=False).agg({"CO mean": "mean"})

scl = [[0.0, 'rgb(242,240,47)'], [0.2, 'rgb(218,218,35)'], [0.4, 'rgb(188,189,20)'], [0.6, 'rgb(158,154,18)'],
       [0.8, 'rgb(117,107,15)'], [1.0, 'rgb(84,39,10)']]
dataCO = [dict(
    type='choropleth',
    colorscale=scl,
    autocolorscale=False,
    locations=groupedDataCO['code'],
    z=groupedDataCO['CO Mean'].astype(float),
    locationmode='USA-states',
    text=groupedDataCO['text'],
    marker=dict(
        line=dict(
            color='rgb(255,255,255)',
            width=2
        )),
    colorbar=dict(
        title="Millions USD")
)]

layoutCO = dict(
    title='CO mean for each and every state',
    geo=dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showlakes=True,
        lakecolor='rgb(255, 255, 255)'),
)

fig = dict(data=dataCO, layout=layoutCO)
py.iplot(fig, filename='d3-cloropleth-map')

import plotly.graph_objs as go
scatterDataNO2 = go.Scatter(x=groupedYearNO2['year'],y=groupedYearNO2['NO2 mean'])
scatterDataNO2=go.Scatter([scatterDataNO2])
layoutDataNO2=go.Layout(title="Plot of mean NO2 trace vs year", xaxis={'title':'year'}, yaxis={'title':'Mean of NO2'})
figure=go.Figure(data=scatterDataNO2,layout=layoutDataNO2)
py.iplot(figure, filename='time-series')

scatterDataSO2 = go.Scatter(x=groupedYearSO2['year'],y=groupedYearSO2['SO2 mean'])
scatterDataSO2=go.Scatter([scatterDataSO2])
layoutDataSO2=go.Layout(title="Plot of mean SO2 trace vs year", xaxis={'title':'year'}, yaxis={'title':'Mean of SO2'})
figure2=go.Figure(data=scatterDataSO2,layout=layoutDataSO2)
py.iplot(figure2, filename='time-series')

scatterDataCO = go.Scatter(x=groupedYearCO['year'],y=groupedYearCO['CO mean'])
scatterDataCO=go.Scatter([scatterDataCO])
layoutDataCO=go.Layout(title="Plot of mean CO trace vs year", xaxis={'title':'year'}, yaxis={'title':'Mean of CO'})
figure3=go.Figure(data=scatterDataCO,layout=layoutDataCO)
py.iplot(figure3, filename='time-series')
#py.iplot(scatterDataCO, filename='time-series')