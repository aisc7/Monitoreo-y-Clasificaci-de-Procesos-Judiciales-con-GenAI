import csv

def extract_data_from_csv(csv_path):
    """
    Extract data from a CSV file
    
    Args:
        csv_path: Path to the CSV file
    
    Returns:
        list: List of rows, where each row is a list of values
    """
    data = []
    
    try:
        with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                data.append(row)
        
        return data
    
    except UnicodeDecodeError:
        # Try with a different encoding if UTF-8 fails
        with open(csv_path, 'r', newline='', encoding='latin-1') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                data.append(row)
        
        return data
    
    except Exception as e:
        # Log the error and return an empty list
        print(f"Error extracting data from CSV: {str(e)}")
        return []