import pandas as pd
url = "datos_archivo_ETFs.csv"
df = pd.read_csv(url)

nombres = {"ANO": "year", "MES": "month", "DIA": "day", "HORA": "hour"}
df = df.rename(columns=nombres)

df.index = pd.(df[["high", "low", "open", "close", "volume"]])

df = df[["DECL"]]

print(len(df))

df = df.dropna()
df = df[df.DECL != 0]

print(len(df))

df.plot()