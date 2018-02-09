import netCDF4
import numpy

def data_url(period):
  """Returns url to OpenDAP data corresponding to WOA13 5-degree ocean temperature for given period"""
  return 'https://data.nodc.noaa.gov/thredds/dodsC/woa/WOA13/DATAv2/temperature/netcdf/decav/1.00/woa13_decav_t%2.2i_01v2.nc'%(period)

def create_local_file(file_name, form, nc):
  """Creates local file "file_name" and places SST data from nc in it."""
  new_file = netCDF4.Dataset(file_name, 'w', format=form)
  # Copy global attributes
  for a in nc.ncattrs():
    new_file.setncattr(a, nc.getncattr(a))
  new_file.title = nc.title.replace('sea_water_temperature', 'sea_surface_temperature')
  # Create dimensions
  for d in nc.dimensions:
    if not d == 'time':
      new_file.createDimension(d, nc.dimensions[d].size)
  # Define corresponding variables
  for v in ('lat', 'lon'):
    vv = new_file.createVariable(v, nc.variables[v].dtype, nc.variables[v].dimensions)
    for a in nc.variables[v].ncattrs():
      vv.setncattr(a, nc.variables[v].getncattr(a))
  # Create SST from t_mn[0]
  v = 't_an'
  vv = new_file.createVariable('tos', nc.variables[v].dtype, ('lat', 'lon',))
  for a in nc.variables[v].ncattrs():
    vv.setncattr(a, nc.variables[v].getncattr(a))
  vv.standard_name = vv.standard_name.replace('sea_water_temperature', 'sea_surface_temperature')
  vv.long_name = vv.long_name.replace('sea_water_temperature', 'sea_surface_temperature')
  # Copy coordinate data
  for d in ('lat', 'lon'):
    new_file.variables[d][:] = nc.variables[d][:]
  # Write data
  vv[:] = nc.variables[v][0,0]
  new_file.close();

# Open 1-degree annual average data via OpenDAP
nc = netCDF4.Dataset(data_url(0))
# Create a file using each netcdf format
create_local_file('WOA13_annual_SST_nc3_classic.nc', 'NETCDF3_CLASSIC', nc)
#create_local_file('WOA13_annual_SST_nc3_64bitoffset.nc', 'NETCDF3_64BIT_OFFSET', nc)
#create_local_file('WOA13_annual_SST_nc3_64bitdata.nc', 'NETCDF3_64BIT_DATA', nc)
#create_local_file('WOA13_annual_SST_nc4_classic.nc', 'NETCDF4_CLASSIC', nc)
#create_local_file('WOA13_annual_SST_nc4.nc', 'NETCDF4', nc)
