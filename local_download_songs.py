import os
import pandas as pd
import wandb

run = wandb.init(project="cshanty", job_type="show_samples")
dataset_at = run.use_artifact("sample_songs:v1")
songs_dir = dataset_at.download()

metadata_csv = ""
for s in os.listdir(songs_dir):
  if s.endswith("metadata.csv"):
    metadata_csv = os.path.join(songs_dir, s)

metadata = pd.read_csv(metadata_csv)

columns = list(metadata.columns) #["id", "song", "species", "location", "date"]
data = metadata[["song_id", "filepath", "species", "location", "date"]].values
song_data = []
for d in data:
  local_song_path = os.path.join(songs_dir, str(d[1]))
  local_audio = wandb.Audio(local_song_path, sample_rate=32)
  song_data.append([d[0], local_audio, d[2], d[3], d[4]])

table = wandb.Table(data=song_data, columns=columns)
songs_at = wandb.Artifact("playable_songs", type="raw_data")
songs_at.add(table, "song_samples")
run.log_artifact(songs_at)
run.finish()  

