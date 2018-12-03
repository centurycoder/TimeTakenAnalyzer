#!/usr/bin/python
import sys
from datetime import datetime, date, time, timedelta

if __name__ == '__main__':
    filename = sys.argv[1]
    starttime = ""
    endtime = ""
    if (len(sys.argv) == 4):
        starttime = sys.argv[2]
        endtime = sys.argv[3]
    tally = 0
    cost_scatter = {}
    time_scatter = {}

    file=open(filename,'rt')
    for line in file:
        if (line.startswith("#")):
            continue
        fields = line.strip('\r\n').split(" ")
        (dayutc,timeutc,host,timetaken) = (fields[0],fields[1],fields[3],fields[-1])
        bjtime=datetime.strptime(dayutc+" "+timeutc,"%Y-%m-%d %X") + timedelta(hours=8)
        timestr = bjtime.time().strftime("%X")
        if ((starttime !="") and (timestr < starttime or timestr > endtime)):
            continue
        else:
            tally += 1
            seconds = int(timetaken) / 1000
            if seconds in cost_scatter:
                cost_scatter[seconds] += 1
            else:
                cost_scatter[seconds] = 1
            # stat each minute stat count
            minstr = bjtime.time().strftime("%H_%M")
            if minstr in time_scatter:
                time_scatter[minstr] +=1
            else:
                time_scatter[minstr] = 1
    print tally
    print cost_scatter
    print time_scatter
    file.close()
