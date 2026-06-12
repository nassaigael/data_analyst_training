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

def get_correlation_between_age_and_turnover(file_path):
    hr_data = pd.read_csv(file_path)
    hr_data["Left_Binary"] = hr_data["Left_Company"].map({"Yes": 1, "No": 0})
    correlation = hr_data["Age"].corr(hr_data["Left_Binary"])
    average_age_by_status = hr_data.groupby("Left_Company")["Age"].mean()
    return correlation, average_age_by_status

def get_average_salary_between_left_and_right_company(file_path):
    hr_data = pd.read_csv(file_path)
    average_salary_by_status = hr_data.groupby("Left_Company")["Monthly_Salary"].mean()
    average_salary_by_status["diff_between_two"] = average_salary_by_status["Yes"] - average_salary_by_status["No"]
    return average_salary_by_status

# Usage example
file_to_test = "E:/data_analyst/work/data/hr_employees.csv"
print(get_average_salary_between_left_and_right_company(file_to_test))
