import os
import shutil

train_folder = '/Users/arsyaninsa/Documents/Data_Personal/Kuliah/Bangkid/Nyobas Modelling/dataset_many/train'
test_folder = '/Users/arsyaninsa/Documents/Data_Personal/Kuliah/Bangkid/Nyobas Modelling/dataset_many/test'
num_images_to_move = 40

# Get a list of subfolders in the train folder
subfolders = [f for f in os.listdir(train_folder) if os.path.isdir(os.path.join(train_folder, f))]

# Create the test folder if it doesn't exist
if not os.path.exists(test_folder):
    os.makedirs(test_folder)

# Iterate over each subfolder
for subfolder in subfolders:
    train_subfolder_path = os.path.join(train_folder, subfolder)

    # Get a list of images in the current subfolder
    images = [f for f in os.listdir(train_subfolder_path) if os.path.isfile(os.path.join(train_subfolder_path, f))]

    # Create the corresponding subfolder in the test folder
    test_subfolder_path = os.path.join(test_folder, subfolder)
    if not os.path.exists(test_subfolder_path):
        os.makedirs(test_subfolder_path)

    # Move the specified number of images to the test subfolder
    for image in images[:num_images_to_move]:
        image_path = os.path.join(train_subfolder_path, image)
        shutil.move(image_path, test_subfolder_path)