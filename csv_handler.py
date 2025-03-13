import pandas as pd

dataset = None
columns_available = []

def upload_csv_file(file):
    global dataset, columns_available
    if not file:
        return "⚠ No file provided.", None
    try:
        df = pd.read_csv(file.name)
        dataset = df
        columns_available = df.columns.tolist()
        
        if df.empty:
            return "⚠ The CSV file is empty.", None
        
        missing_count = df.isnull().sum().sum()
        column_details = df.dtypes.to_json()
        preview = df.sample(n=min(5, len(df)))
        
        message = f"✅ CSV uploaded successfully!\n"
        message += f"🔍 Missing Values: {missing_count}\n"
        message += f"📊 Column Details: {column_details}"
        
        return message, preview
    except Exception as error:
        return f"❌ Error reading file: {str(error)}", None
