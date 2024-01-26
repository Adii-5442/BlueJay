import pandas as pd


def analyze_schedule():
    # Read the spreadsheet into a DataFrame
    df = pd.read_csv("data.csv")
    print(df)

    # # Convert date columns to datetime format
    # df['Time'] = pd.to_datetime(df['Time'])
    # df['Time Out'] = pd.to_datetime(df['Time Out'])

#     # a) Employees who have worked for 7 consecutive days
#     consecutive_days = df.groupby('Employee Name')['Time'].diff().dt.days == 1
#     employees_7_consecutive_days = df[consecutive_days].groupby(
#         'Employee Name').filter(lambda x: len(x) >= 7)

#     # b) Employees with less than 10 hours between shifts but greater than 1 hour
#     time_between_shifts = df.groupby('Employee Name')[
#         'Time'].diff().dt.total_seconds() / 3600
#     employees_less_than_10_hours = df[(
#         time_between_shifts < 10) & (time_between_shifts > 1)]

#     # c) Employees who have worked for more than 14 hours in a single shift
#     employees_more_than_14_hours = df[(
#         df['Time Out'] - df['Time']).dt.total_seconds() / 3600 > 14]

#     # Print results to console
#     print("Employees who have worked for 7 consecutive days:")
#     print(employees_7_consecutive_days[['Employee Name']])
#     print("\nEmployees with less than 10 hours between shifts but greater than 1 hour:")
#     print(employees_less_than_10_hours[['Employee Name']])
#     print("\nEmployees who have worked for more than 14 hours in a single shift:")
#     print(employees_more_than_14_hours[['Employee Name']])

#     # Save console output to a text file
#     output_file_path = 'output.txt'
#     with open(output_file_path, 'w') as output_file:
#         output_file.write(
#             "Employees who have worked for 7 consecutive days:\n")
#         output_file.write(
#             str(employees_7_consecutive_days[['Employee Name']]) + '\n\n')
#         output_file.write(
#             "Employees with less than 10 hours between shifts but greater than 1 hour:\n")
#         output_file.write(
#             str(employees_less_than_10_hours[['Employee Name']]) + '\n\n')
#         output_file.write(
#             "Employees who have worked for more than 14 hours in a single shift:\n")
#         output_file.write(str(employees_more_than_14_hours[['Employee Name']]))

#     print(f"\nResults saved to {output_file_path}")


# if __name__ == "__main__":
#     file_path = "path/to/your/downloaded/file.csv"  # Update with the actual file path
#     analyze_schedule()
