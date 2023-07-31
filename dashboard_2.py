Can't create, edit, or upload … Not enough storage. Get more now, or remove files from Drive, Google Photos, or Gmail.
#!/usr/bin/env python
# coding: utf-8

# # Import packages

# In[ ]:


#required for manipulating data
import pandas as pd
import numpy as np 

#enable Google Drive API
import gspread

#required for building the interactive dashboard
import panel as pn
pn.extension('tabulator')
import hvplot.pandas
import holoviews as hv
hv.extension('bokeh')


# # Connect to bank data and clean up your transactions

# In[ ]:


#option 1: connect to Google Drive
#move json file to project directory (where you have your python file) and rename it "service_account.json"

gc = gspread.service_account(filename="service_account.json")
sh = gc.open("revolut")


# In[ ]:


ws = sh.worksheet('Sheet1')
df = pd.DataFrame(ws.get_all_records())
df.head()


# In[ ]:


#option 2: import csv file

df = pd.read_csv('filename.csv')



# option 3: create dataset manually

data = [
    ['CARD_PAYMENT', 'Current', '2023-01-26 22:02:47', '2023-01-27 10:10:12', 'Tesco Stores 6601', -6.35, 0, 'GBP', 'COMPLETED', 521.07],
    ['CARD_PAYMENT', 'Current', '2023-01-26 16:13:50', '2023-01-27 11:50:32', 'Zettle_*donovan?s Bake', -2.5, 0, 'GBP', 'COMPLETED', 518.57],
    ['CARD_PAYMENT', 'Current', '2023-01-26 08:26:35', '2023-01-27 13:42:55', 'apple.com/bill', -3.99, 0, 'GBP', 'COMPLETED', 514.58],
    ['CARD_PAYMENT', 'Current', '2023-01-27 13:16:59', '2023-01-28 09:59:20', 'Tesco Stores 6601', -4.85, 0, 'GBP', 'COMPLETED', 509.73],
    ['CARD_PAYMENT', 'Current', '2023-01-27 10:43:22', '2023-01-28 11:48:36', 'Zettle_*the Good Eatin', -3.3, 0, 'GBP', 'COMPLETED', 506.43],
    ['CARD_PAYMENT', 'Current', '2023-01-27 19:07:07', '2023-01-28 15:51:42', 'Toogoodtog Mzs3m03xcn9', -5, 0, 'GBP', 'COMPLETED', 501.43],
    ['CARD_PAYMENT', 'Current', '2023-01-28 01:14:16', '2023-01-29 08:55:25', 'Montys Bar', -21, 0, 'GBP', 'COMPLETED', 480.43],
    ['CARD_PAYMENT', 'Current', '2023-01-28 16:26:00', '2023-01-29 09:41:04', 'Amznmktplace', -8.99, 0, 'GBP', 'COMPLETED', 471.44],
    ['CARD_PAYMENT', 'Current', '2023-01-28 19:59:36', '2023-01-29 09:49:29', 'Tesco Stores 6601', -8.65, 0, 'GBP', 'COMPLETED', 462.79],
    ['CARD_PAYMENT', 'Current', '2023-01-27 22:59:58', '2023-01-29 10:08:56', 'Urban 40', -12.6, 0, 'GBP', 'COMPLETED', 450.19],
    ['CARD_PAYMENT', 'Current', '2023-01-27 22:06:03', '2023-01-29 10:08:56', 'Urban 40', -6.1, 0, 'GBP', 'COMPLETED', 444.09],
    ['CARD_PAYMENT', 'Current', '2023-01-29 02:39:46', '2023-01-29 10:55:55', 'Tfl Travel Charge', -4.25, 0, 'GBP', 'COMPLETED', 439.84],
    ['CARD_PAYMENT', 'Current', '2023-01-28 15:06:44', '2023-01-29 11:31:51', 'Sq *lavelle Coffee Limite', -3.2, 0, 'GBP', 'COMPLETED', 436.64],
    ['CARD_PAYMENT', 'Current', '2023-01-29 15:08:04', '2023-01-31 14:06:07', 'Tubebuddycom*', -2.43, 0.02, 'GBP', 'COMPLETED', 451.69],
    ['CARD_PAYMENT', 'Current', '2023-01-29 15:11:03', '2023-01-31 14:45:55', 'Sp Blomma Beauty', -35, 0, 'GBP', 'COMPLETED', 416.69],
    ['CARD_PAYMENT', 'Current', '2023-01-29 20:03:55', '2023-01-31 15:11:28', 'Uber* Trip', -13.46, 0, 'GBP', 'COMPLETED', 403.23],
    ['CARD_PAYMENT', 'Current', '2023-01-29 14:31:09', '2023-01-31 17:29:48', 'Caravan', -27.67, 0, 'GBP', 'COMPLETED', 375.56],
    ['CARD_PAYMENT', 'Current', '2023-01-30 01:57:58', '2023-01-31 17:41:29', 'Tfl Travel Charge', -4.25, 0, 'GBP', 'COMPLETED', 371.31],
    ['CARD_PAYMENT', 'Current', '2023-01-31 02:36:53', '2023-01-31 18:03:14', 'Tfl Travel Charge', -1.65, 0, 'GBP', 'COMPLETED', 369.66],
    ['CARD_PAYMENT', 'Current', '2023-01-29 19:13:59', '2023-01-31 18:46:41', 'Hart Shoreditch Hotel', -3.6, 0, 'GBP', 'COMPLETED', 366.06],
    ['CARD_PAYMENT', 'Current', '2023-01-30 19:03:58', '2023-01-31 19:00:20', 'Tesco Stores 6601', -4.25, 0, 'GBP', 'COMPLETED', 361.81],
    ['CARD_PAYMENT', 'Current', '2023-01-30 13:41:48', '2023-01-31 19:32:36', 'Lidl Gb London', -8.12, 0, 'GBP', 'COMPLETED', 343.69],
    ['CARD_PAYMENT', 'Current', '2023-01-30 11:55:40', '2023-01-31 19:55:25', 'E5 Bakehouse Canning T', -12.36, 0, 'GBP', 'COMPLETED', 331.33],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Amznmktplace', -17.07, 0, 'GBP', 'COMPLETED', 555.43],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Starbucks', -3.95, 0, 'GBP', 'COMPLETED', 551.48],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Tfl Travel Charge', -2.6, 0, 'GBP', 'COMPLETED', 548.88],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Millennium Mini Store', -5, 0, 'GBP', 'COMPLETED', 543.88],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'cm.com', -253, 0, 'GBP', 'COMPLETED', 290.88],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Katsute100', -12.25, 0, 'GBP', 'COMPLETED', 278.63],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Ubr* Pending.uber.com', -13.66, 0, 'GBP', 'COMPLETED', 264.97],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Ubr* Pending.uber.com', -7.03, 0, 'GBP', 'COMPLETED', 257.94],
    ['CARD_PAYMENT', 'Current', '30-02-2023 11:55:40', '02-02-2023 11:55:40', 'Starbucks', -3.9, 0, 'GBP', 'COMPLETED', 254.04]
]

columns = ['Type', 'Product', 'Started Date', 'Completed Date', 'Description', 'Amount', 'Fee', 'Currency', 'State', 'Balance']

df = pd.DataFrame(data=data, columns=columns)


# In[ ]:


#clean df

df = df[['Completed Date', 'Description', 'Amount']] #keep only desired columns
df['Description'] = df['Description'].map(str.lower) #lower case of descriptions

df = df.rename(columns={'Completed Date': 'Date'})   #rename columns
df['Category'] = 'unassigned'                        #add category column

df.head()


# In[ ]:


#define all categories

    # Self-Care
    # Fines
    # Lore So What
    # Coffee
    # Groceries
    # Shopping
    # Restaurants
    # Transport
    # Travel
    # Entertainment
    # Gifts
    # Services
    # Excluded


# In[ ]:


#Assign transactions to the correct category

# Self-Care

df['Category'] = np.where(df['Description'].str.contains(
    'cash at tesco old st h exp|boots|royal'), 
    'Self-Care', df['Category'] )
    
# Fines

df['Category'] = np.where(df['Description'].str.contains(
    'car rental'), 
    'Fines', df['Category'] )
    
# Lore So What

df['Category'] = np.where(df['Description'].str.contains(
    'tubebuddy|itunes|dario|calendly|canva|epidemic|upwork|lada'), 
    'LoreSoWhat', df['Category'] )
    
# Coffee

df['Category'] = np.where(df['Description'].str.contains(
    'lavelle|hart|starbucks|barista|new road|mama shelter'), 
    'Coffee', df['Category'] )
    
# Shopping
    
df['Category'] = np.where(df['Description'].str.contains(
    'islington|at camden town'), 
    'Shopping', df['Category'] )
    
# Restaurants

df['Category'] = np.where(df['Description'].str.contains(
    'bakehouse|zettle|caravan|kod|eating|o ver|mcdonald|manteca|wine house|giacomo|real greek|restaurant|katsute|tonkotsu|zia lucia|viet|change please|me zhi chua|osm'), 
    'Restaurants', df['Category'] )
        
# Entertainment
    
df['Category'] = np.where(df['Description'].str.contains(
    'montys|urban|oshveda|egg|francesco|budgens whitechapel'), 
    'Entertainment', df['Category'] )
    
# Gifts
    
df['Category'] = np.where(df['Description'].str.contains(
    'gucci|blomma'), 
    'Gifts', df['Category'] )
    
# Services
    
df['Category'] = np.where(df['Description'].str.contains(
    'apple|snappy|exchanged to usd'), 
    'Services', df['Category'] )
    
# Excluded
    
df['Category'] = np.where(df['Description'].str.contains(
    'from|paypal|amznmktplace|starnow|refund|giffgaff|backstage|hectagon|tower hamlets bc|sweet suites|temporary hold|cm.com'), 
    'Excluded', df['Category'] )

# Groceries

df['Category'] = np.where(df['Description'].str.contains(
    'tesco|sainsbury|asda|lidl|toogoodtog|nisa|market|millennium mini store'), 
    'Groceries', df['Category'] )

# Transport
    
df['Category'] = np.where(df['Description'].str.contains(
    'uber|zipcar|bird|tfl|Ewa'), 
    'Transport', df['Category'] )
    
# Travel
    
df['Category'] = np.where(df['Description'].str.contains(
    'ryanair|easyjet|airways'), 
    'Travel', df['Category'] )

# Convert the "Date" column to a datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract the month and year information
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
    
pd.options.display.max_rows = 999
df.head(200)


# In[ ]:


#check unassigned transactions and confirm all transactions are assigned to a category

unassigned = df.loc[df['Category'] == 'unassigned']
unassigned


# ## Create Top Banner for a summary of last month's income, recurring expenses, non-recurring expenses and savings

# In[ ]:


# Get the latest month and year
latest_month = df['Month'].max()
latest_year = df['Year'].max()

# Filter the dataframe to include only transactions from the latest month
last_month_expenses = df[(df['Month'] == latest_month) & (df['Year'] == latest_year)]


# In[ ]:


last_month_expenses = last_month_expenses.groupby('Category')['Amount'].sum().reset_index()

last_month_expenses['Amount']=last_month_expenses['Amount'].astype('str')
last_month_expenses['Amount']=last_month_expenses['Amount'].str.replace('-','')
last_month_expenses['Amount']=last_month_expenses['Amount'].astype('float')        #get absolute figures

last_month_expenses = last_month_expenses[last_month_expenses["Category"].str.contains("Excluded|unassigned") == False]    #exclude "excluded" category
last_month_expenses = last_month_expenses.sort_values(by='Amount', ascending=False)    #sort values
last_month_expenses['Amount'] = last_month_expenses['Amount'].round().astype(int)      #round values

last_month_expenses


# In[ ]:


last_month_expenses_tot = last_month_expenses['Amount'].sum()
last_month_expenses_tot


# In[ ]:


def calculate_difference(event):
    income = float(income_widget.value)
    recurring_expenses = float(recurring_expenses_widget.value)
    monthly_expenses = float(monthly_expenses_widget.value)
    difference = income - recurring_expenses - monthly_expenses
    difference_widget.value = str(difference)

income_widget = pn.widgets.TextInput(name="Income", value="0")
recurring_expenses_widget = pn.widgets.TextInput(name="Recurring Expenses", value="0")
monthly_expenses_widget = pn.widgets.TextInput(name="Non-Recurring Expenses", value=str(last_month_expenses_tot))
difference_widget = pn.widgets.TextInput(name="Last Month's Savings", value="0")

income_widget.param.watch(calculate_difference, "value")
recurring_expenses_widget.param.watch(calculate_difference, "value")
monthly_expenses_widget.param.watch(calculate_difference, "value")

#pn.Row(income_widget, recurring_expenses_widget, monthly_expenses_widget, difference_widget).show()


# 
# ## Create last month expenses bar chart 

# In[ ]:


last_month_expenses_chart = last_month_expenses.hvplot.bar(
    x='Category', 
    y='Amount', 
    height=250, 
    width=850, 
    title="Last Month Expenses",
    ylim=(0, 500))

last_month_expenses_chart


# ## Create monthly expenses trend bar chart 

# In[ ]:


df['Date'] = pd.to_datetime(df['Date'])            # convert the 'Date' column to a datetime object
df['Month-Year'] = df['Date'].dt.to_period('M')    # extract the month and year from the 'Date' column and create a new column 'Month-Year'
monthly_expenses_trend_by_cat = df.groupby(['Month-Year', 'Category'])['Amount'].sum().reset_index()

monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].astype('str')
monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].str.replace('-','')
monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].astype('float')
monthly_expenses_trend_by_cat = monthly_expenses_trend_by_cat[monthly_expenses_trend_by_cat["Category"].str.contains("Excluded") == False]

monthly_expenses_trend_by_cat = monthly_expenses_trend_by_cat.sort_values(by='Amount', ascending=False)
monthly_expenses_trend_by_cat['Amount'] = monthly_expenses_trend_by_cat['Amount'].round().astype(int)
monthly_expenses_trend_by_cat['Month-Year'] = monthly_expenses_trend_by_cat['Month-Year'].astype(str)
monthly_expenses_trend_by_cat = monthly_expenses_trend_by_cat.rename(columns={'Amount': 'Amount '})

monthly_expenses_trend_by_cat


# In[17]:


#Define Panel widget

select_category1 = pn.widgets.Select(name='Select Category', options=[
    'All',
    'Self-Care',
    'Fines',
    'LoreSoWhat',
    'Coffee',
    'Groceries',
    'Shopping',
    'Restaurants',
    'Transport',
    'Travel',
    'Entertainment',
    'Gifts',
    'Services',
    #'Excluded'
])

select_category1


# In[18]:


# define plot function
def plot_expenses(category):
    if category == 'All':
        plot_df = monthly_expenses_trend_by_cat.groupby('Month-Year').sum()
    else:
        plot_df = monthly_expenses_trend_by_cat[monthly_expenses_trend_by_cat['Category'] == category].groupby('Month-Year').sum()
    plot = plot_df.hvplot.bar(x='Month-Year', y='Amount ')
    return plot

# define callback function
@pn.depends(select_category1.param.value)
def update_plot(category):
    plot = plot_expenses(category)
    return plot

# create layout
monthly_expenses_trend_by_cat_chart = pn.Row(select_category1, update_plot)
monthly_expenses_trend_by_cat_chart[1].width = 600

monthly_expenses_trend_by_cat_chart


# ## Create summary table

# In[19]:


df = df[['Date', 'Category', 'Description', 'Amount']]
df['Amount']=df['Amount'].astype('str')
df['Amount']=df['Amount'].str.replace('-','')
df['Amount']=df['Amount'].astype('float')        #get absolute figures

df = df[df["Category"].str.contains("Excluded") == False]    #exclude "excluded" category
df['Amount'] = df['Amount'].round().astype(int)      #round values
df


# In[20]:


# Define a function to filter the dataframe based on the selected category
def filter_df(category):
    if category == 'All':
        return df
    return df[df['Category'] == category]

# Create a DataFrame widget that updates based on the category filter
summary_table = pn.widgets.DataFrame(filter_df('All'), height = 300,width=400)

# Define a callback that updates the dataframe widget when the category filter is changed
def update_summary_table(event):
    summary_table.value = filter_df(event.new)

# Add the callback function to the category widget
select_category1.param.watch(update_summary_table, 'value')

summary_table


# ## Create Final Dashboard

# In[21]:


template = pn.template.FastListTemplate(
    title="Personal Finances Summary",
    sidebar=[
        pn.pane.Markdown("## *If you can't manage your money, making more won't help*"),
        pn.pane.PNG('vecteezy_pack-of-dollars-money-clipart-design-illustration_9303600_278.png', sizing_mode='scale_both'),
        pn.pane.Markdown(""),
        pn.pane.Markdown(""),
        select_category1
    ],
    main=[
        pn.Row(income_widget, recurring_expenses_widget, monthly_expenses_widget, difference_widget, width=950),
        pn.Row(last_month_expenses_chart, height=240),
        pn.GridBox(
            monthly_expenses_trend_by_cat_chart[1],
            summary_table,
            ncols=2,
            width=500,  
            align='start',
            sizing_mode='stretch_width'
        )
    ]
)

template.show()
