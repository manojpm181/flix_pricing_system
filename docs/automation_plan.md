1. Data Ingestion:
   - Daily data from database or API

2. Processing:
   - Python pipeline (preprocessing + clustering)

3. Analysis:
   - Pricing anomaly detection

4. Storage:
   - Store results in database or cloud

5. Visualization:
   - Streamlit dashboard

6. Automation:
   - Cron job / Airflow scheduling

Tech Stack:
Python, Pandas, Scikit-learn, Streamlit, SQL, Cloud (AWS/GCP)

Similar buses are identified using KMeans clustering based on:
- Price
- Load (seat occupancy)
- Ratings (Bus Score)
- Number of Reviews
- Search Ranking Position

This ensures buses compared belong to similar demand, quality, and visibility segments.

Pricing anomalies are detected using median-based comparison:

- HIGH: Price > 120% of median of similar buses
- LOW: Price < 80% of median of similar buses

Median is used instead of mean to reduce effect of outliers.

