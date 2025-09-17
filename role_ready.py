import os
folder = "sample_folder"
for count, filename in enumerate(os.listdir(folder)):
    new_name = f"file_{count}.txt"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
print("Files renamed successfully.")
