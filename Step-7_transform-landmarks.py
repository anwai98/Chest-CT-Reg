# This Step 7 extracts the landmark points from the output points file 

import os
import pandas as pd
import numpy as np
import re

def extract_landmarks (filepath):

    new_landmarks = np.zeros((300, 3))
    current_landmark_file = open(filepath, "r")
    reg_ex = r'OutputIndexFixed = \[([\d.\s\-]+)\]'

    for i, line in enumerate(current_landmark_file):
        
        match_found = re.search(reg_ex, line, re.M)
        j = match_found.group(1).split()
        j = [round(float(c)) for c in j]
        new_landmarks[i,:] = j
        
    return new_landmarks

list_id = [1, 2, 3, 4, 7, 8, 9, 10]

for val_i in list_id:
    
    id = val_i
    
    output_name = "test_nii/copd{}/copd{}_reg_transformed_points.txt".format(val_i,val_i)
    data_directory = "test_nii/copd{}/".format(val_i)
    result_directory = data_directory + "elastix_out"

    # Ouput points after transformation
    output_point_path = result_directory + "/registered_landmarks" + "/outputpoints.txt"
    
    # Extracting only the landmark points and saving it
    transformed_landmarks = extract_landmarks(output_point_path)
    np.savetxt("{}".format(output_name), transformed_landmarks)