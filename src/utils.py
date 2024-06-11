import os
import zipfile
import requests
from pathlib import Path
from netrc import netrc
from urllib.parse import urlparse


def download_file(url, destination_file):
    """
    Download a file from a URL to a specified destination.

    Args:
        url (str): The URL of the file to download.
        destination_file (str): The path to the destination file.

    Returns:
        None
    """
    # Ensure the directory exists
    destination_path = Path(destination_file)
    destination_path.parent.mkdir(parents=True, exist_ok=True)

    if destination_path.is_file():
        print(f"Already downloaded {destination_file}")
    else:
        print(f"Downloading {destination_file} ... ", end="")
        
        # Load credentials from .netrc file if available
        auth = None
        try:
            netrc_info = netrc()
            host = urlparse(url).hostname
            auth = netrc_info.authenticators(host)
        except (FileNotFoundError, KeyError):
            pass

        # Download the file
        with requests.get(url, auth=auth, stream=True) as response:
            response.raise_for_status()
            with open(destination_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("done.")


def unzip_one_file(zipfile_path, filename, destination_file):
    """
    Unzip a specific file from a zip archive to a specified destination.

    Args:
        zipfile_path (str): The path to the zip archive.
        filename (str): The name of the file to extract from the zip archive.
        destination_file (str): The path to the destination file.

    Returns:
        None
    """
    # Ensure the directory exists
    destination_path = Path(destination_file)
    destination_path.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
        if filename in zip_ref.namelist():
            with zip_ref.open(filename) as source, open(destination_file, 'wb') as target:
                target.write(source.read())
            print(f"Extracted {filename} to {destination_file}")
        else:
            print(f"{filename} not found in the zip archive")


def unzip_all_files(zipfile_path, destination_dir):
    """
    Unzip all files from a zip archive to a specified directory.

    Args:
        zipfile_path (str): The path to the zip archive.
        destination_dir (str): The directory where to extract all files.

    Returns:
        None
    """
    # Ensure the directory exists
    destination_path = Path(destination_dir)
    destination_path.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
        zip_ref.extractall(destination_dir)
    print(f"Extracted all files to {destination_dir}")


def convert_to_csv(source_file, destination_file):
    """
    Convert a text file to a CSV file.

    Args:
        source_file (str): The path to the source text file.
        destination_file (str): The path to the destination CSV file.

    Returns:
        None
    """
    import pandas as pd

    data = pd.read_csv(source_file, delimiter="\t")
    data.to_csv(destination_file, index=False)
    print(f"Converted {source_file} to {destination_file}")

# Example usage
if __name__ == "__main__":
    unzip_one_file('path/to/your/archive.zip', 'file_to_extract.txt', 'destination/path/file_to_extract.txt')
    unzip_all_files('path/to/your/archive.zip', 'destination/directory')
    convert_to_csv('path/to/your/source_file.txt', 'destination/path/destination_file.csv')
