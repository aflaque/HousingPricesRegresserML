import pandas as pd

df= pd.read_csv("india_housing_prices.csv")

#first upload the dataset, create one df, by using the below code
test_df = df.sample(n=10000, random_state=42)

#then do
target = test_df["Price_in_Lakhs"]
feature_data = test_df.drop(columns=['Price_in_Lakhs'])


#to save as a csv file
target.to_csv("target.csv", index=False)
feature_data.to_csv("feature.csv", index=False)