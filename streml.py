import streamlit as st
import pandas as pd

def generate_pivot_table(df, index_cols, column, values, agg_funcs):
    pivot_table = pd.pivot_table(df, index=index_cols, columns=column, values=values, aggfunc=agg_funcs, fill_value=0, margins=True, margins_name='Grand Total')
    return pivot_table

def main():
    st.title("Pivot Table Generator")
    
    uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx'])
    if uploaded_file is not None:
        try:
            sheets = pd.ExcelFile(uploaded_file).sheet_names
            sheet_name = st.selectbox("Select a sheet", sheets)
            if sheet_name:
                df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
                columns = df.columns.tolist()
                
                index_cols = st.multiselect("Select index column(s)", columns)
                column = st.selectbox("Select a column for columns", columns)
                values = st.selectbox("Select a column for values", columns)
                agg_funcs = ['sum', 'mean', 'count', 'min', 'max']
                selected_agg_funcs = st.multiselect("Select aggregation functions", agg_funcs)
                if st.button("Generate Pivot Table"):
                    pivot_table = generate_pivot_table(df, index_cols, column, values, selected_agg_funcs)
                    
                    st.write(pivot_table)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
