import os

train_folder = '/Users/arsyaninsa/Documents/Data_Personal/Kuliah/Bangkid/Nyobas Modelling/dataset_many/train'

# Get a list of subfolders in the train folder
subfolders = [f for f in os.listdir(train_folder) if os.path.isdir(os.path.join(train_folder, f))]

# Iterate over each subfolder
for subfolder in subfolders:
    subfolder_path = os.path.join(train_folder, subfolder)
    subfolder_files = os.listdir(subfolder_path)

    # Iterate over each file in the subfolder
    for index, file_name in enumerate(subfolder_files, start=1):
        file_path = os.path.join(subfolder_path, file_name)

        # Split the file name and extension
        file_name_no_ext, file_ext = os.path.splitext(file_name)

        # Generate the new file name by combining the folder name and a number
        new_file_name = f"{subfolder}_{index}{file_ext}"

        # Generate the new file path by replacing the old file name with the new file name
        new_file_path = os.path.join(subfolder_path, new_file_name)

        # Rename the file
        os.rename(file_path, new_file_path)