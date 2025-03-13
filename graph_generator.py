import matplotlib.pyplot as plt
from csv_handler import dataset

def create_visual(x_axis, y_axis, graph_type):
    if dataset is None:
        return "⚠ No dataset available. Please upload a CSV first."
    try:
        plt.figure(figsize=(8, 5))
        
        if graph_type == "Bar Chart":
            plt.bar(dataset[x_axis], dataset[y_axis], color="blue")
        elif graph_type == "Line Graph":
            plt.plot(dataset[x_axis], dataset[y_axis], marker="o", linestyle="--", color="purple")
        elif graph_type == "Scatter Plot":
            plt.scatter(dataset[x_axis], dataset[y_axis], color="red", alpha=0.5)
        elif graph_type == "Box Plot":
            dataset[[y_axis]].boxplot()
        
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"{graph_type} of {y_axis} vs {x_axis}")
        plt.xticks(rotation=30)
        plt.grid(True)
        plt.savefig("chart_output.png")
        plt.close()
        return "chart_output.png"
    except Exception as error:
        return f"❌ Error creating graph: {str(error)}"
