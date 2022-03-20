# This Step 9 makes the TRE Calculation.

import os
import sh
import numpy as np
import nibabel as nib

list_id = [1, 2, 3, 4, 7, 8, 9, 10]

for val_i in list_id:

  id = str(val_i)
  #print("\nWorking on copd - "+id+" ...")

  # Directory containing the COPD Folers
  data_directory = "test_nii/copd{0}/".format(id)
  
  # The Inhale Image Directory
  inhale_image = data_directory + 'copd' + id + '_iBHCT.nii.gz'

  # Landmark Point Files of the Inhale and Exhale images
  inhale_points = data_directory + 'copd' + id + '_reg_transformed_points.txt'
  exhale_points = data_directory + 'copd' + id + '_300_eBH_xyz_r1.txt'

  moving_points = np.loadtxt(exhale_points)
  fixed_points = np.loadtxt(inhale_points)

  # Voxel Spacing of the Inhale Image
  voxel_spacing = nib.load(inhale_image).header.get_zooms()
  
  # Voxel Size of the COPD Instance
  moving_points = voxel_spacing * moving_points
  fixed_points  = voxel_spacing * fixed_points

  # Squared Difference - Euclidean Distance
  tre = np.sqrt(np.sum((fixed_points - moving_points) ** 2,axis =1))

  # Mean and Standard Deviation of the TRE after Registration
  mean_tre = np.mean(tre)
  std_tre = np.std(tre)

  print('COPD{0} & {1:.2f} ({2:.2f}) \\\\ \hline'.format(id, mean_tre , std_tre))