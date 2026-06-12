import csv


def read_and_process_file(csv_file):
    """
    Reads a CSV file with complete error handling
    """
    file = None
    try:
        print(f"Attempting to open '{csv_file}'...")
        file = open(csv_file, 'r', encoding='utf-8')
        reader = csv.DictReader(file)

        if 'math score' not in reader.fieldnames:
            raise KeyError("Column 'math score' missing")

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' does not exist")
        return None

    except PermissionError:
        print(f"Error: Permission denied to read '{csv_file}'")
        return None

    except KeyError as e:
        print(f"Error: {e}")
        return None

    else:
        print("File opened successfully")

        math_scores = []
        reading_scores = []
        writing_scores = []

        for line_num, row in enumerate(reader, 2):
            try:
                math_scores.append(float(row['math score']))
                reading_scores.append(float(row['reading score']))
                writing_scores.append(float(row['writing score']))
            except (ValueError, KeyError) as e:
                print(f"Warning Line {line_num}: Conversion error - {e}")

        if math_scores:
            math_avg = sum(math_scores) / len(math_scores)
            reading_avg = sum(reading_scores) / len(reading_scores)
            writing_avg = sum(writing_scores) / len(writing_scores)

            print(f"\nRESULTS:")
            print(f"   Math: {math_avg:.2f}")
            print(f"   Reading: {reading_avg:.2f}")
            print(f"   Writing: {writing_avg:.2f}")

            return {
                'math': math_avg,
                'reading': reading_avg,
                'writing': writing_avg
            }
        else:
            print("No valid data found")
            return None

    finally:
        if file and not file.closed:
            file.close()
            print("File closed properly")
        elif file:
            print("File already closed")
        else:
            print("No file to close")


result = read_and_process_file("E:/data_analyst/week_one/day_03/exercice_1/data/csv/students_rates.csv")

print("\n" + "=" * 50)
result2 = read_and_process_file("missing_file.csv")
