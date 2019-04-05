##1 importing libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

##2 creating pdDataFrame
kick_ds = pd.read_csv(r"C:\Users\aleks\Documents\9_TU_Wien\4_Machine_Learning\kick_dataset\kick.csv")

##3 cleaning pdDataFrame
# transforming empty cells to no data values
cols=kick_ds.columns
for elem in cols:
    kick_ds[elem] = kick_ds[elem].replace("?", np.nan)
# transforming dtypes (object dtype to int, float, date, categorical) 
num_cols=["VehYear", "VehicleAge", "VehOdo", "MMRAcquisitionAuctionAveragePrice", \
    "MMRAcquisitionAuctionCleanPrice", "MMRAcquisitionRetailAveragePrice", "MMRAcquisitonRetailCleanPrice", \
        "MMRCurrentAuctionAveragePrice", "MMRCurrentAuctionCleanPrice", "MMRCurrentRetailAveragePrice", \
            "MMRCurrentRetailCleanPrice", "BYRNO", "VehBCost", "WarrantyCost"]
cat_cols=["IsBadBuy", "Auction", "Make", "Model", "Trim", "SubModel", "Color", \
    "Transmission", "WheelTypeID", "WheelType", "Nationality", "Size", "TopThreeAmericanName", \
        "PRIMEUNIT", "AUCGUART", "VNZIP1", "VNST", "IsOnlineSale"]
str_cols=["Auction", "Make", "Model", "Trim", "SubModel", "Color", \
    "Transmission", "WheelType", "Nationality", "Size", "TopThreeAmericanName", \
        "PRIMEUNIT", "AUCGUART", "VNST"] #str_cols is the subset of cat_cols, the ones being a text

for elem in num_cols:
    kick_ds[elem] = pd.to_numeric(kick_ds[elem])

for elem in cat_cols:
    kick_ds[elem] = kick_ds[elem].astype("category")

kick_ds["PurchDate"] = pd.to_datetime(kick_ds["PurchDate"])

# converting all categorical string (text) values to uppercase
for elem in str_cols:
    kick_ds[elem] = kick_ds[elem].str.upper()

##4 info about each feature
# feature's data type
print(kick_ds.dtypes)
# number of missing values in each feature
mv = kick_ds.isna().sum()
print(mv)
# statistics for numeric features
print(kick_ds.describe())
# statistics for category features
print(kick_ds[cat_cols].describe())

##5 general info about the dataset
# number of samples
n_samples = kick_ds.shape[0]
print(n_samples)
# number of features (attributes)
n_att = kick_ds.shape[1]
print(n_att)
# number of classes == unique values in the selected attribute 
n_cl = kick_ds.loc[:,"IsBadBuy"].unique().shape[0]
print(n_cl)
# missing values => how many mv present in ds, in how many features
print(np.sum(mv))
print(mv[mv.values!=0].shape[0])

##6 graphs
# graphs for category features - "IsBadBuy" and "Make"
prop_tables = []
for variable in cat_cols:
    tab = pd.crosstab(kick_ds[variable], columns="count")
    rel_tab = tab/tab.sum()
    prop_tables.append(rel_tab)

print(prop_tables[0])
print(prop_tables[2])

prop_tables[0].plot(kind="bar",title="Relative frequency of IsBadBuy")
prop_tables[2].plot(kind="bar", title="Relative frequency of Make")

# graphs for numeric features - "VehOdo" and "VehBCost"
kick_ds.VehOdo.plot(kind="hist", title="Distribution of vehicles' odometer readings", bins = 20)
kick_ds.VehBCost.plot(kind="box", title="Distribution of vehicles' prices")
plt.show()