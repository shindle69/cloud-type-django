from django.shortcuts import render
from .models import Today
from datetime import datetime
from django.utils.dateformat import DateFormat

from korean_lunar_calendar import KoreanLunarCalendar

# Create your views here.
def today_fortune(request):
    today = DateFormat(datetime.now()).format('Ymd')
    today_year = DateFormat(datetime.now()).format('Y')
    today_month = DateFormat(datetime.now()).format('m')
    today_day = DateFormat(datetime.now()).format('d')
    key = int(int(today) % 365)
    dataset = Today.objects.get(id=key)

    calendar = KoreanLunarCalendar()
    calendar.setSolarDate(int(today_year), int(today_month), int(today_day))
    lunar = calendar.LunarIsoFormat()
    gabja = calendar.getGapJaString()
    hanja = calendar.getChineseGapJaString()

    week = datetime.today().weekday()
    if week ==0:
        weekday = "월요일"
    elif week ==1:
        weekday = "화요일"
    elif week ==2:
        weekday = "수요일"
    elif week ==3:
        weekday = "목요일"
    elif week ==4:
        weekday = "금요일"
    elif week ==5:
        weekday = "토요일"
    elif week ==6:
        weekday = "일요일"
    else:
        weekday = "error"

    context = {
        "today": today,
        "key": key,
        "weekday": weekday,
        "today_year": today_year,
        "today_month": today_month,
        "today_day": today_day,
        "dataset": dataset,
        "lunar": lunar,
        "gabja": gabja,
        "hanja": hanja,
    }
    return render(request, "today/today_fortune.html", context)