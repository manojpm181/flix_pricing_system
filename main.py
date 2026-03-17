
import pandas as pd
import os

from src.sharepoint_loader import load_from_sharepoint
from src.preprocess import preprocess
from src.clustering import create_clusters
from src.pricing import pricing_analysis


def run_pipeline():
    print("🚀 Starting pipeline...")

    url = "https://einfachbusfahren-my.sharepoint.com/:x:/g/personal/kishor_sivakumar_flix_com/IQAvXhePXMWqRbEVHYE3ADA6ASgC7QuoyaL2-muStPOjnOQ?e=TkjKdL"

    df = load_from_sharepoint(url)

    if df is None:
        print("❌ Failed to load dataset!")
        return

    print("✅ Data Loaded:", df.shape)

    # ---------------- PROCESS ----------------
    df = preprocess(df)
    df = create_clusters(df)
    df = pricing_analysis(df)

    # ---------------- EXTRA FEATURES ----------------
    df['comparable_buses'] = df.groupby('cluster')['route_number'] \
        .transform(lambda x: ', '.join(map(str, x.unique())))

    # ---------------- OUTPUT ----------------
    df_output = df[[
        'route_number', 'operator', 'bus_type', 'price',
        'median_price', 'flag', 'cluster', 'comparable_buses'
    ]]

    # ---------------- SPLIT ----------------
    df_flagged = df_output[df_output['flag'] != "OK"]
    df_sample = df_output.sample(min(5000, len(df_output)), random_state=42)

    summary = df_output['flag'].value_counts().reset_index()
    summary.columns = ['Flag', 'Count']

    # ---------------- SAVE (CSV ONLY) ----------------
    os.makedirs("outputs", exist_ok=True)

    df_flagged.to_csv("outputs/flagged_cases.csv", index=False)
    df_sample.to_csv("outputs/sample_data.csv", index=False)
    summary.to_csv("outputs/summary.csv", index=False)

    print("🎉 DONE! Files saved in outputs/")


if __name__ == "__main__":
    run_pipeline()
# import pandas as pd
# import os
# os.environ["TEMP"] = "D:\\temp"
# os.environ["TMP"] = "D:\\temp"
# from openpyxl import load_workbook
# from openpyxl.chart import BarChart, Reference
# from openpyxl.styles import PatternFill, Font
# from openpyxl.utils import get_column_letter

# from src.sharepoint_loader import load_from_sharepoint
# from src.preprocess import preprocess
# from src.clustering import create_clusters
# from src.pricing import pricing_analysis


# def run_pipeline():
#     print("🚀 Starting pipeline...")

#     url = "https://einfachbusfahren-my.sharepoint.com/:x:/g/personal/kishor_sivakumar_flix_com/IQAvXhePXMWqRbEVHYE3ADA6ASgC7QuoyaL2-muStPOjnOQ?e=TkjKdL"

#     df = load_from_sharepoint(url)

#     if df is None:
#         print("⚠️ Failed to load dataset!")
#         return

#     print("✅ Data Loaded:", df.shape)

#     df = preprocess(df)
#     df = create_clusters(df)
#     df = pricing_analysis(df)

    
#     df['comparable_buses'] = df.groupby('cluster')['route_number'] \
#         .transform(lambda x: ', '.join(map(str, x.unique())))

#     df_output = df[[
#         'route_number','operator','bus_type','price',
#         'median_price','flag','cluster','comparable_buses'
#     ]]

#     df_flagged = df_output[df_output['flag'] != "OK ✅"]
#     df_sample = df_output.sample(min(5000, len(df_output)), random_state=42)

#     summary = df_output['flag'].value_counts().reset_index()
#     summary.columns = ['Flag', 'Count']

   
#     file_path = "outputs/results.xlsx"

#     with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
#         df_flagged.to_excel(writer, sheet_name="Flagged Cases", index=False)
#         df_sample.to_excel(writer, sheet_name="Sample Data", index=False)
#         summary.to_excel(writer, sheet_name="Summary", index=False)

    
#     wb = load_workbook(file_path)

#     ws = wb["Flagged Cases"]

#     for col in ws.columns:
#         max_length = 0
#         col_letter = get_column_letter(col[0].column)

#         for cell in col:
#             if cell.value:
#                 max_length = max(max_length, len(str(cell.value)))

#             if col_letter == "G":
#                 if cell.value == "HIGH 🚨":
#                     cell.fill = PatternFill(start_color="FF9999", fill_type="solid")
#                 elif cell.value == "LOW 🔻":
#                     cell.fill = PatternFill(start_color="FFD580", fill_type="solid")
#                 elif cell.value == "OK ✅":
#                     cell.fill = PatternFill(start_color="90EE90", fill_type="solid")

#         ws.column_dimensions[col_letter].width = max_length + 2

#     for cell in ws[1]:
#         cell.font = Font(bold=True)

    
#     ws_summary = wb["Summary"]

#     chart = BarChart()
#     chart.title = "Pricing Anomaly Distribution"

#     data = Reference(ws_summary, min_col=2, min_row=1, max_row=ws_summary.max_row)
#     cats = Reference(ws_summary, min_col=1, min_row=2, max_row=ws_summary.max_row)

#     chart.add_data(data, titles_from_data=True)
#     chart.set_categories(cats)

#     ws_summary.add_chart(chart, "E2")

#     wb.save(file_path)

#     print("🎉 DONE! Excel with charts ready!")


# if __name__ == "__main__":
#     run_pipeline()