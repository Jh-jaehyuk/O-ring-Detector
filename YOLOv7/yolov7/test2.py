import os

# Set the directory where the images are located
directory = 'C:\simple_images'

# Get the list of images in the directory
image_list = os.listdir(directory)

# Set the prefix for the new image names
prefix = 'image_'

# Set the starting value for the image counter
counter = 1

# Iterate over the images in the list
for image in image_list:
    # Get the file extension of the image
    extension = os.path.splitext(image)[1]

    # Construct the new image name
    new_name = prefix + str(counter) + extension

    # Construct the old and new file paths
    old_path = os.path.join(directory, image)
    new_path = os.path.join(directory, new_name)

    # Rename the image
    os.rename(old_path, new_path)

    # Increment the counter
    counter += 1
