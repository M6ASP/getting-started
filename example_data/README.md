# Test data

The following files are generated with fetch__woa13_sst.py (which was run using python/3.4.5 with netcdf4/1.2.4 and numpy.1.11.0):
- WOA13_annual_SST_nc3_classic.nc
  - The original, most widely understood and default, format (not HDF5).
- WOA13_annual_SST_nc3_64bitoffset.nc
  - Extension to netcdf3 classic to allow files larger than 2Gb (introduced in 3.6.0).
- WOA13_annual_SST_nc3_64bitdata.nc
  - Further extension to allow unsigned 64-bit integers (introduced in 4.4.0 of C library).
- WOA13_annual_SST_nc4_classic.nc
  - Uses HDF5 file format but supports only netcdf3 data structures/APIs.
- WOA13_annual_SST_nc4.nc
  - The current format using HDF5 file format (introduced in 4.0).
