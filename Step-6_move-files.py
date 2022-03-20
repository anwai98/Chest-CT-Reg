# This Step 6 moves the files upfront for our convenience.
import os
import shutil

list_id = [1, 2, 3, 4, 7, 8, 9, 10]


for val_i in list_id:
 
    id = val_i
    data_directory = "test_nii/copd{}/".format(val_i)
    
    # Directing the Path to our Registered Image
    result_file = data_directory + "elastix_out/registered_moving/result.nii.gz"
    move_to = data_directory + "reg_copd{}_eBHCT.nii.gz".format(val_i)
    
    shutil.move(result_file, move_to)

