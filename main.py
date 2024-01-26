import pandas as pd

def analyze():

    df = pd.read_csv("data.csv")

    df['Time'] = pd.to_datetime(df['Time'], format='%m/%d/%Y %I:%M %p')
    df['Time Out'] = pd.to_datetime(df['Time Out'], format='%m/%d/%Y %I:%M %p')

    brk = "x----x"*20
    print(brk)

    #  Employees worked for 7 consecutive days
    consecutive_days = df.groupby('Employee Name')['Time'].diff().dt.days == 1
    employees_7_consecutive_days = df[consecutive_days].groupby(
        'Employee Name').filter(lambda x: len(x) >= 7)

    print("Employees who have worked for 7 consecutive days: =>")
    print(employees_7_consecutive_days[['Employee Name']])
    print("Total Results =>",len(employees_7_consecutive_days[['Employee Name']]))
    print(brk)


    # Employees with less than 10 hours between shifts but greater than 1 hour

    time_shifts = df.groupby('Employee Name')[
        'Time'].diff().dt.total_seconds() / 3600
    employees_less_than_10_hours = df[(
        time_shifts < 10) & (time_shifts > 1)]

    print("Employees with less than 10 hours between shifts but greater than 1 hour:")
    print(employees_less_than_10_hours[['Employee Name']])
    print("Total Results =>",len(employees_less_than_10_hours[['Employee Name']]))
    print(brk)

    # Employees who have worked for more than 14 hours in a single shift

    employees_more_than_14_hours = df[(
        df['Time Out'] - df['Time']).dt.total_seconds() / 3600 > 14]

    print("Employees who  worked for more than 14 hours in a single shift : =>")
    print(employees_more_than_14_hours[['Employee Name']])
    print("Total Results : =>",len(employees_more_than_14_hours[['Employee Name']]))
    print(brk)



    output = 'output.txt'
    with open(output, 'w') as opf:
        opf.write(
            "Employees who have worked for 7 consecutive days:\n")
        opf.write(
            str(employees_7_consecutive_days[['Employee Name']]) + '\n\n')
        opf.write(
            "Employees with less than 10 hours between shifts but greater than 1 hour:\n")
        opf.write(
            str(employees_less_than_10_hours[['Employee Name']]) + '\n\n')
        opf.write(
            "Employees who have worked for more than 14 hours in a single shift:\n")
        opf.write(str(employees_more_than_14_hours[['Employee Name']]))

    print("Results saved to ",output)


analyze()

#Submitted by Aditya Singh