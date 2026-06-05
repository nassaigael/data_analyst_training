import pandas as pd

data = {
    'name': ['Alice', 'Thomas', 'Sofia', 'Lucas', 'Emma'],
    'age': [20, 22, 21, 19, 23],
    'math_score': [15, 12, 18, 14, 11],
    'cs_score': [17, 14, 19, 13, 16],
    'physics_score': [14, 15, 16, 12, 13],  # Added new subject
    'biology_score': [16, 13, 15, 14, 12]   # Added new subject
}

def add_average_columns(data):
    """
    Add average column dynamically based on available score columns.
    Works with any number of subjects.
    """
    df = pd.DataFrame(data)
    
    # Detect all columns that end with '_score' or contain 'score'
    score_columns = []
    for col in df.columns:
        if col.endswith('_score') or 'score' in col:
            score_columns.append(col)
    
    # Alternative: Select all numeric columns except 'age' and 'id'
    # numeric_columns = df.select_dtypes(include=['number']).columns
    # score_columns = [col for col in numeric_columns if col not in ['age', 'id']]
    
    if not score_columns:
        raise ValueError("No score columns found. Columns should contain 'score' in name.")
    
    # Calculate average across all detected score columns
    df['average'] = df[score_columns].mean(axis=1)
    df['average_rounded'] = df['average'].round(2)
    
    # Add subject count information
    df['num_subjects'] = len(score_columns)
    
    return df, score_columns

# Example usage
df, subjects = add_average_columns(data)

print("="*60)
print("DATAFRAME WITH DYNAMIC AVERAGE")
print("="*60)
print(f"\nDetected subjects ({len(subjects)}): {subjects}")
print(f"\nDataFrame:")
print(df)
print(f"\nClass averages:")
print(f"  Overall class average: {df['average'].mean():.2f}/20")
print(f"  Highest average: {df['average'].max():.2f} ({df.loc[df['average'].idxmax(), 'name']})")
print(f"  Lowest average: {df['average'].min():.2f} ({df.loc[df['average'].idxmin(), 'name']})")