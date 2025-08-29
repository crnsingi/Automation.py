import pandas as pd
import glob

# Read all Excell files in a folder
files = glob.glob("reports/*/xlsx")

final_df = pd.DataFrame()

for file in files:
    df = pd.read_excel(file)
    final_df = pd.concat([final_df, df], ignore_index=True)
    
    # Save consolidated report
    final_df.to_excel("Final_Report.xlsx", index=False)
    print("Consolidated report created successfully!")