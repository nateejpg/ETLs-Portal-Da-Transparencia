import os
import zipfile
import pandas as pd

# Folder
RAW_FOLDER = "Downloads/Raw"
EXTRACTED_FOLDER = "Downloads/Clean"
os.makedirs(EXTRACTED_FOLDER, exist_ok=True)

# Extract

for file in os.listdir(RAW_FOLDER):
    if file.endswith("zip"):
        zip_path = os.path.join(RAW_FOLDER, file)
        print("Extracting {file}...")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(EXTRACTED_FOLDER)

# Read

for file in os.listdir(EXTRACTED_FOLDER):
    print(f"\n --- {file} ---")
    try:
        df = pd.read_csv(os.path.join(EXTRACTED_FOLDER, file), sep = ';', nrows=5, encoding='latin1')
        print(df.head())

    except Exception as e:
        print(f"There was an error with {file}! {e}")