from numpy import asarray
import argparse
import fancy_pca
from PIL import Image
import os
import glob

# Construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True,
#	help = "Path to the image")
#args = vars(ap.parse_args())

# Load multiple images
image_list = []
fname_list = []
path = 'D:/pca/images/*jpg' # path of the original dataset
path2 = 'D:/pca/images' # path of the original dataset folder

# Load images and put them in a list (image_list)
for infile in glob.glob(path):
    im = Image.open(infile)
    image_list.append(im)

# Extract the names of the files and put them in a list (fname_list)
base = os.listdir(path2)
for f in base:
    fname = os.path.splitext(f)
    fname_list.append(fname[0])
    print("Loading",infile)
    print(len(image_list)," images has loaded.")




# Load one image and show it
# i = Image.open('test.jpg')
# i.show(title="Original image")

# Convert images to numpy arrays
array_list =[]
n=1
for i in image_list:
    i_a = asarray(i)
    array_list.append(i_a)
    print("Image", n, ": Conversion successful.")
    n+=1
#print("Array of original image: ", i_a) #To see the array

print("Conversion successful")
print(type(i_a), i_a.shape)

# Perform the PCA color augmentation
n=1
aug_list=[]
for a in array_list:
    augmented = fancy_pca.fancy_pca(a)
    aug_list.append(a)
    print("Array",n, ":Augmentation successful")
    n += 1
#print("Array of PCA augmented image: ", augmented) #To see the array

# Convert Fancy PCA result back to PIL image
path3 = "D:/pca/augmented/" #path of the destination folder
idx=0
for aug in aug_list:
    i2 = Image.fromarray(aug)
    print(fname_list)
    while idx<= len(fname_list):
        print(str(fname_list[idx])+"_1.jpg")
        i2.save(path3+(str(fname_list[idx])+"_1.jpg"))
        break
    idx+=1
    print("Augmented image", idx, "saved.")