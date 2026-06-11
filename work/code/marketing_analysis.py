import pandas as pd

CAMPAIGN_COLUMN = "Campaign"
CLICKS_COLUMN = "Clicks"
IMPRESSIONS_COLUMN = "Impressions"


def get_campaign_with_highest_ctr(file_path):
    marketing_data = pd.read_csv(file_path)

    campaign_totals = marketing_data.groupby(CAMPAIGN_COLUMN)[
        [CLICKS_COLUMN, IMPRESSIONS_COLUMN]
    ].sum()

    campaign_click_through_rates = (
        campaign_totals[CLICKS_COLUMN] / campaign_totals[IMPRESSIONS_COLUMN]
    ) * 100

    return campaign_click_through_rates.idxmax()


file_to_test = "E:/data_analyst/work/data/marketing_campaign.csv"
print(get_campaign_with_highest_ctr(file_to_test))