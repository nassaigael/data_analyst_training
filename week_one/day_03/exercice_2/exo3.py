import csv

def read_csv(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
                print("CSV file read successfully.")
        except FileNotFoundError:
            print("Error: The specified file was not found.")
        
        
           
file_path_not_found = "non_existent_file.csv"
file_path_valid = "E:\\data_analyst\\week_one\\day_03\\exercice_1\\data\\csv\\average_scores.csv"
            
            
# Example usage:
read_csv(file_path_not_found)
print("\n")
read_csv(file_path_valid)
