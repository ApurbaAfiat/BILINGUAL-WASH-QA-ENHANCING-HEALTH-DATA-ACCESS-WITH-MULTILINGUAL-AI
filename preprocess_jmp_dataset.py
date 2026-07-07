import pandas as pd


df = pd.read_csv("combined_jmp_wash_dataset.csv")

# Drop irrelevant unnamed columns
df.drop(columns=[col for col in df.columns if "unnamed" in col.lower()], errors='ignore', inplace=True)

# Step 1: Combining all possible versions of key fields
df["country_name"] = df.get("country_name").combine_first(df.get("country"))
df["indicator_name"] = df.get("indicator_name").combine_first(df.get("indicator"))
df["value"] = df.get("value").combine_first(df.get("obs_value"))
df["value"] = df["value"].combine_first(df.get("observation_value"))
df["year"] = df.get("year").combine_first(df.get("time_period"))

# Step 2: Clean 'value' field
def parse_numeric(val):
    if isinstance(val, str):
        val = val.strip().replace("<", "").replace(">", "").replace("-", "").replace(",", "")
        try:
            return float(val)
        except ValueError:
            return None
    return val

df["value"] = df["value"].apply(parse_numeric)

# Step 3: Merge and clean residence/service columns
df["service_level"] = df.get("service_level").combine_first(df.get("service type"))
df["residence"] = df.get("residence").combine_first(df.get("residence_type"))

# Step 4: Final subset and cleanup
df_final = df[["country_name", "indicator_name", "year", "value", "service_level", "residence", "source"]].copy()
df_final.dropna(subset=["country_name", "indicator_name", "year", "value"], inplace=True)
df_final.reset_index(drop=True, inplace=True)

# output
df_final.to_csv("final_cleaned_jmp_dataset.csv", index=False)
print("Final cleaned dataset saved as 'final_cleaned_jmp_dataset.csv'")
