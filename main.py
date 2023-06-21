import tabula
import pandas as pd

# Extract table from PDF
#df = tabula.read_pdf('pdf/Ethnic Catalogue 2021 - online.pdf', pages='all', encoding='latin1')
#df = tabula.read_pdf('pdf/Packaging Catalogue Draft.pdf', pages='all', encoding='latin1')
df = tabula.read_pdf('pdf/Daftar karyawan.pdf', pages=1, encoding='latin1')
print(df)

# Concatenate multiple DataFrames into a single DataFrame
df_combined = pd.concat(df)

# Save extracted data to an Excel file
#df_combined.to_excel('excel/output_excel_file.xlsx', index=False)
df_combined.to_excel('excel/daftar karyawan.xlsx', index=False)