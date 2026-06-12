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


def get_experienced_vs_fidelity_employee(file_path):
    return pd.read_csv(file_path).groupby("Left_Company")["Years_Experience"].mean()


def get_turnover_rate_by_education_level(file_path):
    hr_data = pd.read_csv(file_path)
    turnover_by_education_level = hr_data.groupby("Education_Level").agg(
        employee_left=("Left_Company", lambda x: (x == "Yes").sum()),
        total_employees=("Employee_ID", "count")
    )
    turnover_by_education_level["turnover_rate"] = (
            turnover_by_education_level["employee_left"] / turnover_by_education_level["total_employees"] * 100
    )
    return turnover_by_education_level["turnover_rate"]


def get_turnover_rate_by_gender(file_path):
    hr_data = pd.read_csv(file_path)
    turnover_by_gender = hr_data.groupby("Gender").agg(
        employee_left=("Left_Company", lambda x: (x == "Yes").sum()),
        total_employees=("Employee_ID", "count")
    )
    turnover_by_gender["turnover_rate"] = (turnover_by_gender["employee_left"] / turnover_by_gender[
        "total_employees"]) * 100
    return turnover_by_gender

def get_turnover_rate_by_score(file_path):
    hr_data = pd.read_csv(file_path)
    turnover_by_score = hr_data.groupby("Performance_Score").agg(
        employee_left=("Left_Company", lambda x: (x == "Yes").sum()),
        total_employees=("Employee_ID", "count")
    )
    turnover_by_score["turnover_rate"] = (turnover_by_score["employee_left"] / turnover_by_score[
        "total_employees"]) * 100
    return turnover_by_score["turnover_rate"]

def get_count_of_female_employee(file_path):
    hr_data = pd.read_csv(file_path)
    return (hr_data["Gender"] == "Female").sum()




# Usage example
file_to_test = "E:/data_analyst/work/data/hr_employees.csv"
print(get_turnover_rate_by_score(file_to_test))
