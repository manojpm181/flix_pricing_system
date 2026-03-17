import requests
import pandas as pd
import io

def load_from_sharepoint(url):
    try:
        print("📥 Downloading file...")

        # Add download flag
        if "download=1" not in url:
            url = url + "&download=1"

        response = requests.get(url)

        if response.status_code != 200:
            print("❌ Failed to download. Status:", response.status_code)
            return None

        file_bytes = io.BytesIO(response.content)

        df = pd.read_excel(file_bytes)

        print("✅ File loaded successfully!")
        return df

    except Exception as e:
        print("❌ Error:", e)
        return None