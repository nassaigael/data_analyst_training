import csv
import os


def calculate_average(input_file_path, output_file_path):
    if not os.path.exists(input_file_path):
        print(f"File '{input_file_path}' does not exist.")
        return None

    subjects = ["math score", "reading score", "writing score"]
    scores = {subject: [] for subject in subjects}

    with open(input_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for subject in subjects:
                scores[subject].append(float(row[subject]))

    averages = {subject: sum(score) / len(score) for subject, score in scores.items()}

    with open(output_file_path, mode='w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["subject", "average"])
        writer.writeheader()
        for subject, average in averages.items():
            writer.writerow({"subject": subject, "average": average})
    print(f"Averages have been calculated and saved to '{output_file_path}'.")
    return None


input_file = "./data/csv/students_rates.csv"
output_file = "./data/csv/average_scores.csv"
calculate_average(input_file, output_file)
