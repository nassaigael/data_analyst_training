import pandas as pd


def get_department_with_highest_rate_turnover(file_path):
    hr_data = pd.read_csv(file_path)
    turnover_by_department = hr_data.groupby("Department").agg(
        employee_left=("Left_Company", lambda x: (x == "Yes").sum()),
        total_employees=("Employee_ID", "count"),
    )
    turnover_by_department["turnover_rate"] = (turnover_by_department["employee_left"] / turnover_by_department[
        "total_employees"]) * 100
    turnover_by_department["employees_stayed"] = turnover_by_department["total_employees"] - turnover_by_department[
        "employee_left"]
    return turnover_by_department["turnover_rate"].sort_values(ascending=False).head(2)


# Usage example
file_to_test = "E:/data_analyst/work/data/hr_employees.csv"
print(get_department_with_highest_rate_turnover(file_to_test))
