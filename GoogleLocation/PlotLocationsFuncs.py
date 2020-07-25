import plotly as py
import plotly.graph_objs as go
import json
import matplotlib.pyplot as plt
from datetime import date

# from mapboxgl.utils import *
# from mapboxgl.viz import *
# import pandas as pd

mapbox_access_token = 'pk.eyJ1IjoiZWxpamFoa28iLCJhIjoiY2s4eGdlZ2xqMDFrazNkb2dheGg2OGF5cyJ9.l-FXRkUK91L43HSleBusuw'


def plot_original(longitudes, latitudes):
    plt.plot(longitudes, latitudes, linewidth=0.08, marker='.', markersize=1.75)
    plt.ylabel('latitude')
    plt.xlabel('longitude')
    plt.show()


def plot_scattergeo(longitudes, latitudes, name):
    trace = [
        dict(type='scattergeo',
             lon=longitudes,
             lat=latitudes,
             mode='lines+markers',
             line=dict(
                 width=0.5,
                 color='red',
             ),
             marker=dict(
                 size=2,
                 color='blue',
             ),
             )
    ]
    lyt = dict(
        geo=dict(
            resolution=50,
            lonaxis=dict(showgrid=True),
            # showland=True,
            # showocean=True,
            showcountries=True,
            # projection = dict(type='aitoff')
            projection=dict(scale=1)
        ),
    )
    my_map = go.Figure(data=trace, layout=lyt)
    py.offline.plot(my_map, filename=name + 'geo.html')


def plot_scattermapbox(longitudes, latitudes, name, zoom):
    data = [
        go.Scattermapbox(
            lon=longitudes,
            lat=latitudes,
            mode='lines+markers',
            marker=dict(
                size=3,
                color='blue',
            ),
            line=dict(
                width=1,
                color='red',
            ),
            opacity=0.4
        )
    ]
    layout = go.Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=51.5074,
                lon=-0.1278
            ),
            pitch=0,
            zoom=zoom,
            style='light'
        ),
    )
    fig = dict(data=data, layout=layout)
    py.offline.plot(fig, validate=True, filename=name + 'mapbox.html')


def getJsonData(fileName):
    file = open(fileName)
    datastore = json.load(file)
    loc_array = datastore.get('locations')
    return loc_array


def isLocValid(loc_point,
               show_all_days=True,
               valid_day_of_week=1,
               show_full_range=True,
               min_lat_range=40.495992,
               max_lat_range=40.915568,
               min_lon_range=-74.257159,
               max_lon_range=-73.699215,
               include_traveling=True,
               include_stationary=True
               ):
    if (not show_all_days) and date.isoweekday(
            date.fromtimestamp(int(loc_point.get('timestampMs')) / 1000)) != valid_day_of_week:
        return False
    lat = loc_point.get('latitudeE7') * 1e-7
    lon = loc_point.get('longitudeE7') * 1e-7
    if (not show_full_range) and (not (min_lat_range < lat < max_lat_range and min_lon_range < lon < max_lon_range)):
        return False
    velocity = loc_point.get('velocity')
    is_traveling = type(velocity) is int and velocity > 0
    if is_traveling and not include_traveling:
        return False
    if (not is_traveling) and not include_stationary:
        return False
    return True


def velocity_calc(loc_point):
    velocity = loc_point.get('velocity')
    if type(velocity) is not int:
        return "none"
    return velocity


def getLatLonFromJson(loc_array,
                      show_all_days=True,
                      valid_day_of_week=1,
                      max_range=1000000,
                      show_full_range=True,
                      min_lat_range=40.495992,
                      max_lat_range=40.915568,
                      min_lon_range=-74.257159,
                      max_lon_range=-73.699215,
                      include_traveling=True,
                      include_stationary=True
                      ):
    latitudes = []
    longitudes = []

    for i in range(0, min(len(loc_array), max_range)):
        if isLocValid(
                loc_array[i],
                show_all_days=show_all_days,
                valid_day_of_week=valid_day_of_week,
                show_full_range=show_full_range,
                min_lat_range=min_lat_range,
                max_lat_range=max_lat_range,
                min_lon_range=min_lon_range,
                max_lon_range=max_lon_range,
                include_traveling=include_traveling,
                include_stationary=include_stationary,
        ):
            lat = loc_array[i].get('latitudeE7') * 1e-7
            lon = loc_array[i].get('longitudeE7') * 1e-7
            latitudes.append(lat)
            longitudes.append(lon)
    return [latitudes, longitudes]


def plot_locs(loc_array, thisConfig, show_all_days=True, include_traveling=True, include_stationary=True):
    max_range = 1000000
    show_full_range = True

    if show_all_days:
        [latitudes, longitudes] = getLatLonFromJson(loc_array,
                                                    show_all_days,
                                                    include_traveling=include_traveling,
                                                    include_stationary=include_stationary
                                                    )

        plot_scattermapbox(longitudes, latitudes, thisConfig['name'], thisConfig['zoom'])
        # plot_scattergeo(longitudes,latitudes,thisConfig['name'])
        # plot_original(longitudes,latitudes)

        # viz = CircleViz(thisConfig['file'], access_token=mapbox_access_token, radius=2, center=(-95, 40), zoom=3)
        # viz.show()
    else:
        for i in range(1, 8):
            [latitudes, longitudes] = getLatLonFromJson(loc_array, show_all_days, i, max_range, show_full_range)

            plot_scattermapbox(longitudes, latitudes, thisConfig['name'] + str(i), thisConfig['zoom'])


def plotdata(whichdata, fileNum, show_all_days=True, include_traveling=True, include_stationary=True):
    configs = {
        'photos': {
            'name': 'photos',
            'file': 'PhotoData.json',
            'zoom': 3
        },
        'photos2': {
            'name': 'photos2',
            'file': 'PhotoData2.json',
            'zoom': 3
        },
        'locations': {
            'name': 'locations',
            'file': '/Users/elijahko/PycharmProjects/GoogleLocation/Takeout20200412/Location History/Location History.json', #Location History.json
            'zoom': 10
        }
    }

    this_Config = configs[whichdata]
    file_Name = this_Config['file']

    loc_array = getJsonData(file_Name)

    #    [latitudes,longitudes] = getLatLonFromJson(loc_array, show_all_days)
    plot_locs(loc_array, this_Config, show_all_days, include_traveling, include_stationary)
