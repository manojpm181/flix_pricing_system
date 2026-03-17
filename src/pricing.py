import pandas as pd

def pricing_analysis(df: pd.DataFrame) -> pd.DataFrame:
    print("💰 Running pricing analysis...")

    p10 = df['price'].quantile(0.10)
    p90 = df['price'].quantile(0.90)
    median_price = df['price'].median()

    def flag(price):
        if pd.isna(price):
            return "UNKNOWN"
        elif price > p90:
            return "HIGH"
        elif price < p10:
            return "LOW"
        else:
            return "OK"

    df['flag'] = df['price'].apply(flag)

    df['median_price'] = median_price
    df['price_diff_%'] = ((df['price'] - median_price) / median_price) * 100
    df['price_diff_%'] = df['price_diff_%'].round(2)

    print("✅ Pricing analysis complete")

    return df

# import pandas as pd

# def pricing_analysis(df: pd.DataFrame) -> pd.DataFrame:
#     print("💰 Running pricing analysis (robust mode)...")


#     p10 = df['price'].quantile(0.10)
#     p90 = df['price'].quantile(0.90)
#     median_price = df['price'].median()

#     print(f"📊 P10: {p10}, P90: {p90}, Median: {median_price}")


#     def flag(price):
#         if pd.isna(price):
#             return "UNKNOWN"
#         elif price > p90:
#             return "HIGH"
#         elif price < p10:
#             return "LOW"
#         else:
#             return "OK"

#     df['flag'] = df['price'].apply(flag)


#     df['median_price'] = median_price
#     df['price_diff_%'] = ((df['price'] - median_price) / median_price) * 100

#     df['price_diff_%'] = df['price_diff_%'].round(2)

#     print("✅ Pricing analysis complete (stable)")

#     return df