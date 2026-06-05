import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Thomas', 'Sofia', 'Lucas', 'Emma'],
    'age': [20, 22, 21, 19, 23],
    'math_score': [15, 12, 18, 14, 11],
    'cs_score': [17, 14, 19, 13, 16]
}, index=['S001', 'S002', 'S003', 'S004', 'S005'])

def display_comparison(dataframe):
    """Display comparison table between .loc and .iloc"""
    
    print("\n" + "="*70)
    print("COMPARISON TABLE: .loc vs .iloc")
    print("="*70)
    
    examples = [
        ("Single row", ".loc['S003']", ".iloc[2]"),
        ("Multiple rows", ".loc[['S001', 'S003']]", ".iloc[[0, 2]]"),
        ("Slice", ".loc['S002':'S004'] (INCLUSIVE)", ".iloc[1:4] (EXCLUSIVE)"),
        ("All rows", ".loc[:, 'name']", ".iloc[:, 0]"),
        ("Rows + columns", ".loc['S002':'S004', 'name':'age']", ".iloc[1:4, 0:2]"),
    ]
    
    for description, loc_expr, iloc_expr in examples:
        print(f"\n> {description}:")
        print(f"  .loc  -> {loc_expr}")
        print(f"  .iloc -> {iloc_expr}")

# Example usage
display_comparison(df)