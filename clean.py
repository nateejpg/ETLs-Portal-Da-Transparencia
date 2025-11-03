import os
import pandas as pd

# Folder
EXTRACTED_FOLDER = "Downloads/Extracted"

# SINGLE
dfs = []

for file in os.listdir(EXTRACTED_FOLDER):

    if file.endswith("csv"):
        df = pd.read_csv(os.path.join(EXTRACTED_FOLDER, file), sep = ';', encoding='latin1')
        df['ANO'] = int(file[:4])
        dfs.append(df)

single_df = pd.concat(dfs, ignore_index=True)

