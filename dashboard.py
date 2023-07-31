import streamlit as st
import pandas as pd
import plotly.express as px

# Disable the warning about pyplot global use
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="My Dashboard", page_icon=':bar_chart:', layout='wide')

def plot_chart(data, x_column, y_column, chart_type):
    if chart_type == "Line Plot":
        fig = px.line(data, x=x_column, y=y_column)
    elif chart_type == "Bar Plot":
        fig = px.bar(data, x=x_column, y=y_column)
    elif chart_type == "Scatter Plot":
        fig = px.scatter(data, x=x_column, y=y_column)
    elif chart_type == "Histogram":
        fig = px.histogram(data, x=x_column)
    elif chart_type == "Box Plot":
        fig = px.box(data, x=x_column, y=y_column)
    elif chart_type == "Heatmap":
        fig = px.imshow(data.corr())
    elif chart_type == "Pie Chart":
        fig = px.pie(data, values=y_column, names=x_column)
    elif chart_type == "3D Scatter Plot":
        fig = px.scatter_3d(data, x=x_column, y=y_column, z='Another_Column')
    
    # Display the Plotly figure
    st.plotly_chart(fig)

def main():
    st.title("Logatta Dashboard")

    uploaded_file = st.file_uploader("Upload a dataset file", type=["csv", "xlsx", "xls"])

    if uploaded_file is not None:
        # Determine the file extension of the uploaded file
        file_extension = uploaded_file.name.split(".")[-1]

        if file_extension in ["csv", "xlsx", "xls"]:
            # Read the uploaded dataset based on its extension
            if file_extension == "csv":
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file, engine='openpyxl')

            # Show the DataFrame in the dashboard
            st.subheader("Preview of the Dataset")
            st.dataframe(data)

            columns = st.sidebar.multiselect("Select Columns", data.columns.tolist())

            if columns:
                chart_type = st.sidebar.selectbox("Select Chart Type", [
                    "Line Plot", "Bar Plot", "Scatter Plot", "Histogram",
                    "Box Plot", "Heatmap", "Pie Chart", "3D Scatter Plot"
                ])

                if len(columns) >= 2:
                    x_column = st.sidebar.selectbox("Select X-axis Column", columns)
                    y_column = st.sidebar.selectbox("Select Y-axis Column", columns)
                    filtered_data = data[columns]
                    plot_chart(filtered_data, x_column, y_column, chart_type)
                else:
                    st.warning("Please select at least two columns for the chart.")
            else:
                st.warning("Please select columns to visualize.")
        else:
            st.warning("Invalid file format. Please upload a CSV, Excel (xlsx), or Excel (xls) file.")

if __name__ == "__main__":
    main()
