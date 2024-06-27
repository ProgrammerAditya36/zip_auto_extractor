import os
import time
import zipfile

# Directory to monitor (change this to your Downloads directory or any other directory)
download_directory = "C:\\Users\\Administrator\\Downloads"

# Function to check for new zip files
def check_for_new_zips(directory):
    new_zips = []
    for filename in os.listdir(directory):
        if filename.endswith('.zip'):
            new_zips.append(os.path.join(directory, filename))
    return new_zips

# Example usage
while True:
    new_zips = check_for_new_zips(download_directory)
    if new_zips:
        for zip_file in new_zips:
            # Extract the zip file
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                # Create a folder with the same name as the zip file (without extension)
                extract_dir = os.path.splitext(zip_file)[0]
                os.makedirs(extract_dir, exist_ok=True)
                zip_ref.extractall(extract_dir)
                
            # Delete the zip file after extraction
            os.remove(zip_file)
            print(f"Extracted and deleted: {zip_file}")
    
    # Sleep for 1 second before checking again
    time.sleep(1)
