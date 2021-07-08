import os
import pandas as pd
import wandb
from google.cloud import storage

# remote bucket reference
bucket_name ="wandb-artifact-refs-public-test"
bucket = storage.Client().get_bucket(bucket_name)



# method 1: iterate over bucket contents
song_files = {}
for blob in bucket.list_blobs(prefix="whalesong/"):
  print(blob.name)
  filename = blob.name.split("/")
  if filename[1] and len(filename[1]) > 0 and not filename[1].endswith("csv"):
    song_files[str(filename[1])] = os.path.join("gs://" + bucket_name, blob.name) 

run = wandb.init(project="weave_whale", job_type="show_samples")
dataset_at = run.use_artifact("stacey/cshanty/sample_songs:v2")
songs_dir = dataset_at.download()

metadata_csv = "./song_metadata.csv"

metadata = pd.read_csv(metadata_csv)

print(song_files)

columns = ["id", "song", "species", "location", "date"]
data = metadata[["song_id", "filepath", "species", "location", "date"]].values
song_data = []
for d in data:
  gs_song_path = song_files[str(d[1])]
  gs_audio = wandb.Audio(gs_song_path, sample_rate=32)
  song_data.append([d[0], gs_audio, d[2], d[3], d[4]])

table = wandb.Table(data=song_data, columns=columns)
run.log({"original_songs" : table})
#songs_at = wandb.Artifact("play_songs", type="play_songs")
#songs_at.add(table, "song_samples")
#run.log_artifact(songs_at)
#run.finish()  

