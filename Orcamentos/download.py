import os
import requests

# URL
URL = "https://portaldatransparencia.gov.br/download-de-dados/orcamento-despesa"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/129.0.0.0 Safari/537.36"
}

# Folder
RAW_DATA_FILES = "../Downloads/Raw"
os.makedirs(RAW_DATA_FILES, exist_ok=True)

# Prepare Data
years = list(range(2014, 2026))
print(f"Years to download: {years}")

# Get the data
for year in years:

    print(f"Donwloading year: {year}")
    file_url = f"{URL}/{year}"
    file_path = os.path.join(RAW_DATA_FILES, f"orcamento_despesa_{year}.zip")

    try:

        response = requests.get(file_url, headers=headers, timeout=180)
        response.raise_for_status()

# Write Data
        with open(file_path, "wb") as f:
            f.write(response.content)

            print(f"Saved {file_path}")

    except requests.exceptions.RequestException as e:

        print(f"Failed to download {year}: {e}")

print("All files have been downloaded!")

