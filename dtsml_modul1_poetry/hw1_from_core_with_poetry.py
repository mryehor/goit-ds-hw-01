from datetime import datetime, timedelta, timezone

def days_difference(date: str ) -> int :

    datetime_object = datetime.strptime(date, "%Y-%m-%d").date()
    date_now = datetime.now().date()

    date_diffrence = date_now - datetime_object 

    return date_diffrence.days

print(f"Різниця становить: {days_difference('2020-10-09')} днів")
