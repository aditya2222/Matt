from django.db import models

# Create your models here.


# Spreadsheet Model

# Models 1-10

class SpreadSheet1(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)



class SpreadSheet2(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)


class SpreadSheet3(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)




class SpreadSheet4(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)



class SpreadSheet5(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)


class SpreadSheet6(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)


class SpreadSheet7(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)


class SpreadSheet8(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)


class SpreadSheet9(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)


class SpreadSheet10(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)

# 11-20 models



class SpreadSheet11(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)



class SpreadSheet12(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)


class SpreadSheet13(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)




class SpreadSheet14(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)



class SpreadSheet15(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)


class SpreadSheet16(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)


class SpreadSheet17(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)


class SpreadSheet18(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)


class SpreadSheet19(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)


class SpreadSheet20(models.Model):
    consumed = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    clr = models.DecimalField(blank=True, null=True,
                              max_digits=100, decimal_places=20)
    spread = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    percentage_of_available_funds = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_loan_amount = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_term = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    rand_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_usd_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_eth_price = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_demand_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_bids_demand = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    number_of_offers_supply = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    ratio_bids_offers = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    weighted_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    simple_average_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    demand_avg_rate = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_3_hr_vs_6 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_6_hr_vs_12 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_12_hr_vs_24 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_24_hr_vs_48 = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    avg_clr_48_hr_vs_7_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_1_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    btc_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_2_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_3_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_7_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_14_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    eth_sentiment_30_days = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    day_of_week = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    time_of_day = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)
    good_bad = models.DecimalField(
        blank=True, null=True, max_digits=100, decimal_places=20)

    def __str__(self):
        return str(self.clr)
