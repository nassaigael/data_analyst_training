import csv
import os

def calculate_average(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"File '{input_file}' does not exist.")
        return None
    
    subjects = ["math score", "reading score", "writing score"]
    scores = {subject: [] for subject in subjects}
    print("scores: ", scores)

    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for subject in subjects:
                scores[subject].append(float(row[subject]))
    
    averages = {subject: sum(score) / len(score) for subject, score in scores.items()}
    print("averages: ", averages)

    with open(output_file, mode='w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["subject", "average"])
        writer.writeheader()
        for subject, average in averages.items():
            writer.writerow({"subject": subject, "average": average})
    print(f"Averages have been calculated and saved to '{output_file}'.")


input_file = "./data/students_rates.csv"
output_file = "./data/average_scores.csv"
calculate_average(input_file, output_file)
