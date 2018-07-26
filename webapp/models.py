from django.db import models


# Create your models here.


# Spreadsheet Model

# Models 1-60

class SpreadSheet1(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet2(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet3(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet4(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet5(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet6(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet7(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet8(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet9(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet10(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


# 11-55 models


class SpreadSheet11(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet12(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet13(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet14(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet15(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet16(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet17(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet18(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet19(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)


class SpreadSheet20(models.Model):
    consumed = models.FloatField(
        blank=True, null=True)
    clr = models.FloatField(blank=True, null=True,
                            )
    spread = models.FloatField(
        blank=True, null=True)
    percentage_of_available_funds = models.FloatField(
        blank=True, null=True)
    rand_loan_amount = models.FloatField(
        blank=True, null=True)
    rand_term = models.FloatField(
        blank=True, null=True)
    rand_rate = models.FloatField(
        blank=True, null=True)
    btc_usd_price = models.FloatField(
        blank=True, null=True)
    eth_usd_price = models.FloatField(
        blank=True, null=True)
    btc_eth_price = models.FloatField(
        blank=True, null=True)
    demand = models.FloatField(
        blank=True, null=True)
    supply = models.FloatField(
        blank=True, null=True)
    ratio_demand_supply = models.FloatField(
        blank=True, null=True)
    number_of_bids_demand = models.FloatField(
        blank=True, null=True)
    number_of_offers_supply = models.FloatField(
        blank=True, null=True)
    ratio_bids_offers = models.FloatField(
        blank=True, null=True)
    weighted_average_rate = models.FloatField(
        blank=True, null=True)
    simple_average_rate = models.FloatField(
        blank=True, null=True)
    demand_avg_rate = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr = models.FloatField(
        blank=True, null=True)
    avg_clr_7_days = models.FloatField(
        blank=True, null=True)
    avg_clr_3_hr_vs_60 = models.FloatField(
        blank=True, null=True)
    avg_clr_60_hr_vs_12 = models.FloatField(
        blank=True, null=True)
    avg_clr_12_hr_vs_24 = models.FloatField(
        blank=True, null=True)
    avg_clr_24_hr_vs_48 = models.FloatField(
        blank=True, null=True)
    avg_clr_48_hr_vs_7_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_1_day = models.FloatField(
        blank=True, null=True)
    btc_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    btc_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_2_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_3_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_7_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_14_days = models.FloatField(
        blank=True, null=True)
    eth_sentiment_30_days = models.FloatField(
        blank=True, null=True)
    day_of_week = models.FloatField(
        blank=True, null=True)
    time_of_day = models.FloatField(
        blank=True, null=True)
    good_bad = models.FloatField(
        blank=True, null=True)
    date = models.DateTimeField(max_length=120,blank=True, null=True)

    def __str__(self):
        return str(self.clr)
