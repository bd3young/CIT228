import datetime

weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

now = datetime.date.today()

dayOfWeek = now.weekday()

today = weekDays[dayOfWeek]

daysToWeekend = 6 - dayOfWeek
print(f"There are {daysToWeekend - 1} days until the weekend")

quotePrinted = "false"

for left in weekDays[dayOfWeek:daysToWeekend]:
    if today == "Sunday" and quotePrinted == "false":
        print(left, "Sunday, last say of the weekend.")
        quotePrinted = "true"
    elif (today == "Monday" or today == "Tuesday" or today == "Wednesday") and quotePrinted == "false":
        print(left, "Wake me up when the week is over.")
        quotePrinted = "true"
    elif today == "Thursday" and quotePrinted == "false":
        print(left, "Just a little bit more.")
        quotePrinted = "true"
    elif quotePrinted == "false":
        print(left, "Party time!")
        quotePrinted = "true"
    else:
        print(left)