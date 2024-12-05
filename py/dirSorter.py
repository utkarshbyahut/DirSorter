import os
import shutil
from pathlib import Path


def organize_files(directory: str) -> None:
    """
    Organizes files in the given directory by their extensions.

    This function scans the specified directory for files, creates subdirectories
    for each unique file extension, and moves the files into their respective subdirectories.

    Parameters:
        directory (str): The path to the directory to organize.

    Returns:
        None
    """
    # Resolve the absolute path of the directory
    directory_path = Path(directory).resolve()

    # Check if the given path is a valid directory
    if not directory_path.is_dir():
        print(f"[Error] The provided path '{directory_path}' is not a valid directory.")
        return

    # Retrieve a list of all files in the directory (ignoring subdirectories)
    files = [file for file in directory_path.iterdir() if file.is_file()]

    # Exit if no files are found
    if not files:
        print(f"[Info] No files found in the directory: {directory_path}")
        return

    print(f"[Processing] Organizing files in directory: {directory_path}")

    # Iterate over the files and organize them by extension
    for file in files:
        # Extract the file extension (e.g., .txt, .jpg)
        file_extension = file.suffix[1:]  # Remove the leading dot (.)
        if not file_extension:  # Handle files with no extensions
            file_extension = "no_extension"

        # Create a subdirectory for the file extension if it doesn't already exist
        target_folder = directory_path / file_extension
        target_folder.mkdir(exist_ok=True)

        # Move the file into the respective subdirectory
        destination = target_folder / file.name
        shutil.move(str(file), str(destination))
        print(f"[Moved] {file.name} -> {target_folder}/")

    print(f"[Success] Files in '{directory_path}' have been organized by extension.")


if __name__ == "__main__":
    import argparse

    # Define the command-line interface using argparse
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by their extensions."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=os.getcwd(),
        help="The directory to organize (default: current working directory).",
    )
    args = parser.parse_args()

    # Call the organize_files function with the provided directory
    organize_files(args.directory)
