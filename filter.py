import pandas as pd


file_name = "All_2020-05-22_2000_CHAIYA.xlsx"
xl_file = pd.ExcelFile(file_name)

dfs = {
  sheet_name: xl_file.parse(sheet)
}

print(df)