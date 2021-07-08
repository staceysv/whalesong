import os
import pandas as pd
import wandb
from google.cloud import storage


run = wandb.init(project="weave_whale", job_type="log_synth")

other_songs = [
["78018002", "78018002.wav", "Bowhead Whale", "Barrow;Alaska CC2A", "10-May-1978"],
["88006034", "88006034.wav", "Bowhead Whale", "Bailie Is., Beaufort Sea X", "03-Oct-1988"],
["55113001", "55113001.wav", "Humpback Whale", "St. David's Island, Bermuda", "30-Apr-1953"],
["6301900Y", "6301900Y.wav", "Humpback Whale", "Argus Island, Bermuda", "26-Mar-1963"],
["54024008", "54024008.wav", "Long-Finned Pilot Whale", "Trinity Bay, Newfoundland", "18-Jul-1954"]
]

ref_urls = ["https://cis.whoi.edu/science/B/whalesounds/WhaleSounds/78018002.wav", "https://cis.whoi.edu/science/B/whalesounds/WhaleSounds/88006034.wav", "https://whoicf2.whoi.edu/science/B/whalesounds/WhaleSounds/55113001.wav", "https://whoicf2.whoi.edu/science/B/whalesounds/WhaleSounds/6301900Y.wav", "https://whoicf2.whoi.edu/science/B/whalesounds/WhaleSounds/54024008.wav"]


songs_by_id = {}
s_meta = {}
columns = ["id", "song", "species", "location", "date"]
#table = wandb.Table(columns=columns)
for ru, s in zip(ref_urls, other_songs):
  # create an artifact by reference???
  #song_at.add_reference(ru, name=ru)
  song_file = "whale_songs/" + s[0] + ".wav"
  wb_song = wandb.Audio(song_file, caption=s[3], sample_rate=32)
#  table.add_data(s[0], s[1], s[2], s[3], s[4])
  songs_by_id[s[0]] = wb_song
  s_meta[s[0]] = s

print(songs_by_id)


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
  orig_song = songs_by_id[orig_id]
  song_meta = s_meta[orig_id]
  song_data.append([orig_id, orig_song, gs_audio, instrument.split(".")[0], song_name, song_meta[2], song_meta[3], song_meta[4]]) 

# create data table
table = wandb.Table(data=song_data, columns=["song_id", "source_song", "synth_song", "instrument", "song_name", "species", "location", "date"])
#songs_at = wandb.Artifact("synth_samples_2", type="synth_ddsp_2")
#songs_at.add(table, "synth_song_samples_2")
#run.log_artifact(songs_at)
run.log({"cshanty_5" : table})
#run.finish()  

