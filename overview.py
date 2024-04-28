import pandas as pd 
import zipfile
from datetime import timedelta


zipfile = zipfile.ZipFile('my_spotify_data.zip', 'r')
audiodfs = []

# data includes both video and audio --> extract only audiofile json data
for name in zipfile.namelist():
    if "Streaming_History_Audio_" not in name:
        continue
    audiodfs.append(pd.read_json(zipfile.open(name)))

# concatinate into single dataframe
audiodf = pd.concat(audiodfs)

#print info
print("Columns:", audiodf.columns.values)
print("Number of streams:", str(audiodf.shape[0]))
print(timedelta(milliseconds = int(audiodf['ms_played'].sum())))
