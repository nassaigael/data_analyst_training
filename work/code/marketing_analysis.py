import pandas as pd # type: ignore

def get_ctr_by_campagne(file_path):
    df = pd.read_csv(file_path)
    
    df["click_through_rate"] = (
        df["Clicks"] / df["Impressions"] * 100
    )
    
    result = df.groupby("Campaign")["click_through_rate"].sum()
    return result
    
file_to_test = "E:/data_analyst/work/data/marketing_campaign.csv"
    
print(get_ctr_by_campagne(file_to_test))