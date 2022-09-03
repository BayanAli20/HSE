import pandas as pd
import numpy as np

xrays_df = pd.read_excel("XRays.xlsx").sort_values(by = "dtBegin")

# some stats
#xrays_df.head(50)
#np.shape(xrays_df)

# убираем дубликаты ID пациентов
xrays_df_filtered = xrays_df.drop_duplicates(subset = "stMRN")

# настраиваем время начала и конца обследования с 7 утра до 8 вечера
xrays_df_filtered = xrays_df_filtered[(xrays_df_filtered.dtBegin.dt.hour > 7) & (xrays_df_filtered.dtCompleted.dt.hour < 20)]
#xrays_df_filtered.head()


# итерация по 30 минутам и получение максимального количества уникальных stMRN (ID пациента) в каждом 30 минутном чанке
xrays_df_filtered= xrays_df_filtered.set_index("dtBegin")
offset = pd.Timedelta("30min")

lengths = []
for start_time in xrays_df_filtered.index:
    stop_time = start_time + offset
    chunk_length = xrays_df_filtered.loc[start_time:stop_time].shape[0]
    
    record = (start_time, chunk_length)
    lengths.append(record)
    
max(lengths, key=lambda item: item[1])



