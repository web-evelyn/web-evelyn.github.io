import os

def rename_images(folder_path):
    files = os.listdir(folder_path)
    images = [f for f in files if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.JPG'))]
    for i, filename in enumerate(images, start=1):
        file_extension = os.path.splitext(filename)[1]
        new_filename = f"{i}{file_extension}"
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)
        os.rename(old_filepath, new_filepath)
        print(f"Renamed: {old_filepath} -> {new_filepath}")

folder_path = 'images/Art to Heart'
rename_images(folder_path)
