from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    
    today = date.today()
    
    if not users:
        return {}  # Повертаємо пустий словник для порожнього списку користувачів
    
    def find_start_of_next_week():
        days_until_monday = (7 - today.weekday()) % 7
        start_of_next_week = today + timedelta(days=days_until_monday)
        return start_of_next_week 
     
    start_of_next_week = find_start_of_next_week()
      
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    birthdays_per_week = {day: [] for day in days_of_week} #робить список
    
    for user in users:
        birthday = user['birthday'].replace(year=today.year) # 2024-01-26
        
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)   # Якщо день народження вже минув у цьому році, пропускаємо.
            
        if birthday >= today + timedelta(days=7):# Якщо день народження не на наступній неділі , пропускаємо користувача.   
            continue
        
        if birthday.weekday() >= 5:
            while birthday.weekday() != start_of_next_week.weekday():
                birthday += timedelta(days=1) # Зміщуємо день народження на наступний тиждень
                
        day_name = days_of_week[(birthday.weekday() - start_of_next_week.weekday()) % 7]
        birthdays_per_week[day_name].append(user['name'])
        
    if not any(birthdays_per_week.values()):
        print({})
        return {}
    
    
    # Видаляємо дні тижня, для яких немає днів народжень
    birthdays_per_week = {day: names for day, names in birthdays_per_week.items() if names}
    return birthdays_per_week

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum1", "birthday": datetime(2015, 1,25).date()},
        {"name": "Jan Koum2", "birthday": datetime(2015, 1,26).date()},
        {"name": "Jan Koum3", "birthday": datetime(2015, 1,27).date()},
        {"name": "Jan Koum4", "birthday": datetime(2015, 1,28).date()},
        {"name": "Jan Koum5", "birthday": datetime(2015, 1,29).date()},
        {"name": "Jan Koum6", "birthday": datetime(2015, 1,30).date()},
    ]
    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")