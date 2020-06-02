## PCA Color Augmentation on Multiple Images

The easiest and most common method to perform data augmentation is to use transformations that does not change the labels. One example is PCA Color Augmentation.

PCA Color Augmentation (also called Fancy PCA) alters the intensities of the RGB channels along the natural variations of the images, denoted by the principal components of the pixel colors (Bargoti & Underwood, 2016). It performs Principal Components Analysis on the color channels, thus, given the name Fancy PCA.

To know more details, see [pca-color-augment.ipynb](https://github.com/addieira03/pca-color-augment/blob/master/pca_color_augment.ipynb).

The file [batch.py](https://github.com/addieira03/pca-color-augment/blob/master/batch.py) does PCA color augmentation on images from a source folder to another destination folder. 




Note: This is a modified version of this pca color augmentation code: https://github.com/pixelatedbrian/fortnight-furniture/blob/master/src/fancy_pca.py



