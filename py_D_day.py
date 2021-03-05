import datetime

def getDaysBefore(d="2021-9-5"): #찾으려는 일 수 
    dList = d.split("-")
    year = int(dList[0])
    month = int(dList[1])
    day = int(dList[2])
    
    dday = datetime.datetime(year, month, day)
    now = datetime.datetime.now()
    
    return str(dday - now).split(",")[0]
    
print(getDaysBefore("2021-9-5")) #찾으려는 일수 출력 