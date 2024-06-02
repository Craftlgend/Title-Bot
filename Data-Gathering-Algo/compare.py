from pathlib import Path
import pandas as pd
from openpyxl import load_workbook, Workbook


new_version = Path.cwd() /"TOP600-2024-05-28-3368.xlsx"
old_version = Path.cwd() /"TOP600-2024-05-10-3368.xlsx"
final_table = Path.cwd() /"TOP600-05-Differences.xlsx"

df_old = pd.read_excel(old_version)
df_new = pd.read_excel(new_version)
df_final = pd.read_excel(final_table)





while df_old["Governor ID"].iloc[0] != None:
    Governor_ID = df_old["Governor ID"].iloc[0]
    
    if Governor_ID in df_new["Governor ID"].values:
        #new sheet
        result_new = df_new.loc[df_new['Governor ID'] == Governor_ID]
        Name = result_new["Governor Name"].values[0]
        Power_new = result_new["Power"].values[0]
        KP_new = result_new["Kill Points"].values[0]
        Deads_new = result_new["Deads"].values[0]
        T1_new = result_new["Tier 1 Kills"].values[0]
        T2_new = result_new["Tier 2 Kills"].values[0]
        T3_new = result_new["Tier 3 Kills"].values[0]
        T4_new = result_new["Tier 4 Kills"].values[0]
        T5_new = result_new["Tier 5 Kills"].values[0]
        RSS_new = result_new["Rss Assistance"].values[0]
        Alliance = result_new["Alliance"].values[0]

        #old sheet
        result_old = df_old.loc[df_old['Governor ID'] == Governor_ID]
        Power_old = result_old["Power"].values[0]
        KP_old = result_old["Kill Points"].values[0]
        Deads_old = result_old["Deads"].values[0]
        T1_old = result_old["Tier 1 Kills"].values[0]
        T2_old = result_old["Tier 2 Kills"].values[0]
        T3_old = result_old["Tier 3 Kills"].values[0]
        T4_old = result_old["Tier 4 Kills"].values[0]
        T5_old = result_old["Tier 5 Kills"].values[0]
        RSS_old = result_old["Rss Assistance"].values[0]
    
    
        Power = Power_new-Power_old
        KP = KP_new-KP_old
        Deads = Deads_new-Deads_old
        #T1 = T1_new-T1_old
        #T2 = T2_new-T2_old
        #T3 = T3_new-T3_old
        T4 = T4_new-T4_old
        T5 = T5_new-T5_old
        #RSS = RSS_new-RSS_old
        print(Name, Governor_ID, Power, KP, Deads,  T4, T5, Alliance )
        row = {
            "Governor Name": Name,
            "Governor ID": Governor_ID,
            "Power": Power,
            "Kill Points": KP,
            "Deads": Deads,
            #"Tier 1 Kills": T1,
            #"Tier 2 Kills": T2,
            #"Tier 3 Kills": T3,
            "Tier 4 Kills": T4,
            "Tier 5 Kills": T5,
            #"Rss Assistance": T4,
            #"Alliance": Alliance
        }
        df_final.loc[len(df_final)] = row
        df_final.to_excel(final_table, index= False)
        df_old = df_old.drop(df_old.index[0])
        df_old.to_excel(old_version, index= False)
    else:
        print(f"Player not in new ranking")
        df_old = df_old.drop(df_old.index[0])
        df_old.to_excel(old_version, index= False)
        

        

    







 


