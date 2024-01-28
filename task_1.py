from datetime import datetime

def get_days_from_today():
    try:
        user_input = input(f"Введіть дату у форматі 'РРРР-ММ-ДД': ")
        now = datetime.now()
        user_input = datetime.strptime(user_input, "%Y-%m-%d")
        result = user_input - now
        return result
    
    except ValueError:
        print(f"Введена строка не є датою")
        return None
    
res = get_days_from_today()
if res is not None:
    print(res.days)




# Розрахунок прикладу, котрий навидиться в 1 завданні

# from datetime import datetime

# def get_days_from_today(date):
#     future_date = datetime.strptime(date, "%Y-%m-%d")
#     now = "2021-05-05"
#     now = datetime.strptime(now, "%Y-%m-%d")
#     result = future_date - now
#     return result.days



# res = get_days_from_today("2021-10-09")
# print(res)

