import pandas as pd
import matplotlib.pyplot as plt


def get_department_with_highest_rate_turnover(file_path):
    hr_data = pd.read_csv(file_path)

    turnover_by_department = hr_data.groupby("Department").agg(
        employee_left=("Left_Company", lambda x: (x == "Yes").sum()),
        total_employees=("Employee_ID", "count"),
    )

    turnover_by_department["turnover_rate"] = (
            turnover_by_department["employee_left"]
            / turnover_by_department["total_employees"]
            * 100
    )

    turnover_by_department["employees_stayed"] = (
            turnover_by_department["total_employees"]
            - turnover_by_department["employee_left"]
    )

    turnover_by_department["turnover_rate"].sort_values(ascending=False).plot(
        kind="bar",
        color="tomato",
        title="Taux de turnover par département"
    )

    plt.xlabel("Département")
    plt.ylabel("Taux de turnover (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return turnover_by_department["turnover_rate"].sort_values(ascending=False)


def get_correlation_between_age_and_turnover(file_path):
    hr_data = pd.read_csv(file_path)

    hr_data["Left_Binary"] = hr_data["Left_Company"].map({
        "Yes": 1,
        "No": 0
    })

    correlation = hr_data["Age"].corr(hr_data["Left_Binary"])
    average_age_by_status = hr_data.groupby("Left_Company")["Age"].mean()

    average_age_by_status.plot(
        kind="bar",
        color=["green", "red"],
        title=f"Âge moyen selon le départ - Corrélation : {correlation:.2f}"
    )

    plt.xlabel("Statut")
    plt.ylabel("Âge moyen")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    return correlation, average_age_by_status


def get_average_salary_between_left_and_right_company(file_path):
    hr_data = pd.read_csv(file_path)

    average_salary_by_status = hr_data.groupby("Left_Company")["Monthly_Salary"].mean()

    average_salary_by_status.plot(
        kind="bar",
        color=["green", "red"],
        title="Salaire moyen : employés restés vs partis"
    )

    plt.xlabel("Statut")
    plt.ylabel("Salaire moyen mensuel (€)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    return average_salary_by_status


def get_experienced_vs_fidelity_employee(file_path):
    hr_data = pd.read_csv(file_path)

    experience_by_status = hr_data.groupby("Left_Company")["Years_Experience"].mean()

    experience_by_status.plot(
        kind="bar",
        color=["green", "red"],
        title="Expérience moyenne : employés restés vs partis"
    )

    plt.xlabel("Statut")
    plt.ylabel("Années d'expérience")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    return experience_by_status


def get_turnover_rate_by_education_level(file_path):
    hr_data = pd.read_csv(file_path)

    turnover_by_education_level = hr_data.groupby("Education_Level").agg(
        employee_left=("Left_Company", lambda x: (x == "Yes").sum()),
        total_employees=("Employee_ID", "count")
    )

    turnover_by_education_level["turnover_rate"] = (
            turnover_by_education_level["employee_left"]
            / turnover_by_education_level["total_employees"]
            * 100
    )

    turnover_by_education_level["turnover_rate"].sort_values(ascending=False).plot(
        kind="bar",
        color="orange",
        title="Taux de turnover par niveau d'éducation"
    )

    plt.xlabel("Niveau d'éducation")
    plt.ylabel("Taux de turnover (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return turnover_by_education_level["turnover_rate"].sort_values(ascending=False)


def get_turnover_rate_by_gender(file_path):
    hr_data = pd.read_csv(file_path)

    turnover_by_gender = hr_data.groupby("Gender").agg(
        employee_left=("Left_Company", lambda x: (x == "Yes").sum()),
        total_employees=("Employee_ID", "count")
    )

    turnover_by_gender["turnover_rate"] = (
            turnover_by_gender["employee_left"]
            / turnover_by_gender["total_employees"]
            * 100
    )

    turnover_by_gender["turnover_rate"].plot(
        kind="bar",
        color=["pink", "skyblue"],
        title="Taux de turnover par genre"
    )

    plt.xlabel("Genre")
    plt.ylabel("Taux de turnover (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    return turnover_by_gender


def get_turnover_rate_by_score(file_path):
    hr_data = pd.read_csv(file_path)

    turnover_by_score = hr_data.groupby("Performance_Score").agg(
        employee_left=("Left_Company", lambda x: (x == "Yes").sum()),
        total_employees=("Employee_ID", "count")
    )

    turnover_by_score["turnover_rate"] = (
            turnover_by_score["employee_left"]
            / turnover_by_score["total_employees"]
            * 100
    )

    turnover_by_score["turnover_rate"].plot(
        kind="bar",
        color="purple",
        title="Taux de turnover par score de performance"
    )

    plt.xlabel("Performance Score")
    plt.ylabel("Taux de turnover (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    return turnover_by_score["turnover_rate"]


def get_average_seniority_of_employees_left(file_path):
    hr_data = pd.read_csv(file_path)

    hr_data["Hiring_Date"] = pd.to_datetime(hr_data["Hiring_Date"])

    baseline_date = pd.to_datetime("2024-12-31")

    employees_left = hr_data[hr_data["Left_Company"] == "Yes"].copy()

    employees_left["seniority_days"] = (
            baseline_date - employees_left["Hiring_Date"]
    ).dt.days

    employees_left["seniority_months"] = employees_left["seniority_days"] / 30.44

    average_seniority_months = employees_left["seniority_months"].mean().round(2)

    employees_left.plot(
        x="Employee_ID",
        y="seniority_months",
        kind="bar",
        color="brown",
        title="Ancienneté des employés partis"
    )

    plt.xlabel("Employé")
    plt.ylabel("Ancienneté en mois")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return average_seniority_months


def get_most_stable_age_group(file_path):
    hr_data = pd.read_csv(file_path)

    hr_data["Age_Group"] = pd.cut(
        hr_data["Age"],
        bins=[20, 30, 40, 50],
        labels=["20-30", "30-40", "40-50"],
        right=False
    )

    turnover_by_age_group = hr_data.groupby("Age_Group", observed=False).agg(
        employee_left=("Left_Company", lambda x: (x == "Yes").sum()),
        total_employees=("Employee_ID", "count")
    )

    turnover_by_age_group["turnover_rate"] = (
            turnover_by_age_group["employee_left"]
            / turnover_by_age_group["total_employees"]
            * 100
    )

    most_stable_age_group = turnover_by_age_group["turnover_rate"].idxmin()
    most_unstable_age_group = turnover_by_age_group["turnover_rate"].idxmax()

    turnover_by_age_group["turnover_rate"].plot(
        kind="bar",
        color="teal",
        title="Taux de turnover par tranche d'âge"
    )

    plt.xlabel("Tranche d'âge")
    plt.ylabel("Taux de turnover (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    return most_stable_age_group, most_unstable_age_group, turnover_by_age_group


def get_profile_of_employee_who_left(file_path):
    hr_data = pd.read_csv(file_path)

    employees_left = hr_data[hr_data["Left_Company"] == "Yes"].copy()

    profile = {
        "average_age": employees_left["Age"].mean().round(1),
        "average_experience": employees_left["Years_Experience"].mean().round(1),
        "average_salary": employees_left["Monthly_Salary"].mean().round(1),
        "average_performance_score": employees_left["Performance_Score"].mean().round(1),
        "most_common_department": employees_left["Department"].mode()[0],
        "most_common_education": employees_left["Education_Level"].mode()[0],
        "most_common_gender": employees_left["Gender"].mode()[0],
    }

    numeric_profile = pd.Series({
        "Âge moyen": profile["average_age"],
        "Expérience moyenne": profile["average_experience"],
        "Score moyen": profile["average_performance_score"]
    })

    numeric_profile.plot(
        kind="bar",
        color="darkred",
        title="Profil moyen de l'employé qui part"
    )

    plt.ylabel("Valeur moyenne")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    employees_left["Department"].value_counts().plot(
        kind="bar",
        color="steelblue",
        title="Départements des employés partis"
    )

    plt.xlabel("Département")
    plt.ylabel("Nombre de départs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    employees_left["Education_Level"].value_counts().plot(
        kind="bar",
        color="orange",
        title="Niveau d'éducation des employés partis"
    )

    plt.xlabel("Niveau d'éducation")
    plt.ylabel("Nombre de départs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return profile


def get_count_of_female_employee(file_path):
    hr_data = pd.read_csv(file_path)

    gender_count = hr_data["Gender"].value_counts()

    gender_count.plot(
        kind="pie",
        autopct="%1.1f%%",
        title="Répartition hommes / femmes"
    )

    plt.ylabel("")
    plt.tight_layout()
    plt.show()

    return (hr_data["Gender"] == "Female").sum()


def run_all_analyses(file_path):
    print("=" * 70)
    print("1. Département avec le plus haut turnover")
    print("=" * 70)
    print(get_department_with_highest_rate_turnover(file_path))

    print("\n" + "=" * 70)
    print("2. Corrélation entre l'âge et le départ")
    print("=" * 70)
    correlation, average_age = get_correlation_between_age_and_turnover(file_path)
    print(f"Corrélation : {correlation:.2f}")
    print(average_age)

    print("\n" + "=" * 70)
    print("3. Salaire moyen des employés partis vs restés")
    print("=" * 70)
    print(get_average_salary_between_left_and_right_company(file_path))

    print("\n" + "=" * 70)
    print("4. Expérience moyenne des employés partis vs restés")
    print("=" * 70)
    print(get_experienced_vs_fidelity_employee(file_path))

    print("\n" + "=" * 70)
    print("5. Turnover par niveau d'éducation")
    print("=" * 70)
    print(get_turnover_rate_by_education_level(file_path))

    print("\n" + "=" * 70)
    print("6. Turnover par genre")
    print("=" * 70)
    print(get_turnover_rate_by_gender(file_path))

    print("\n" + "=" * 70)
    print("7. Turnover par score de performance")
    print("=" * 70)
    print(get_turnover_rate_by_score(file_path))

    print("\n" + "=" * 70)
    print("8. Ancienneté moyenne des employés partis")
    print("=" * 70)
    seniority = get_average_seniority_of_employees_left(file_path)
    print(f"Ancienneté moyenne : {seniority} mois")

    print("\n" + "=" * 70)
    print("9. Tranche d'âge la plus stable")
    print("=" * 70)
    stable_group, unstable_group, age_group_details = get_most_stable_age_group(file_path)
    print(age_group_details)
    print(f"Tranche la plus stable : {stable_group}")
    print(f"Tranche la plus instable : {unstable_group}")

    print("\n" + "=" * 70)
    print("10. Profil-type de l'employé qui part")
    print("=" * 70)
    profile = get_profile_of_employee_who_left(file_path)
    for key, value in profile.items():
        print(f"{key} : {value}")

    print("\n" + "=" * 70)
    print("Bonus. Nombre de femmes dans l'entreprise")
    print("=" * 70)
    print(f"Nombre de femmes : {get_count_of_female_employee(file_path)}")


# Usage example
file_to_test = "E:/data_analyst/work/data/hr_employees.csv"

run_all_analyses(file_to_test)
