import os
import requests

# FOLDER
RAW_FOLDER = "Downloads/Raw"
os.makedirs(RAW_FOLDER, exist_ok=True)

# URL

URL = "https://portaldatransparencia.gov.br/download-de-dados/orcamento-despesa"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/129.0.0.0 Safari/537.36"
}

# PREPARE URL

years = list(range(2014, 2026))
print(f"Available years: {years}")

# DOWNLOAD DATA

for year in years:

    file_path = os.path.join(RAW_FOLDER, f"orcamento_despesa_{year}.zip")
    i_url = {f"{URL}/{year}"}

    try:
        response = requests.get(i_url, timeout=180, headers=headers)
        response.raise_for_status()

# WRITE DATA
        with open(file_path, "wb") as f:

            f.write(response.content)
            print((f"Saved {file_path}"))

    except requests.exceptions.RequestException as e:

        print(f"There was an error with {year}")


print("All years have beeen downloaded!")

