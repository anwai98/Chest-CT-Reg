# This Step 4 adds the 300 number in the top of the landmark file as we have 300 landmark points

import os
import shutil

list_id = [1, 2, 3, 4, 7, 8, 9, 10]


for val_i in list_id:
 
    id = val_i
    
    r1_file = "test_nii/copd{}/copd{}_300_eBH_xyz_r1.txt".format(val_i,val_i)
    r2_file = "test_nii/copd{}/copd{}_300_eBH_xyz_r2.txt".format(val_i,val_i)
    
    with open(r2_file,'a') as secondfile:
        secondfile.write("300\n")

    # open both files
    with open(r1_file,'r') as firstfile, open(r2_file,'a') as secondfile:
      
        # read content from first file
        for line in firstfile:
               
                 # write content to second file
                 secondfile.write(line)
                 
                 
    r1_file = "test_nii/copd{}/copd{}_300_iBH_xyz_r1.txt".format(val_i,val_i)
    r2_file = "test_nii/copd{}/copd{}_300_iBH_xyz_r2.txt".format(val_i,val_i)
    
    with open(r2_file,'a') as secondfile:
        secondfile.write("300\n")

    # open both files
    with open(r1_file,'r') as firstfile, open(r2_file,'a') as secondfile:
      
        # read content from first file
        for line in firstfile:
               
                 # write content to second file
                 secondfile.write(line)

