age = input("What is your current age?\n")
age_as_int = int(age)
age_in_days = 32850 - age_as_int * 365
age_in_weeks = 4680 - age_as_int * 52 
age_in_months = 1080 - age_as_int * 12 
print(f"You have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left.")