import datetime

def day_of_week(day, month, year):
  """
  Определяет день недели, соответствующий заданной дате.
  """
  date = datetime.date(year, month, day)
  weekday = date.weekday()
  days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
  return days_of_week[weekday]

def is_leap_year(year):
  """
  Проверяет, является ли год високосным.
  """
  if year % 4 != 0:
    return False
  elif year % 100 == 0 and year % 400 != 0:
    return False
  else:
    return True

def calculate_age(day, month, year):
  """
  Рассчитывает возраст пользователя в годах.
  """
  today = datetime.date.today()
  birthdate = datetime.date(year, month, day)
  age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
  return age

def format_date(day, month, year):
  """
  Форматирует дату в виде дд мм гггг
  """
  return f"{day} {month} ****"

# Запрашиваем дату у пользователя
day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))

# Определяем день недели
weekday = day_of_week(day, month, year)

# Проверяем, високосный ли год
is_leap = is_leap_year(year)

# Вычисляем возраст
age = calculate_age(day, month, year)

# Форматируем дату
formatted_date = format_date(day, month, year)

# Выводим результат
print(f"Ваш день рождения был {weekday}.")
if is_leap:
  print(f"Год {year} был високосным.")
else:
  print(f"Год {year} не был високосным.")
print(f"Вам сейчас {age} лет.")
print(f"Ваша дата рождения: {formatted_date}")

-----------------------------------------------------------------------------

import datetime

def day_of_week(day, month, year):
  """
  Определяет день недели, соответствующий заданной дате.
  """
  date = datetime.date(year, month, day)
  weekday = date.weekday()
  days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
  return days_of_week[weekday]

def is_leap_year(year):
  """
  Проверяет, является ли год високосным.
  """
  if year % 4 != 0:
    return False
  elif year % 100 == 0 and year % 400 != 0:
    return False
  else:
    return True

def calculate_age(day, month, year):
  """
  Рассчитывает возраст пользователя в годах.
  """
  today = datetime.date.today()
  birthdate = datetime.date(year, month, day)
  age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
  return age

def format_date(day, month, year):
  """
  Форматирует дату в виде ** ** ** **
  """
  return f"** ** ** **"

# Запрашиваем дату у пользователя
day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))

# Определяем день недели
weekday = day_of_week(day, month, year)

# Проверяем, високосный ли год
is_leap = is_leap_year(year)

# Вычисляем возраст
age = calculate_age(day, month, year)

# Форматируем дату
formatted_date = format_date(day, month, year)

# Выводим результат
print(f"Ваш день рождения был {weekday}.")
if is_leap:
  print(f"Год {year} был високосным.")
else:
  print(f"Год {year} не был високосным.")
print(f"Вам сейчас {age} лет.")
print(f"Ваша дата рождения: {formatted_date}")
