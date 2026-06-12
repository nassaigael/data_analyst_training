import pandas as pd

data = {
    'name': ['Alice', 'Thomas', 'Sofia', 'Lucas', 'Emma'],
    'age': [20, 22, 21, 19, 23],
    'math_score': [15, 12, 18, 14, 11],
    'cs_score': [17, 14, 19, 13, 16],
    'physics_score': [14, 15, 16, 12, 13],
    'biology_score': [16, 13, 15, 14, 12]
}


def add_average_columns(data_to_add):
    data_frame = owner_data_to_data_frame(data_to_add)
    score_columns = extract_scores_columns(data_to_add)

    data_frame['average'] = data_frame[score_columns].mean(axis=1)
    data_frame['average_rounded'] = data_frame['average'].round(2)

    data_frame['num_subjects'] = len(score_columns)

    return data_frame, score_columns


def owner_data_to_data_frame(data_to_analys):
    result = pd.DataFrame(data_to_analys)
    return result


def extract_scores_columns(data_to_extract):
    data_to_extract = owner_data_to_data_frame(data_to_extract)
    scores_columns = []

    for col in data_to_extract.columns:
        if col.endswith('_score'):
            scores_columns.append(col)

    if not scores_columns:
        raise ValueError("No score columns found. Columns should contain 'score' in name.")

    return scores_columns


# Example usage
df, subjects = add_average_columns(data)

print("=" * 60)
print("DATAFRAME WITH DYNAMIC AVERAGE")
print("=" * 60)
print(f"\nDetected subjects ({len(subjects)}): {subjects}")
print(f"\nDataFrame:")
print(df)
print(f"\nClass averages:")
print(f"  Overall class average: {df['average'].mean():.2f}/20")
print(f"  Highest average: {df['average'].max():.2f} ({df.loc[df['average'].idxmax(), 'name']})")
print(f"  Lowest average: {df['average'].min():.2f} ({df.loc[df['average'].idxmin(), 'name']})")
