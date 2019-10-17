### Data Analysis Pipeline ###

# Get Data
reference:https://www.datacamp.com/community/tutorials/finance-python-trading
1.透過pandas_datareader抓線上資料
2.read_csv()

# Explore & Preprocess & Clean Data & Save Data to DB
head(),tail(),describe()
df.index,df.columns # df means Dataframe
ts = aapl['Close'][-10:] # Subset Dataframe
loc() and iloc() # you use the former for label-based indexing and the latter for positional indexing. 
                 # the most idiomatic way to do things with Pandas
EX:
print(aapl.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')].head())
print(aapl.loc['2007'].head(1))
print(aapl.iloc[22:43])
print(aapl.iloc[[22,43], [0, 3]])

sample(),resample(),asfreq()
EX:
sample = aapl.sample(20)
monthly_aapl = aapl.resample('M').mean()
aapl.asfreq("M", method="bfill")

aapl['diff'] = aapl.Open - aapl.Close # Add a column `diff` to `aapl` 
del aapl['diff'] # Delete the new `diff` column
type(ts)
to_csv()

# EDA(Explorary Data Analysis)

# Plot Data(visualize time series data)
import matplotlib.pyplot as plt
aapl['Close'].plot(grid=True)
plt.show()

# Define the problem

# Train the model

# Validation the model

# Deploy the application

