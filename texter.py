
# import numpy as np
# import netCDF4 as nc

# #read in the data
# storLow_richards_2 = nc.Dataset('../data/output/30arcminutes/pcrglobwb_richards_extended/netcdf/storLowTotal_dailyTot_output.nc')
# storUpp_richards_2 = nc.Dataset('../data/output/30arcminutes/pcrglobwb_richards_extended/netcdf/storUppTotal_dailyTot_output.nc')

# storLow_richards_1 = nc.Dataset('../data/output/30arcminutes/pcrglobwb_richards/netcdf/storLowTotal_dailyTot_output.nc')
# storUpp_richards_1 = nc.Dataset('../data/output/30arcminutes/pcrglobwb_richards/netcdf/storUppTotal_dailyTot_output.nc')

# storLow = nc.Dataset('../data/output/30arcminutes/pcrglobwb/netcdf/storLowTotal_dailyTot_output.nc')
# storUpp = nc.Dataset('../data/output/30arcminutes/pcrglobwb/netcdf/storUppTotal_dailyTot_output.nc')


# print(storUpp.dimensions["lat"])

import xarray as xr
import matplotlib.pyplot as plt

ds = xr.open_dataset('output/30arcminutes/pcrglobwb_richards_extended/netcdf/storLowTotal_dailyTot_output.nc')
print(ds.lat.values.min(), ds.lat.values.max(), ds.lon.values.min(), ds.lon.values.max())

cell = ds["lower_soil_storage"].sel(lat=52.10, lon=5.18, method="nearest")
cell.plot()