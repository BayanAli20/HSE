from calendar import month
import pandas as pd
import numpy as np

xrays_df = pd.read_excel("XRays.xlsx").sort_values(by="dtArrive")


print(xrays_df)

offset = pd.Timedelta("30min")


start_time= xrays_df.iloc[0].dtArrive.replace(minute=0,second=0)

stop_time = start_time + offset
sample = xrays_df.loc[(xrays_df.dtArrive >=start_time)& (xrays_df.dtArrive <= stop_time)]
sample_dt = pd.DataFrame(sample)
step = len(sample_dt)
xrays_rooms_temp = 1
xrays_rooms=[]
xrays_room_day= []

wait_samples= []
wait_days =[]
k=0
index_step=0
utilization=[0]*5
for index in range(0,len(xrays_df),step):
    if(step==0):
        index_step = index_step
    else:
        index_step = index_step + step


    xrays_rooms_temp=1
    wait_temp = [1] * step

    temp=0
    for i in range(len(sample_dt)):
        temp=0
        for j in range(0,i):
             if(sample_dt.iloc[i].dtBegin < sample_dt.iloc[j].dtCompleted):
                 temp = temp + 1
             if(sample_dt.iloc[i].dtArrive < sample_dt.iloc[j].dtBegin):
                 wait_temp[i] = wait_temp[i] + 1



        if(temp==xrays_rooms_temp):
            xrays_rooms_temp=xrays_rooms_temp+1
    xrays_rooms.append(xrays_rooms_temp)
    if(step==0):
        wait_temp=[0]
    w=max(wait_temp, key=lambda x: int(x))
    wait_samples.append(w)



    start_time = start_time + offset
    stop_time = start_time + offset
    if(start_time.hour == 20 and index_step< 21874):
        start_time = xrays_df.iloc[index_step].dtArrive.replace(hour=7,minute=0,second=0)

        stop_time = start_time + offset
        xrays_room_day.append(max(xrays_rooms, key=lambda x: int(x)))
        wait_days.append(max(wait_samples, key=lambda x: int(x)))

        xrays_rooms=[]
        wait_samples = []


    sample = xrays_df.loc[(xrays_df.dtArrive >= start_time) & (xrays_df.dtArrive <= stop_time)]
    sample_dt = pd.DataFrame(sample)
    step = len(sample_dt)


for i in range(len(xrays_df)):
    begin=xrays_df.iloc[i].dtBegin.hour
    complete=xrays_df.iloc[i].dtCompleted.hour
    if (begin >= 7 and complete <= 9):
        utilization[0] += 1
    else:
        if (begin >= 10 and complete <= 12):
            utilization[1] += 1
        else:
            if (begin>= 13 and complete <= 14):
                utilization[2] += 1
            else:
                if (begin >= 14 and complete <= 15):
                    utilization[3] += 1
                else:
                    if (begin >= 15 and complete <= 16):
                        utilization[4] += 1



utilization[2]+=utilization[3]
utilization[4]+=utilization[3]
max_room =max(xrays_room_day,key=lambda x:int(x))
max_wait = max(wait_days, key=lambda x: int(x))
max_utilization= max(utilization, key=lambda x: int(x))

print(max_room)
print(max_wait)
print(utilization)
print(max_utilization)













#start = pd.Timedelta("8h")
'''
    shift0_begin = xrays_df.iloc[index_step].dtBegin.replace(hour=15, minute=0, second=0)
        shift0_complete = xrays_df.iloc[index_step].dtBegin.replace(hour=16, minute=0, second=0)
        shift1_begin = xrays_df.iloc[index_step].dtBegin.replace(hour=14, minute=0, second=0)
        shift1_complete = xrays_df.iloc[index_step].dtBegin.replace(hour=15, minute=0, second=0)
        shift2_begin = xrays_df.iloc[index_step].dtBegin.replace(hour=13, minute=0, second=0)
        shift2_complete = xrays_df.iloc[index_step].dtBegin.replace(hour=14, minute=0, second=0)
        shift3_begin = xrays_df.iloc[index_step].dtBegin.replace(hour=10, minute=0, second=0)
        shift3_complete = xrays_df.iloc[index_step].dtBegin.replace(hour=12, minute=0, second=0)
        shift4_begin = xrays_df.iloc[index_step].dtBegin.replace(hour=7, minute=0, second=0)
        shift4_complete = xrays_df.iloc[index_step].dtBegin.replace(hour=9, minute=0, second=0)

        if (sample_dt.iloc[i].dtBegin >= shift0_begin and sample_dt.iloc[i].dtCompleted <= shift0_complete):
                utilization[0] += 1
        else:
            if (sample_dt.iloc[i].dtBegin >= shift1_begin and sample_dt.iloc[i].dtCompleted <= shift1_complete):
                    utilization[1] += 1
            else:
                if (sample_dt.iloc[i].dtBegin >= shift2_begin and sample_dt.iloc[i].dtCompleted <= shift2_complete):
                        utilization[2] += 1
                else:
                    if (sample_dt.iloc[i].dtBegin >= shift3_begin and sample_dt.iloc[i].dtCompleted <= shift3_complete):
                          utilization[3] += 1
                    else:
                        if (sample_dt.iloc[i].dtBegin >= shift4_begin and sample_dt.iloc[i].dtCompleted <= shift4_complete):
                              utilization[4] += 1



    day_temp= sample_dt.iloc[step-1].dtArrive.day
    month_temp = sample_dt.iloc[step-1].dtArrive.month
    hour_temp = sample_dt.iloc[step-1].dtArrive.hour
    minut_temp = sample_dt.iloc[step-1].dtArrive.minute


 print(stop_time)
            print(sample_dt)
            print(step)

lengths = []
for start_time in xrays_df_filtered.index:
    stop_time = start_time + offset
    chunk_length = xrays_df_filtered.loc[start_time:stop_time]

    record = (start_time, chunk_length)
    lengths.append(record)

print (max(lengths, key=lambda item: item[1]))
////
stop_time = start + offset
chunk_length = xrays_df.loc[(xrays_df.dtBegin.dt.hour >= start)]
print(chunk_length)
print(xrays_df)
'''
'''
start= xrays_df.iloc[70].dtBegin
print("hi")
print(start)
for i in range(0,len(xrays_df),100):
    print(xrays_df.iloc[i].dtBegin.month )
    print( str(i))
    
    
    
 ////
 
 
 d=0
start= xrays_df.iloc[0].dtArrive.hour
stop =pd.Timedelta("11hour")
for i in range(0,len(xrays_df),100):
   if (xrays_df.loc[i].dtBegin.hour > 11):
       d=d+1
print(str(str(d)))
print(start)   
'''
