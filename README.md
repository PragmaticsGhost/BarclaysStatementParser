# PDF to CSV Transaction Converter

This project is a Python script that extracts transaction data from Barclays Luxury Card credit card statement .PDFs and converts the data into .CSV files.

There is currently no way to organize large amounts of Luxury Card statement data, as it annoyingly can only be exported via a .PDF (or the last 90 days of activity in .CSV). 

This script supports processing multiple PDFs at once, and merges the results into a single CSV file.

## Features

- **Extracts transaction data** from Barclays Luxury Card Credit Card statement PDFs, including transaction date, posting date, description, points (optional), and amount.
- **Processes multiple PDF files at once** and converts each into a corresponding CSV file.
- **Merges all output CSV files** into one consolidated CSV file containing all transactions.
- **Handles missing "points" field** ensures correct formatting for CSV output.

## Requirements

- Python 3.x
- The following Python libraries:
  - `textract`: For extracting text from PDFs.
  - `re`: For parsing transaction patterns using regular expressions.
  - `pandas`: For saving the parsed data into CSV files.

### Installation

Clone the repository:
```
git clone https://github.com/PragmaticsGhost/BarclaysStatementParser.git
```
Install the required Python libraries:
```
pip install textract pandas
```

## Usage

Modify the script to point to the folder that your PDF statements are in, and an output folder for the CSV files.

Run the script from your terminal:
```
python3 barclays_statement_parser.py
```
## Parameters

pdf_folder: The directory where your PDF statements are located in.

output_folder: The directory where the individual CSV files will be saved.

merged_csv: The file path for the final merged CSV file containing all transactions.

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

## Contributing
Feel free to submit pull requests or raise issues. Contributions are welcome!
