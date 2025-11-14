import os
import pandas as pd

EXTRACTED_FOLDER = "./Downloads/Extracted"

dfs = []
for file in os.listdir(EXTRACTED_FOLDER):
    if file.endswith("csv"):
        df = pd.read_csv(os.path.join(EXTRACTED_FOLDER, file), sep=";", encoding="latin1")
        df["ANO"] = int(file[:4])
        dfs.append(df)

single_df = pd.concat(dfs, ignore_index=True)

df = single_df.copy()

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.normalize("NFKD")
    .str.encode("ascii", errors="ignore")
    .str.decode("utf-8")
    .str.replace(" ", "_")
    .str.replace(r"[^a-zA-Z0-9_]", "", regex=True)
)

numeric_cols = [
    "orcamento_atualizado_r",
    "orcamento_empenhado_r",
    "orcamento_realizado_r",
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .replace("", "0")
            .astype(float)
        )

target_col = [c for c in df.columns if "realizado" in c and "orcamento" in c]

if target_col:
    col = target_col[0]
    df["percentual_realizado"] = (
        df[col]
        .astype(str)
        .str.replace("%", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float) / 100
    )

for col in df.columns:
    if df[col].dtype == object:
        df[col] = df[col].replace({",": ".", "%": ""}, regex=True)
        df[col] = pd.to_numeric(df[col], errors="ignore")

PROCESSED_FOLDER = "Downloads/Processed"
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

output_path = os.path.join(PROCESSED_FOLDER, "orcamento_despesa_clean.csv")
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"Cleaned dataset saved to {output_path}")
