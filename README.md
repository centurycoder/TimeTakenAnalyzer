
Usage: 
    python stat_iis_timetaken.py /path/to/iislog.log [start_time] [end_time]
        /path/to/iislog.log, path to IIS log file you want to analyze
        start_time: optional, start time for the time range you want to analyze, HH24:MI:SS
        end_time: optional, end time for the time range you want to analyze, HH24:MI:SS
        
    This python program will read an IIS log file, extract "time-taken" field, and tells you 2 results:
    1) Time cost scatters: how many requests are finished within 1s, how many between 1-2s, etc.
    2) Time scatters: how many requests are there in each seconds.

    This program is useful for stating how time-cost is related with request count for an IIS server. 

Highlights:
    1. IIS timestamp is UTC time, this program use datetime and timedelta to translate it into BJ +8 timezone
    2. python dictionary is used, to do stat and summarize work efficiently.
