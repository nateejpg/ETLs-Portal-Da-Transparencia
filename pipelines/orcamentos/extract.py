import os
import zipfile
import pandas as pd

# FOLDER

RAW_FOLDER = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../data/raw/orcamentos"
    )
)
EXTRACT_FOLDER = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../data/extracted/orcamentos"
    )
)

os.makedirs(EXTRACT_FOLDER, exist_ok=True)

# EXTRACT

for file in os.listdir(RAW_FOLDER):

    try:
        if file.endswith(".zip"):
            print(f"Extracting {file}")
            file_path = os.path.join(RAW_FOLDER, file)
            with zipfile.ZipFile(file_path) as fe:
                fe.extractall(EXTRACT_FOLDER)
                print(f"File {file_path} has been extracted!")

    except Exception as e:

        print("There are no zips to extract!")

    print(f"All files have been extracted!")

# READ

for file in os.listdir(EXTRACT_FOLDER):

    try:

        file_path = os.path.join(EXTRACT_FOLDER, file)
        df = pd.read_csv(file_path, sep=";", nrows=5, encoding="latin1")
        print(df.head())

    except Exception as e:

        print("There was an error with the CSV, try again!")

