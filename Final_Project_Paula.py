# -*- coding: utf-8 -*-
"""
Name:           .py
Compatibility:  Python 3.5
Description:    



Requires:       

Dev ToDo:

AUTHOR:         Paula Carvalho de Castro
ORGANIZATION:   University of Northern Iowa
Contact:        carvalhp@uni.edu
"""


"""
            Data Input and Preliminary Visualization Code.
            
 Obs: Only first part of the code was commented because the second part is
      exaclty the same but done for the corridor number 2.            

"""
# Dependencies: libraries that are going to be used in the project

import os

import imageio

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

import seaborn as sns

#%%

# Setting the images directory

img_dir = 'C:/Users/carvalhp/Desktop/EDA/Final Project/images/'

# Calling and setting a variable to the 1st image
#1_60 refers to Corridor 1 60m wide buffer 

img1_60 =  imageio.imread(img_dir + 'corr_1_60_current.tif')

# Accessing the information from each image in order to assess the area that 
# was converted from one land use type into forest

# Using frequencies to stablish the amount of pixels of each land use type

(unique, counts) = np.unique(img1_60, return_counts=True)
frequencies1_60 = np.asarray((unique, counts)).T

#Accessing each pixel type frequency and multiplying by the size of the pixel
#Then dividing it by 10 000 to have the result in Ha.

#ArcGIS stablishes the same position in the attribute table for each land use
# type in all the images that were classified. 
# this is the reason why it is possible to access the position of the 
# Croplands, Pastures and Exposed soil in the table corresponding to 
# each image in the same way

# Because of the method of classification, I'm assuming a pixel size of around 
# 22.5 meters x 22.5 meters
# This is because of the vectorization of classes and then reconversion to raster
# This conversion caused some pixels to be cut to a size smaller than the
# 30m x 30m.
# I have tested a variety of pixel sizes and multplying by 500 m is what came
#closest to reality. (I verified with data from ArcGIS processing)

agri_for_1_60 = (frequencies1_60[1,1]*500) / 10000
pasture_for_1_60 = (frequencies1_60[5,1]*500) / 10000
exp_soil_for_1_60 = (frequencies1_60[3,1]*500) / 10000
or_forest_1_60 = (frequencies1_60[4,1]*500) / 10000


img1_90 =  imageio.imread(img_dir + 'corr_1_90_current.tif')


(unique2, counts2) = np.unique(img1_90, return_counts=True)
frequencies1_90 = np.asarray((unique2, counts2)).T

agri_for_1_90 = (frequencies1_90[1,1]*500) / 10000
pasture_for_1_90 = (frequencies1_90[5,1]*500) / 10000
exp_soil_for_1_90 = (frequencies1_90[3,1]*500) / 10000
or_forest_1_90 = (frequencies1_90[4,1]*500) / 10000


img1_120 =  imageio.imread(img_dir + 'corr_1_120_current.tif')


(unique3, counts3) = np.unique(img1_120, return_counts=True)
frequencies1_120 = np.asarray((unique3, counts3)).T

agri_for_1_120 = (frequencies1_120[1,1]*500) / 10000
pasture_for_1_120 = (frequencies1_120[5,1]*500) / 10000
exp_soil_for_1_120 = (frequencies1_120[3,1]*500) / 10000
or_forest_1_120 = (frequencies1_120[4,1]*500) / 10000

#Goruping all land use types results from the 60, 90 and 120 m wide corridors.

results_agri = (agri_for_1_60, agri_for_1_90, agri_for_1_120)
results_pature =(pasture_for_1_60,pasture_for_1_90,pasture_for_1_120)
results_exp_soil = (exp_soil_for_1_60, exp_soil_for_1_90, exp_soil_for_1_120)
results_forest = (or_forest_1_60,or_forest_1_90, or_forest_1_120)


# Setting the scenarios to be used in the visualization part (x axis)

scenarios = (60,90,120)
x = scenarios

# Setting the y variable for the visualization part

y_agri_1 = results_agri
y_past_1 = results_pature
y_exp_s_1 = results_exp_soil
y_forest_1 = results_forest

# Setting up a preliminary visualization for the results of the analysed images

f1 = plt.figure()

# Setting the limits 

plt.xlim(50,130)
plt.ylim(0,350)

# Plotting each land use type

plt.plot(x,y_agri_1, 'b--x', label = "Croplands Restored")
plt.plot(x,y_past_1,'r--x', label = "Pasturelands Restored")
plt.plot(x,y_exp_s_1, 'y--x', label = "Exposed soil Restored")
plt.plot(x,y_forest_1, 'g-x', label = "Original Forest Maintained")

# Adding  legend and labels
plt.legend(loc='upper left')
plt.xlabel("Corridor Width (Meters)")
plt.ylabel("Reforested Area (Hectares)")
plt.title('Corridor 1')

#Adding a grid for better visualization
plt.grid()

#%%
#Visualization - 2



sns.set(style="white", context="talk")


# Set up the matplotlib figure
f2, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7, 5), sharex=True)

# Generate some sequential data

x = [60,90,120]
y1 = y_past_1
sns.barplot(x=x, y=y1, palette="Reds", ax=ax1).set_title('Corridor 1')
ax1.axhline(0, color="k", clip_on=False)
ax1.set_ylabel("Pasture")

# Generate some sequential data

x = [60,90,120]
y1 = y_agri_1
sns.barplot(x=x, y=y1, palette="Reds", ax=ax2)
ax2.axhline(0, color="k", clip_on=False)
ax2.set_ylabel("Agriculture")

# Generate some sequential data

x = [60,90,120]
y1 = y_exp_s_1
sns.barplot(x=x, y=y1, palette="Reds", ax=ax3)
ax3.axhline(0, color="k", clip_on=False)
ax3.set_ylabel("Exposed Soil")

# Finalize the plot

sns.despine(bottom=True)
plt.setp(f2.axes, yticks=[])
plt.tight_layout(h_pad=2)




#%%

img2_60 =  imageio.imread(img_dir + 'corr_2_60_current.tif')


(unique4, counts4) = np.unique(img2_60, return_counts=True)
frequencies2_60 = np.asarray((unique4, counts4)).T

agri_for_2_60 = (frequencies2_60[1,1]*500) / 10000
pasture_for_2_60 = (frequencies2_60[5,1]*500) / 10000
exp_soil_for_2_60 = (frequencies2_60[3,1]*500) / 10000
or_forest_2_60 = (frequencies1_60[4,1]*500) / 10000


img2_90 =  imageio.imread(img_dir + 'corr_2_90_current.tif')


(unique5, counts5) = np.unique(img2_90, return_counts=True)
frequencies2_90 = np.asarray((unique5, counts5)).T

agri_for_2_90 = (frequencies2_90[1,1]*500) / 10000
pasture_for_2_90 = (frequencies2_90[5,1]*500) / 10000
exp_soil_for_2_90 = (frequencies2_90[3,1]*500) / 10000
or_forest_2_90 = (frequencies1_90[4,1]*500) / 10000


img2_120 =  imageio.imread(img_dir + 'corr_2_120_current.tif')


(unique6, counts6) = np.unique(img2_120, return_counts=True)
frequencies2_120 = np.asarray((unique6, counts6)).T

agri_for_2_120 = (frequencies2_120[1,1]*500) / 10000
pasture_for_2_120 = (frequencies2_120[5,1]*500) / 10000
exp_soil_for_2_120 = (frequencies2_120[3,1]*500) / 10000
or_forest_2_120 = (frequencies1_120[4,1]*500) / 10000

results_agri_2 = (agri_for_2_60, agri_for_2_90, agri_for_2_120)
results_pature_2 =(pasture_for_2_60,pasture_for_2_90,pasture_for_2_120)
results_exp_soil_2 = (exp_soil_for_2_60, exp_soil_for_2_90, exp_soil_for_2_120)
results_forest_2 = (or_forest_2_60,or_forest_2_90, or_forest_2_120)
scenarios = (60,90,120)

x = scenarios
y_agri_2 = results_agri_2
y_past_2 = results_pature_2
y_exp_s_2 = results_exp_soil_2
y_forest_2 = results_forest_2

f3 = plt.figure()
plt.xlim(50,130)
plt.ylim(0,350)
plt.plot(x,y_agri_2, 'b--x', label = "Croplands Restored")
plt.plot(x,y_past_2,'r--x', label = "Pasturelands Restored")
plt.plot(x,y_exp_s_2, 'y--x', label = "Exposed soil Restored")
plt.plot(x,y_forest_2, 'g-x', label = "Original Forest Maintained")
plt.legend(loc='upper left')
plt.xlabel("Corridor Width (Meters)")
plt.ylabel("Reforested Area (Hectares)")
plt.title('Corridor 2')
plt.grid()

#%%
#Visualization - 2

# Setting up another type of visualization.
#This time all graphs are in the same image. This allows for better comparison 
# between them.

#setting the style with the seaborn library
sns.set(style="white", context="talk")


# Set up the matplotlib figure and dividing into subplots
f4, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7, 5), sharex=True)

# setting the 1st bar plot 
x = [60,90,120] #corridor with
y1 = y_past_2
sns.barplot(x=x, y=y1, palette="Reds", ax=ax1).set_title('Corridor 2')
ax1.axhline(0, color="k", clip_on=False)
ax1.set_ylabel("Pasture")

# setting the 2nd bar plot
x = [60,90,120] #corridor width
y1 = y_agri_2
sns.barplot(x=x, y=y1, palette="Reds", ax=ax2)
ax2.axhline(0, color="k", clip_on=False)
ax2.set_ylabel("Agriculture")

# setting the 3rd bar plot
x = [60,90,120]
y1 = y_exp_s_2
sns.barplot(x=x, y=y1, palette="Reds", ax=ax3)
ax3.axhline(0, color="k", clip_on=False)
ax3.set_ylabel("Exposed Soil")

# Finalizing and displaying the bar plots into the image

sns.despine(bottom=True)
plt.setp(f4.axes, yticks=[])
plt.tight_layout(h_pad=2)



#%%

# Exporting the images to a directory folder.

#Setting up the directoy
output_dir = "C:/Users/carvalhp/Desktop/EDA/Final Project/Output"

#Saving the images
f1.savefig('{}/Figure_1'.format(output_dir))
f3.savefig('{}/Figure_3'.format(output_dir))
f2.savefig('{}/Figure_2.png'.format(output_dir))
f4.savefig('{}/Figure_4'.format(output_dir))
