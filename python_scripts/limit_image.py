import os
import random
import shutil

train_folder = '/Users/arsyaninsa/Documents/Data_Personal/Kuliah/Bangkid/Nyobas Modelling/dataset_many/train'
max_images_per_subfolder = 500

# Get a list of subfolders in the train folder
subfolders = [f for f in os.listdir(train_folder) if os.path.isdir(os.path.join(train_folder, f))]

# Iterate over each subfolder
for subfolder in subfolders:
    subfolder_path = os.path.join(train_folder, subfolder)

    # Get a list of images in the current subfolder
    images = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]

    # Shuffle the images randomly
    random.shuffle(images)

    # Determine the number of images to move
    num_images = len(images)
    if num_images > max_images_per_subfolder:
        images_to_move = images[max_images_per_subfolder:]
    else:
        continue

    # Create a temporary folder to store the excess images
    temp_folder = os.path.join(subfolder_path, 'temp')
    os.makedirs(temp_folder)

    # Move the excess images to the temporary folder
    for image in images_to_move:
        image_path = os.path.join(subfolder_path, image)
        shutil.move(image_path, temp_folder)

    # Delete the temporary folder
    shutil.rmtree(temp_folder)