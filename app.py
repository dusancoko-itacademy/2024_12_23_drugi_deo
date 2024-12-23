import sys 
import arrow

timezone = None 
date_format = None 

if len(sys.argv) > 1:
    n = len(sys.argv)
    for i in range(len(sys.argv)):
        if sys.argv[i] == "-t" or sys.argv[i] == "--timezone":
            timezone = sys.argv[i+1] 
        elif sys.argv[i] == "-f" or sys.argv[i] == "--format":
            date_format = sys.argv[i+1]            

if timezone is None and date_format == None:
    print(arrow.now().format("DD.MM.YYYY. HH:mm"))
elif timezone is None and date_format is not None:
    try:
        print(arrow.now().format(date_format))
    except:
        print(f"Format '{date_format}' nije validni format.\nPogledajte dokumentaciju na https://arrow.readthedocs.io/")
elif timezone is not None and date_format is None:
    try:
        print(arrow.utcnow().to(timezone).format("DD.MM.YYYY. HH:mm"))  
    except:
        print(f"Vremenska zona nije dobra.\nPogledajte https://en.wikipedia.org/wiki/List_of_tz_database_time_zones")
else:
    try:
        print(arrow.utcnow().to(timezone).format(date_format))
    except Exception as ex:
        print(ex)
