import os
import pandas as pd
import wandb

bucket_name ="wandb-artifact-refs-public-test"
folder_name = "whalesong"

run = wandb.init(project="cshanty", job_type="show_samples")

# fetch the metadata index locally 
dataset_at = run.use_artifact("sample_songs:latest")
metadata_file = dataset_at.get_path("song_metadata.csv")
metadata_csv = metadata_file.download()
metadata = pd.read_csv(metadata_csv)
columns = list(metadata.columns)
data = metadata[columns].values

song_data = []
for d in data:
  # add a reference path for each song
  gs_song_path = os.path.join("gs://", bucket_name, folder_name, str(d[1]))
  gs_audio = wandb.Audio(gs_song_path, sample_rate=32)
  song_data.append([d[0], gs_audio, d[2], d[3], d[4]])

# create data table
table = wandb.Table(data=song_data, columns=columns)
songs_at = wandb.Artifact("playable_songs", type="raw_data")
songs_at.add(table, "song_samples")
run.log_artifact(songs_at)
run.finish()  

