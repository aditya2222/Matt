from django.db import models

# Create your models here.


# Spreadsheet Model

# Models 1-60

class SpreadSheet1(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)



class SpreadSheet2(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)


class SpreadSheet3(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)




class SpreadSheet4(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)



class SpreadSheet5(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)


class SpreadSheet6(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)


class SpreadSheet7(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)


class SpreadSheet8(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)


class SpreadSheet9(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)


class SpreadSheet10(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)

# 11-55 models



class SpreadSheet11(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)



class SpreadSheet12(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)


class SpreadSheet13(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)




class SpreadSheet14(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)



class SpreadSheet15(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)


class SpreadSheet16(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)


class SpreadSheet17(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)


class SpreadSheet18(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)


class SpreadSheet19(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)


class SpreadSheet20(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=60, decimal_places=55)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_3_hr_vs_60 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_60_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=60, decimal_places=55)

    def __str__(self):
        return str(self.clr)