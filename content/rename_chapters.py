import os
import re

# Path to your content folder
root_dir = "content"

# Regex pattern to extract chapter numbers from filenames
chapter_pattern = re.compile(r"chapter-(\d+)", re.IGNORECASE)

# Walk through all subfolders in the content directory
for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".json"):
                match = chapter_pattern.search(filename)
                if match:
                    chapter_number = match.group(1)
                    new_filename = f"chapter-{chapter_number}.json"
                    old_path = os.path.join(folder_path, filename)
                    new_path = os.path.join(folder_path, new_filename)

                    # Only rename if the new filename doesn't already exist
                    if old_path != new_path and not os.path.exists(new_path):
                        print(f"Renaming: {filename} → {new_filename}")
                        os.rename(old_path, new_path)
