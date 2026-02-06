from datetime import datetime, timedelta, date


# str in date
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


# date in str
def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    for user in user_data:
        if isinstance(user['birthday'], str):
            user['birthday'] = string_to_date(user['birthday'])
    return user_data


# наступний день народження протягом тижня
def find_next_weekday(start_date, weekday):
    return start_date + timedelta((weekday - start_date.weekday()) % 7 or 7)


def adjust_for_weekend(birthday):
    if isinstance(birthday, str):
        birthday = string_to_date(birthday)  # якщо дата строка виправляємо її в дату
    weekday = birthday.weekday()
    if weekday >= 5:
        birthday = find_next_weekday(birthday, 0)  # переносимо дату на понеділо якщо припадає вихідний
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []  # список для днів народження
    users = prepare_user_list(users)
    today = date.today()
    # today = date(2025, 12, 30)
    for user in users:
        birthday_this_year = user['birthday'].replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)  # якщо день народження вже пройшов переносимо на наступний рік

        birthday_days = (birthday_this_year - today).days

        if 0 <= birthday_days <= days:
            birthday_this_year = adjust_for_weekend(birthday_this_year)  # переносиму дату на наступний робочий день

            upcoming_birthdays.append({
                'name': user['name'],
                "congratulation_date": date_to_string(birthday_this_year)
            })

    return upcoming_birthdays


users = [
    {"name": "Bill Gates 1955.1.5", "birthday": "1955.1.5"},
    {"name": "Bill Gates 1955.1.2", "birthday": "1955.1.2"},
    {"name": "Bill Gates", "birthday": "1955.3.25"},  # 53 days
    {"name": "Steve Jobs", "birthday": "1955.3.21"},  # 49 days
    {"name": "Jinny Lee", "birthday": "1956.3.22"},  # 50 days
    {"name": "Sarah Lee", "birthday": "1957.3.23"},  # 51 days
    {"name": "Jonny Lee", "birthday": "1958.3.22"},  # 50 days
    {"name": "John Doe", "birthday": "1985.01.23"},  # -8 days
    {"name": "Jane Smith", "birthday": "1990.01.27"}  # -4 days
]

asd = get_upcoming_birthdays(users, days=7)
asd2 = get_upcoming_birthdays(users, days=7)

for i in asd:
    print(i)

for i in asd2:
    print(i)