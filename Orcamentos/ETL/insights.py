import pandas as pd

df = pd.read_csv("Downloads/Processed/orcamento_despesa_clean.csv")

print(df.shape)        # rows and columns
print(df.columns)      # confirm column names
print(df.dtypes)       # see if numerics really are numerics
print(df.head())       # quick preview
print(df.isna().sum()) # look for missing data


df.groupby(["ano", "nome_orgao_superior"])[
    "orcamento_realizado_r"
].sum().reset_index()

df["execucao%"] = (
    df["orcamento_realizado_r"] / df["orcamento_atualizado_r"]
) * 100