import gradio as gr
from csv_handler import upload_csv_file
from graph_generator import create_visual
from query_processor import analyze_csv_query

# Gradio Interfaces
csv_interface = gr.Interface(
    fn=upload_csv_file,
    inputs=gr.File(),
    outputs=["text", "dataframe"],
    title="📂 CSV Data Uploader",
    description="Upload a CSV file and explore its contents."
)

graph_interface = gr.Interface(
    fn=create_visual,
    inputs=[
        gr.Textbox(label="📊 X-axis Column"),
        gr.Textbox(label="📈 Y-axis Column"),
        gr.Radio(["Bar Chart", "Line Graph", "Scatter Plot", "Box Plot"], label="📍 Graph Type")
    ],
    outputs="image",
    title="📊 Data Graph Generator",
    description="Select column names and chart type to visualize data."
)

query_interface = gr.Interface(
    fn=analyze_csv_query,
    inputs=gr.Textbox(placeholder="🔎 Ask about your dataset..."),
    outputs="text",
    title="💡 CSV Data Insights",
    description="Enter a question and get AI-generated insights from your data."
)

def main():
    gr.TabbedInterface(
        [csv_interface, graph_interface, query_interface],
        ["📂 Upload CSV", "📊 Generate Graph", "🔎 Analyze Data"]
    ).launch()

if __name__ == "__main__":
    main()
