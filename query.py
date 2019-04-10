import pandas as pd

# Reading CSV
df = pd.read_csv('sample.csv')
# Fixing Price data
df['Price'] = df['Price'].str.replace(',', '')
df['Price'] = df['Price'].astype(int)
# Adding new Day column
df['Day'] = pd.to_datetime(df['Transaction_date']).dt.date

print ('----------------------------------------------------------------')
print ('Number of users per country per state')
print (df.groupby(['Country', 'State'])['Name'].nunique())
print ('----------------------------------------------------------------')
print ("Total revenue per City.")
print (df.groupby('City')['Price'].sum())
print ('----------------------------------------------------------------')
print ("Number of transactions per name")
print (df.groupby('Name')['Transaction_date'].nunique())
print ('----------------------------------------------------------------')
print ("Total revenue per day per product")
print (df.groupby(['Day', 'Product'])['Price'].sum())
print ('----------------------------------------------------------------')


def get_revenue_per_day_by_product_and_country(product, country):
    """
    This function returns revenue per day by a given product and country name
    :param product:
    :param country:
    :return pandas.Series:
    """
    print ("Revenue per day of {} from {}".format(product, country))
    df_us = df.loc[(df['Product'] == product) & (df['Country'] == country)]
    print(df_us.groupby(['Day', 'Product', 'Country'])[['Price']].sum())


get_revenue_per_day_by_product_and_country('Product1', 'United States')

print ('----------------------------------------------------------------')
print ("Total Revenue per Payment Type per Day")
print (df.groupby(['Payment_Type', 'Day'])['Price'].sum())
print ('----------------------------------------------------------------')
print ("Total revenue per City per Day")
print (df.groupby(['City', 'Day'])['Price'].sum())
print ('----------------------------------------------------------------')
print ("Total revenue per Product per Country per State per City")
print (df.groupby(['Product', 'Country', 'State', 'City'])['Price'].sum())
print ('----------------------------------------------------------------')
print ("Number of transactions per Country per State per City")
print (df.groupby(['Product', 'Country', 'State', 'City'])['Transaction_date'].nunique())
