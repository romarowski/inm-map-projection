import pandas as pd
from modules import lat_lon_to_meter
import numpy as np

data = pd.read_csv('jaipur.csv', sep=';')

origin = np.array([26.8242, 75.812202]) # Lat, Lon

parameters = lat_lon_to_meter.parameters(origin)
project = lat_lon_to_meter.project

data['x (m)'], data['y (m)'] = zip(*data[['Lat', 'Lon']].apply(project, 
                                  axis = 1,
                                  parameters = parameters,
                                  ))

data_xy = data[['Lat', 'Lon']].apply(project, 
                                  axis = 1,
                                  parameters = parameters,
                                  )

data.to_csv('jaipur_w_projection.csv', index = False, sep = ';')

