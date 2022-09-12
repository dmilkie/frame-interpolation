import os
import shutil
from pathlib import Path




path_of_the_directory = r'\\nearline4.hhmi.org\betzig\DATA of CSLS_(Lattice Light Sheet Files)\11072012_cell7_HL60_cell moving on coverslip\tiffs'
dst_directory = r'F:\frame_interpolation\tiff'

ext = ('.tif','.tiff')
print(path_of_the_directory)

# list to store files
res = []

for files in os.listdir(path_of_the_directory):
    if files.endswith(ext):
        res.append(files)
    else:
        continue

# now we have all the input files.  Time to make triplets

for i in range(len(res)-2):
    ifolder = '{0:05d}'.format(1)
    iifolder = '{0:04d}'.format(i)

    dfolder = os.path.join(dst_directory, "sequences", ifolder, iifolder)

    Path(dfolder).mkdir(parents=True, exist_ok=True)

    print(" Copying %d out of %d : %s     into    %s" % (i, len(res)-2, res[i], dfolder) )
    shutil.copy2(os.path.join(path_of_the_directory, res[i+0]), os.path.join(dfolder , 'im01.tif')) 
    shutil.copy2(os.path.join(path_of_the_directory, res[i+1]), os.path.join(dfolder , 'im02.tif')) 
    shutil.copy2(os.path.join(path_of_the_directory, res[i+2]), os.path.join(dfolder , 'im03.tif')) 




    