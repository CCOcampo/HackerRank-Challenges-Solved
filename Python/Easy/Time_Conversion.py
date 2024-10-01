def timeConversion(s):
    hours, minutes, seconds = s[:-2].split(":")
    period = s[-2:]
    
    if period == "PM" and hours != "12":
        hours = str(int(hours) + 12)
    elif period == "AM" and hours == "12":
        hours = "00"
    
    return f"{hours}:{minutes}:{seconds}"

# Ejemplo
s = "01:05:45PM"
print(timeConversion(s))