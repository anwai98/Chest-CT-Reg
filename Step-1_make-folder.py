# The Step 1 makes the folders for keeping the "elastix outputs"

import os
import sh

list_id = [1, 2, 3, 4, 7, 8, 9, 10]

for val_i in list_id:
 
    id = val_i
    data_directory = "test_nii/copd{}/".format(val_i)
    
    # Providing the path to the output directory
    elastix_directory = data_directory + "elastix_out"

    # Creating the Output Directory for the Registrations
    command = elastix_directory
    index = sh.Command("mkdir")
    index(command.split(" "))

    command = elastix_directory + "/" + "registered_moving"
    index = sh.Command("mkdir")
    index(command.split(" "))

    command = elastix_directory + "/" + "registered_landmarks"
    index = sh.Command("mkdir")
    index(command.split(" "))


