import streamlit as st
import pandas as pd
# from joblib import load
import pickle
import numpy as np
from st_pages import Page, show_pages
import gzip

st.set_page_config(
    page_title="AuditWatch",
    page_icon="🔍",
)

# Create menu pages
pages = [
    Page("1_AuditWatch.py", 'AuditWatch', "🔍"),
    Page("pages/2_Tutorial.py", 'Tutorial', "📚"),
    Page("pages/3_Tentang.py", 'Tentang', "ℹ️")
]

# Show the menu pages
show_pages(pages)

# # Load the pre-trained SelectKBest model
# selector_filename = "model/selectkbest_model.pkl"
# selector = load(selector_filename)

# # Load the pre-trained ensemble model
# model_filename = 'model/ensemble_model.pkl'
# ensemble = load(model_filename)

    # Load the pre-trained SelectKBest model
selector_filename = 'model/selectkbest_model.pkl'
selector = pickle.load(selector_filename)


# Load the pre-trained ensemble model
model_filename = 'model/ensemble.gz'
with gzip.open(model_filename, 'rb') as f:
    ensemble = pickle.load(f)

def preprocess_data(data, time_variable, account_variable, amount_variable):
    time = time_variable
    sender = account_variable
    amount = amount_variable
    
    # Mengubah format Timestamp menjadi tipe data datetime
    data[time] = pd.to_datetime(data[time]).dt.date
    
    # Aggregated data by 'Account' and day 'Timestamp' variables
    aggregated_data = data.groupby([sender, time]).agg({
        amount: 'sum',
        'Is Laundering': 'max'
    }).reset_index()
    
    # Extract 'transaction' count by 'Account' and add it to aggregated data
    transaction_count = data.groupby([sender, time]).size().reset_index(name='transaction')
    aggregated_data = pd.merge(aggregated_data, transaction_count, on=[sender, time])
    
    def calculate_digit_distribution(value):
        first_digit = str(value)[0]
        return int(first_digit)
    
    data['First Digit'] = data[amount].apply(calculate_digit_distribution)
    digit_distribution = data.groupby([sender, time, 'First Digit']).size().unstack(fill_value=0)
    digit_distribution = digit_distribution.div(digit_distribution.sum(axis=1), axis=0)
    
    # Add the digit distributions as new variables in aggregated data
    for digit in range(1, 10):
        variable_name = f'{digit}_dist'
        aggregated_data[variable_name] = digit_distribution.loc[:, digit].values
    
    # Calculate the Euclidean distance between the first digit distributions and Benford's Law
    benfords_law  = [0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]
    
    # Extract Euclidean distance from first digit distribution to Benford's Law
    for digit in range(1, 10):
        dist_col = f'{digit}_dist'
        benford_prob = benfords_law[digit - 1]
        aggregated_data[f'{digit}_ed'] = np.sqrt((aggregated_data[dist_col] - benford_prob) ** 2)
    
    # Calculate standard deviation for each row
    for digit in range(1, 10):
        aggregated_data[f'{digit}_sd'] = np.abs(aggregated_data[f'{digit}_dist'].fillna(0) - benfords_law[digit - 1]) / np.sqrt(benfords_law[digit - 1] * (1 - benfords_law[digit - 1]))
    
    input_vars = [amount, 'transaction', '1_dist', '2_dist', '3_dist', '4_dist', '5_dist', '6_dist',
                  '7_dist', '8_dist', '9_dist', '1_ed', '2_ed', '3_ed', '4_ed', '5_ed', '6_ed', '7_ed', '8_ed', '9_ed',
                  '1_sd', '2_sd', '3_sd', '4_sd', '5_sd', '6_sd', '7_sd', '8_sd', '9_sd']
    X = aggregated_data[input_vars]
    
    # Reduce the feature space using SelectKBest feature selection
    X_reduced = selector.transform(X)
    
    return X_reduced, aggregated_data

def analyze_data(data):
    try:
        # Perform preprocessing
        X_reduced, aggregated_data = preprocess_data(data, time_variable, account_variable, amount_variable)

        # Make predictions using the ensemble model
        y_pred = ensemble.predict(X_reduced)

        # Merge results with the original data
        merged_result = pd.concat([aggregated_data, pd.DataFrame({'y_pred': y_pred})], axis=1)

        # Filter the data for suspicious transactions
        filtered_result = merged_result[merged_result['y_pred'] == 1]

        # Aggregate the results
        result = filtered_result.groupby(account_variable).agg({'Timestamp': list}).reset_index()
        result.columns = ['Account', 'Tanggal Pencucian Uang']
        
        # Convert the date format to regular text
        result['Tanggal Pencucian Uang'] = result['Tanggal Pencucian Uang'].apply(lambda x: ', '.join([str(date)[:10] for date in x]))

        return result, merged_result
    except KeyError:
        st.error('Kesalahan: Kolom yang dipilih tidak valid dalam data. Silakan pilih kolom yang sesuai.')
    except Exception as e:
        st.error(f'Kesalahan: {str(e)}')

st.title('AuditWatch')
st.subheader('Unggah Data Transaksi Perbankan')

# File upload
uploaded_file = st.file_uploader('Pilih berkas CSV atau Excel', type=['csv', 'xlsx'])

if uploaded_file is not None:
    st.success('Berkas sukses diunggah.')

    # Read the uploaded file
    data = pd.read_csv(uploaded_file)  # Assuming the uploaded file is a CSV

    # User input for variable selection
    st.subheader('Pilih kolom yang sesuai')

    # Variable selection - Column 1
    col1, col2, col3 = st.columns(3)
    with col1:
        time_variable = st.selectbox('Kolom Waktu', data.columns)
        
    with col2:
        account_variable = st.selectbox('Kolom Akun', data.columns)
    
    with col3:
        amount_variable = st.selectbox('Kolom Jumlah', data.columns)

    # Analyze button
    if st.button('Analisis'):
        with st.spinner('Sedang menganalisis...'):
            result, merged_result = analyze_data(data)
            st.success('Analisis selesai.')

            # Display analysis result
            st.subheader('Hasil Analisis')

            # Rename 'y_pred' column
            merged_result.rename(columns={'y_pred': 'Pencucian Uang'}, inplace=True)
            
            # Map values in 'Pencucian Uang' column
            merged_result['Pencucian Uang'] = merged_result['Pencucian Uang'].map({0: 'Non Pelaku', 1: 'Pelaku'})

            # Split result into two columns
            col1, col2 = st.columns(2)

            # Column 1 - Analysis Result table
            result_container = col1.empty()  # Empty container for the result
            result_container.dataframe(result)

            # Column 2 - Bar graph
            chart_container = col2.empty()  # Empty container for the chart
            chart_container.subheader('Jumlah Transaksi')
            counts = merged_result['Pencucian Uang'].value_counts()
            chart_container.bar_chart(counts)

            # Download button for analysis results
            csv = result.to_csv(index=False)
            download_button = st.download_button(
                label="Unduh Hasil Analisis (CSV)",
                data=csv,
                file_name='Hasil Analisis AuditWatch.csv',
                mime='text/csv'
            )

            # Check if the download button is clicked
            if download_button:
                # Update the containers with the result and chart
                result_container.dataframe(result)
                chart_container.subheader('Jumlah Transaksi')
                chart_container.bar_chart(counts)
                
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
