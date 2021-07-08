import os
import pandas as pd
import wandb
from google.cloud import storage


run = wandb.init(project="weave_whale", job_type="log_synth")
full_bucket = "gs://wandb-artifact-refs-public-test/whalesong/synth"
bucket = "wandb-artifact-refs-public-test" #/whalesong/synth"
dataset_at = wandb.Artifact('synth_songs',type="generated_data")
dataset_at.add_reference(full_bucket)

# now build a table
bucket_iter = storage.Client().get_bucket(bucket)
song_data = []
for synth_song in bucket_iter.list_blobs(prefix="whalesong/synth"):
  if not synth_song.name.endswith(".wav"):
    continue
  song_name = synth_song.name.split("/")[-1]
  print(song_name)
  # add a reference path for each song
  gs_song_path = os.path.join(full_bucket, song_name) 
  gs_audio = wandb.Audio(gs_song_path, sample_rate=32)
  # extract instrument
  orig_id, instrument = song_name.split("_")
  song_data.append([orig_id, song_name, gs_audio, instrument.split(".")[0]]) 

# create data table
table = wandb.Table(data=song_data, columns=["song_id", "song_name", "audio", "instrument"])
#songs_at = wandb.Artifact("synth_samples_2", type="synth_ddsp_2")
#songs_at.add(table, "synth_song_samples_2")
#run.log_artifact(songs_at)
run.log({"weave" : table})
#run.finish()  

