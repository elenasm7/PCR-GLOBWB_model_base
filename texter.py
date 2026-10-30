
# import numpy as np
# import netCDF4 as nc
#%%
import xarray as xr
import matplotlib.pyplot as plt
# #read in the data
storLow_richards_2 = xr.open_dataset('../data/output/30arcminutes/pcrglobwb_richards_extended/netcdf/storLowTotal_dailyTot_output.nc')
storUpp_richards_2 = xr.open_dataset('../data/output/30arcminutes/pcrglobwb_richards_extended/netcdf/storUppTotal_dailyTot_output.nc')
print(storLow_richards_2.lat.values.min(), storLow_richards_2.lat.values.max(), 
      storLow_richards_2.lon.values.min(), storLow_richards_2.lon.values.max())


#storLow_richards_1 = xr.open_dataset('../data/output/30arcminutes/pcrglobwb_richards/netcdf/storLowTotal_dailyTot_output.nc')
#storUpp_richards_1 = xr.open_dataset('../data/output/30arcminutes/pcrglobwb_richards/netcdf/storUppTotal_dailyTot_output.nc')
#print(storLow_richards_1.lat.values.min(), storLow_richards_1.lat.values.max(), 
      #storLow_richards_1.lon.values.min(), storLow_richards_1.lon.values.max())


storLow = xr.open_dataset('../data/output/30arcminutes/pcrglobwb/netcdf/storLowTotal_dailyTot_output.nc')
storUpp = xr.open_dataset('../data/output/30arcminutes/pcrglobwb/netcdf/storUppTotal_dailyTot_output.nc')
print(storLow.lat.values.min(), storLow.lat.values.max(), 
      storLow.lon.values.min(), storLow.lon.values.max())

# print(storUpp.dimensions["lat"])

point = dict(lat=52.10, lon=5.18, method="nearest")

fig, ax = plt.subplots(figsize=(9, 5))

# upper layer
storUpp_richards_2["upper_soil_storage"].sel(**point).plot(ax=ax, label="Upper - Richards (run 2)")
# storUpp_richards_1["upper_soil_storage"].sel(**point).plot(ax=ax, label="Upper - Richards (run 1)")
storUpp["upper_soil_storage"].sel(**point).plot(ax=ax, label="Upper - original")

# lower layer
storLow_richards_2["lower_soil_storage"].sel(**point).plot(ax=ax, linestyle="--", label="Lower - Richards (run 2)")
# storLow_richards_1["lower_soil_storage"].sel(**point).plot(ax=ax, linestyle="--", label="Lower - Richards (run 1)")
storLow["lower_soil_storage"].sel(**point).plot(ax=ax, linestyle="--", label="Lower - original")

ax.set_ylabel("Soil storage [m]")
ax.set_title("Soil storage at the selected cell")
ax.legend()
plt.show()



print(ds.time.values.min(), ds.time.values.max())

#2022-01-01T00:00:00.000000000 2022-01-30T00:00:00.000000000
# %%
import xarray as xr
import matplotlib.pyplot as plt
# #read in the data
storLow_richards_3 = xr.open_dataset('../data/output/30arcminutes/pcrglobwb_richards_extended_longer/netcdf/storLowTotal_dailyTot_output.nc')
storUpp_richards_3 = xr.open_dataset('../data/output/30arcminutes/pcrglobwb_richards_extended_longer/netcdf/storUppTotal_dailyTot_output.nc')
#print(storLow_richards_2.lat.values.min(), storLow_richards_2.lat.values.max(), 
#      storLow_richards_2.lon.values.min(), storLow_richards_2.lon.values.max())


#storLow_richards_1 = xr.open_dataset('../data/output/30arcminutes/pcrglobwb_richards/netcdf/storLowTotal_dailyTot_output.nc')
#storUpp_richards_1 = xr.open_dataset('../data/output/30arcminutes/pcrglobwb_richards/netcdf/storUppTotal_dailyTot_output.nc')
#print(storLow_richards_1.lat.values.min(), storLow_richards_1.lat.values.max(), 
      #storLow_richards_1.lon.values.min(), storLow_richards_1.lon.values.max())


#storLow = xr.open_dataset('../data/output/30arcminutes/pcrglobwb/netcdf/storLowTotal_dailyTot_output.nc')
#storUpp = xr.open_dataset('../data/output/30arcminutes/pcrglobwb/netcdf/storUppTotal_dailyTot_output.nc')
#print(storLow.lat.values.min(), storLow.lat.values.max(), 
#      storLow.lon.values.min(), storLow.lon.values.max())

# print(storUpp.dimensions["lat"])

point = dict(lat=52.10, lon=5.18, method="nearest")

fig, ax = plt.subplots(figsize=(9, 5))

# upper layer
storUpp_richards_3["upper_soil_storage"].sel(**point).plot(ax=ax, label="Upper - Richards (run 2)")
# storUpp_richards_1["upper_soil_storage"].sel(**point).plot(ax=ax, label="Upper - Richards (run 1)")
#storUpp["upper_soil_storage"].sel(**point).plot(ax=ax, label="Upper - original")

# lower layer
storLow_richards_3["lower_soil_storage"].sel(**point).plot(ax=ax, linestyle="--", label="Lower - Richards (run 2)")
# storLow_richards_1["lower_soil_storage"].sel(**point).plot(ax=ax, linestyle="--", label="Lower - Richards (run 1)")
#storLow["lower_soil_storage"].sel(**point).plot(ax=ax, linestyle="--", label="Lower - original")

ax.set_ylabel("Soil storage [m]")
ax.set_title("Soil storage at the selected cell")
ax.legend()
plt.show()



print(storLow_richards_3.time.values.min(), storLow_richards_3.time.values.max())
# %%
