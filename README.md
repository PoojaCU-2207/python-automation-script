# python-automation-script
A  beginner-friendly Python scripts for automating everyday tasks like file handling, simulation log parsing, LaTeX compilation, and basic web scraping. Designed to simplify workflows in academic and technical settings while building foundational coding skills.
import os

folder = "sample_folder"
for count, filename in enumerate(os.listdir(folder)):
    new_name = f"file_{count}.txt"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
print("Files renamed successfully.")
