import pandas as pd
from csv_handler import dataset
from ai_agent import csv_helper

async def analyze_csv_query(user_input):
    if dataset is None:
        return "⚠ No dataset available. Please upload a CSV first."
    if not user_input.strip():
        return "⚠ Please enter a valid query."
    try:
        dataset_summary = dataset.describe().to_json()
        prompt = f"User Query: {user_input}\nDataset Overview:\n{dataset_summary}"
        response = await csv_helper.run(prompt)
        return response.output
    except Exception as error:
        return f"❌ Error processing query: {str(error)}"
