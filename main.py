import os
import shutil
from pathlib import Path

def organize_files(directory):
    # Convert to absolute path
    directory = Path(directory).resolve()

    # Check if directory exists
    if not directory.is_dir():
        print(f"Error: {directory} is not a valid directory.")
        return

    # Scan directory for files
    files = [f for f in directory.iterdir() if f.is_file()]

    if not files:
        print(f"No files found in {directory}.")
        return

    # Process files by extension
    for file in files:
        # Get file extension (e.g., .txt, .jpg)
        extension = file.suffix[1:]  # Skip the dot in .suffix
        if not extension:  # Skip files with no extensions
            extension = "no_extension"

        # Create folder for extension if it doesn't exist
        folder = directory / extension
        folder.mkdir(exist_ok=True)

        # Move file into respective folder
        shutil.move(str(file), str(folder / file.name))

    print(f"Files in {directory} have been organized by extension.")

# Deployable CLI functionality
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Organize files by extension in a directory.")
    parser.add_argument(
        "directory",
        nargs="?",
        default=os.getcwd(),
        help="The directory to organize (default: current directory)."
    )
    args = parser.parse_args()
    organize_files(args.directory)
