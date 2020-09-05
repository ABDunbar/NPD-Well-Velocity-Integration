# VelMod
This program with take checkshot data and sonic logs from Petrel export and formation tops from npd.no and merge them.

The resulting output will be in a form so that interval sonic logs and interval velocities from the checkshot can be compared.

WORKING.ipynb : (using Tops files) is basically complete.  It will pull tops data from npd.no website and combine them with tops exported from a Petrel project.  Adds isochron and interval velocity columns.

def_tops.ipynb : functional version of WORKING.ipynb (in progress)

las.py : program written by Warren Weckesser to load las files into Python

load_checkshot_file.ipynb : work in progress

load_multiple_sonic.ipynb : work in progress

m172.ipynb :  In progress version of the M172 Velocity Modeling training course (Alan Atkinson)

sonic_las_files_edit.ipynb : (in progress) uses las.py to load sonic logs.  Uses depth and sonic, calculates velocity, one-way-time
