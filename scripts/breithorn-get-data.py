import os
import requests
import zipfile

def download_file(url, destination_file):
    """
    Downloads a file from the given URL to the specified destination.

    Args:
        url (str): The URL of the file to download.
        destination_file (str): The path where the downloaded file should be saved.
    """
    os.makedirs(os.path.dirname(destination_file), exist_ok=True)
    
    if os.path.isfile(destination_file):
        print(f"Already downloaded {destination_file}")
    else:
        try:
            print(f"Downloading {destination_file} ... ", end="")
            response = requests.get(url)
            response.raise_for_status()
            with open(destination_file, 'wb') as file:
                file.write(response.content)
            print("done.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {destination_file}: {e}")
            raise

def unzip_file(zip_path, extract_to):
    """
    Unzips a file to the specified directory.

    Args:
        zip_path (str): The path to the zip file.
        extract_to (str): The directory to extract files to.
    """
    os.makedirs(extract_to, exist_ok=True)
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Unzipped {zip_path} to {extract_to}")
    except zipfile.BadZipFile:
        print(f"Error: {zip_path} is not a valid zip file.")

def setup_directories(base_dir):
    """
    Sets up the project directories for data and results.

    Args:
        base_dir (str): The base directory for the project.
    """
    dirs = [
        os.path.join(base_dir, 'data', 'weather'),
        os.path.join(base_dir, 'data', 'glacier_mask'),
        os.path.join(base_dir, 'data', 'dem'),
        os.path.join(base_dir, 'results')
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Created directory: {d}")

def process_file(file_path, extract_to=None):
    """
    Process a downloaded file based on its extension. Unzips if it's a zip file.

    Args:
        file_path (str): The path to the downloaded file.
        extract_to (str, optional): The directory to extract files to if it's a zip file.
    """
    if file_path.endswith('.zip') and extract_to:
        unzip_file(file_path, extract_to)
    else:
        print(f"Processing file: {file_path} (No extraction needed)")


def main():
   # Base directory for the project
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))  # Two levels up
    setup_directories(base_dir)

    # Download data
    # Example URLs, replace with actual URLs
    weather_url = 'https://github.com/mauro3/CORDS/blob/master/data/workshop-reproducible-research/own/weather.dat'
    glacier_mask_url = 'https://github.com/mauro3/CORDS/blob/master/data/workshop-reproducible-research/own/mask_breithorngletscher.zip'
    dem_url = 'https://github.com/mauro3/CORDS/blob/master/data/workshop-reproducible-research/foreign/swisstopo_dhm200_cropped.zip'

    download_file(weather_url, os.path.join(base_dir, 'data', 'weather', 'weather_data.zip'))
    download_file(glacier_mask_url, os.path.join(base_dir, 'data', 'glacier_mask', 'glacier_mask_data.zip'))
    download_file(dem_url, os.path.join(base_dir, 'data', 'dem', 'dem_data.zip'))

    # Unzip data
    unzip_file(os.path.join(base_dir, 'data', 'weather', 'weather_data.zip'), os.path.join(base_dir, 'data', 'weather'))
    unzip_file(os.path.join(base_dir, 'data', 'glacier_mask', 'glacier_mask_data.zip'), os.path.join(base_dir, 'data', 'glacier_mask'))
    unzip_file(os.path.join(base_dir, 'data', 'dem', 'dem_data.zip'), os.path.join(base_dir, 'data', 'dem'))

    # Extra data
    z_weather_station = 2650  # elevation of weather station [m]
    Ps0 = 0.005  # mean (and constant) precipitation rate [m/d]
    print(f"Weather station elevation: {z_weather_station} m")
    print(f"Mean precipitation rate: {Ps0} m/d")

if __name__ == "__main__":
    main()
