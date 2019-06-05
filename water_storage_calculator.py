#!/usr/bin/python

# facts derived from https://mind4survival.com/dehydration-facts/

# set these variables for your situation
# people invovled
males_over_fourteen = 1
females_over_fourteen = 1
female_nursing = 1
female_pregnant = 1
children_under_fourteen = 2

def water_storage_calculator():

    # conversion requirements
    ounces_per_gallon = 128
    liters_per_gallon = float(3.78)
    quarts_per_gallon = 4
    cups_per_gallon = 16

    # per day drinking requirements
    male_over_fourteen_ounces_required = 104
    female_over_fourteen_ounces_required = 72
    female_pregnant_ounces_required = 80
    female_nursing_ounces_required = 104
    children_under_fourteen_ounces_required = 64

    # toilet flushing
    flushes_per_day = 3
    gallons_per_flush = float(3.5)
    ounces_per_flush = gallons_per_flush * ounces_per_gallon

    # calculate daily use
    total_ounces = flushes_per_day * ounces_per_flush
    total_ounces += children_under_fourteen * children_under_fourteen_ounces_required
    total_ounces += males_over_fourteen * male_over_fourteen_ounces_required
    total_ounces += females_over_fourteen * female_over_fourteen_ounces_required
    total_ounces += female_nursing * female_nursing_ounces_required
    total_ounces += female_pregnant * female_pregnant_ounces_required

    # convert to gallons
    total_gallons_per_day = total_ounces / ounces_per_gallon
    total_gallons_per_week = total_gallons_per_day * 7
    total_gallons_per_month = total_gallons_per_day * 30

    # convert to liters
    total_liters_per_day = total_gallons_per_day / liters_per_gallon
    total_liters_per_week = total_gallons_per_day / liters_per_gallon * 7
    total_liters_per_month = total_gallons_per_day / liters_per_gallon * 30

    # paint results
    print ('Total daily water requirements in ounces: %s' % total_ounces)

    print ('Total daily water requirements in gallons: %s' % total_gallons_per_day)
    print ('Total weekly water requirements in gallons: %s' % total_gallons_per_week)
    print ('Total monthly water requirements in gallons: %s' % total_gallons_per_month)

    print ('Total daily water requirements in liters: %s' % total_liters_per_day)
    print ('Total weekly water requirements in liters: %s' % total_liters_per_week)
    print ('Total monthly water requirements in liters: %s' % total_liters_per_month)

if __name__ == "__main__":
    water_storage_calculator()
