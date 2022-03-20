# The Step 2 file creates the segmentation masks for the elastix

import os
import sh
import pandas as pd
import numpy as np
import nibabel as nib
from scipy import ndimage
from skimage import measure
from scipy import stats
import cv2
import re

def morphological_segment(image_path):

    # Loading the Lung Image
    image = nib.load(image_path)
    image_data = image.get_fdata()

    # Intensity Thresholding & Morphological Operations
    temp = np.zeros(image_data.shape)
    temp[image_data > 0] = 1
    temp[image_data > 800] = 0

    str_el1 = ndimage.generate_binary_structure(3, 1)
    str_el2 = ndimage.iterate_structure(str_el1, 2)
    # str_el3 = ndimage.iterate_structure(str_el1, 3)
    temp = ndimage.binary_closing(temp, structure=str_el1, iterations=1)
    temp = ndimage.binary_opening(temp, structure=str_el2, iterations=1)

    # The Lung View Estimation
    [a, b, c] = image_data.shape
    
    # Selecting our cross-section of Connected Components 
    x_val = int(a / 2)
    y_val = int(b / 2)
    x_band1 = int(a / 2 * 0.4)
    x_band2 = int(a / 2 * 0.75)
    z_band1 = int(c * 0.5)
    z_band2 = int(c * 0.75)

    # Selecting the Largest Connected Components in the Lung Volume
    temp = measure.label(temp)
    label1 = temp[x_val - x_band2: x_val - x_band1, y_val, z_band1: z_band2]
    label2 = temp[x_val + x_band1: x_val + x_band2, y_val, z_band1: z_band2]
    label1 = stats.mode(label1[label1 > 0])[0][0]
    label2 = stats.mode(label2[label2 > 0])[0][0]
    temp[temp == label1] = -1
    temp[temp == label2] = -1
    temp[temp > 0] = 0
    temp = temp * -1

    segmented_lung = nib.Nifti1Image(temp, image.affine, image.header)

    return segmented_lung # Obtaining our Segmented Image

# The number of the COPD Patients in the provided dataset 
list_id = [1, 2, 3, 4, 7, 8, 9, 10]

for val_i in list_id:

    print("Working on copd",val_i," ...")
    id = val_i
    data_directory = "test_nii/copd{}/".format(val_i)
    
    # Providing the Image Directory for Segmentation
    exhale_path = data_directory + 'copd' + str(id) + '_eBHCT.nii.gz'
    inhale_path = data_directory + 'copd' + str(id) + '_iBHCT.nii.gz'
 
    # Obtaining the Segmented Lung Volumes for Inhale and Exhale Pairs
    exhale_seg = morphological_segment(exhale_path)
    segmented_exhale_path = "{}seg_copd{}_eBHCT.nii.gz".format(data_directory, id)
    nib.save(exhale_seg, segmented_exhale_path)
    
    inhale_seg = morphological_segment(inhale_path)
    segmented_inhale_path = "{}seg_copd{}_iBHCT.nii.gz".format(data_directory, id)
    nib.save(inhale_seg, segmented_inhale_path)

