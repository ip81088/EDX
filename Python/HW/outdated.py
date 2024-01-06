# # Create a dict of all months
# months = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]
# # Loop forever
# while True:
#     # Get user input
#     i = input("Date: ")
#     try:
#         # Split the date by /
#         m, d, y = i.split("/")
#         # Check if the month is in between of 1 and 12 and day between 1 and 31
#         if (1 <= int(m) <= 12 and 1 <= int(d) <= 31):
#             break  
#     except:
#         try:
#             # Split the date by space
#             month, day, y = i.split(" ")
#             # Find the number of the month
#             for j in range(len(months)):
#                 if month == months[j]:
#                     month = j + 1
#             # Remove the comma from day variable
#             day = day.replace(",","")
#             # Check if month is in between 1 and 12 and day is between 1 and 31
#             if (1 <= int(m) <= 12 and 1 <= int(d) <= 31):
#                 break 
#         except:
#             print()
#             pass

# # If month is less than 10, add a 0 before
        
# # If a day is less than 10, add a 0 before
        
# # Print the result
# print(f"{y}-{int(m):02}-{int(d):02}")

def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    reverse(months)

def reverse(months):
    while True:
        try:
            date = input("Date: ").strip()
            if ',' in date:
                date = date.capitalize()
                month, day, year = date.split()
                day = day.split(',')
                day = int(day[0])
                if month in months and day >= 1 and day <= 31:
                    return print(f"{year}-{months.index(month)+1:02}-{day:02}")

            elif '/' in date:
                month, day, year = date.split('/')
                year = int(year)
                day = int(day)
                month = int(month) - 1
                if month in range(len(months)) and day >= 1 and day <= 31:
                    return print(f"{year}-{month+1:02}-{day:02}")
        except ValueError:
            pass

main()