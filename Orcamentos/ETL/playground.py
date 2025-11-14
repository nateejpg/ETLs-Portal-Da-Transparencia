import os
import zipfile
import pandas as pd


# FOLDER
RAW_FOLDER = "Downloads/Raw"
EXTRACTED_FOLDER = "Download/Extract"

# EXTRACT

for file in os.listdir(RAW_FOLDER):

    file_path = os.path.join(RAW_FOLDER, file)

    try:
        with zipfile.ZipFile(file_path, "r") as extract:
            print(f"Extracting file {file}")
            extract.extractall(EXTRACTED_FOLDER)

    except Exception as e:

        print(f"There was an error with {file}")


# READ

for file in os.listdir(EXTRACTED_FOLDER):

    file_path = os.path.join(EXTRACTED_FOLDER, file)

    try:

        df = pd.read_csv(file_path, sep=";", nrows=5, encoding="latin1")
        print(df.head())


    except Exception as e:
    
        print(f"There was an error with {file}")