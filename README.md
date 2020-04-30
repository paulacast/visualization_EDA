# visualization_EDA
# Restoration Corridors: Visualizing Results 

This script was created to generate quick visualization outputs for classified images representing restoration corridors. 

Input: classified land-use images in .tif format
Processing: calculates the area of conversion from one land use type (agriculture, exposed soil and pasture) into forest.
Output: Graphs representing the results 


## Premisses:

This script requires that some steps are taken during the image classification process.

```
Using ENVI or other remote sensing software:
	Classify the landsat 8 images into: Cloud / Shadow / Agriculture / Pasture / Exposed Soil / Forest
Using ArcGIS:
	Convert image into vector 
	Dissolve the vectorized image into the the land use types
Categorize the image into the 6 class types: now the attribute table should contain only 6 land use types and they’re correspondent pixel count.

In the attribute table it should be in regards to position:

Agriculture = 1
Exposed Soil = 3
Forest = 4
Pasture = 5

```

Because of the method of classification, I'm assuming a pixel size of around 22.5 meters x 22.5 meters. This is because of the vectorization of classes and then reconversion to raster.
This conversion caused some pixels to be cut to a size smaller than the 30m x 30m (Landsat standard).
I have tested a variety of pixel sizes and multiplying by 500 m is what came closest to reality. (I verified this results with data processed with ArcGIS)

### Prerequisites

Python 3.7
Images must be in .tif format. 


## Dependencies (Libraries)

* Os - For reading files and file paths.
* Imageio - For reading images.
* Numpy - For processing.
* Matplotlib - For visualization.
* Seaborn - For visualization.


## Authors

* **Paula Carvalho de Castro** 

## License

None

## Acknowledgments

* A shout out to everyone that posts tutorials on Stack Overflow 
