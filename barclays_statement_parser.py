import textract
import re
import pandas as pd
import os

# Function to extract text from the PDF
def extract_text_from_pdf(pdf_path):
    text = textract.process(pdf_path, method='pdftotext', layout=True).decode('utf-8')
    return text

# Function to parse transactions from the extracted text
def parse_transactions(text):
    # Updated regex pattern that handles points properly
    transaction_pattern = re.compile(
        r'(?P<transaction_date>[A-Za-z]{3} \d{2})\s+'        # Match transaction date
        r'(?P<posting_date>[A-Za-z]{3} \d{2})\s+'            # Match posting date
        r'(?P<description>[\w\s\*\.\-,]+?)\s+'               # Match description (non-greedy to avoid matching points)
        r'(?P<points>\d{1,5})?\s*'                           # Match points (optional, max 5 digits)
        r'\$(?P<amount>[0-9,]+\.\d{2})'                      # Match the amount
    )
    
    transactions = []
    for match in transaction_pattern.finditer(text):
        transaction = match.groupdict()

        # Handle missing points by assigning an empty string
        if not transaction['points']:
            transaction['points'] = ''  # You can set it to '0' if preferred

        transactions.append(transaction)
    
    return transactions

# Function to save transactions to CSV
def save_to_csv(transactions, output_csv):
    df = pd.DataFrame(transactions)
    df.to_csv(output_csv, index=False)
    print(f"Transactions saved to {output_csv}")

# Main function to process multiple PDFs and save transactions to CSVs
def pdfs_to_csvs_and_merge(pdf_folder, output_folder, merged_csv):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # List to store dataframes for merging
    all_dataframes = []

    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            print(f"Processing {pdf_path}...")
            text = extract_text_from_pdf(pdf_path)
            transactions = parse_transactions(text)
            
            if transactions:
                # Create individual CSV for each PDF
                output_csv = os.path.join(output_folder, f"{os.path.splitext(pdf_file)[0]}.csv")
                save_to_csv(transactions, output_csv)
                
                # Read the CSV into a dataframe and store it in the list for merging
                df = pd.DataFrame(transactions)
                all_dataframes.append(df)
            else:
                print(f"No transactions found in {pdf_file}.")
    
    # Merge all dataframes into one and save as a single CSV file
    if all_dataframes:
        merged_df = pd.concat(all_dataframes, ignore_index=True)
        merged_df.to_csv(merged_csv, index=False)
        print(f"All transactions merged into {merged_csv}")
    else:
        print("No transactions to merge.")

# Run the script
pdf_folder = '/home/wntrb0y/Desktop/BC_Statements_2024'  # Folder containing your PDF files
output_folder = '/home/wntrb0y/Desktop/BC_Statements_2024'  # Folder to save the individual CSV files
merged_csv = '/home/wntrb0y/Desktop/BC_Statements_2024/2024_Transactions.csv'  # Output path for the merged CSV file
pdfs_to_csvs_and_merge(pdf_folder, output_folder, merged_csv)