import pandas as pd

#####################
### Exploration
#####################


codes_naf = pd.read_csv("CODES_NAF_PERIMETRE.csv", encoding = "ISO-8859-1", sep=";")
factu = pd.read_excel("Données facturation ptf banques.xlsx")
export = pd.read_excel("Export 05_08_2021 16_41 (1).xlsx", sheet_name="Résultats", nrows=20000)
formes = pd.read_csv("FORMES_JURIDIQUES.csv", encoding = "ISO-8859-1", sep=";")
sul = pd.read_csv("StockUniteLegale_utf8.csv", low_memory=False, nrows=20000)


print(sul.columns)