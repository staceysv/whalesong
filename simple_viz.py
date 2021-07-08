import wandb
import os
import csv

metadata = {}
with open('song_metadata.csv', 'r',) as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i == 0:
            continue
        song_id = row[0]
        song_caption = ";".join(row[2:3])
        metadata[song_id] = song_caption

wandb.init(project="cshanty", job_type="local viz")
songs = []
by_instrument = {}
for song_file in os.listdir("synth_whale_songs"):
  print(song_file)
  _id, instrument = song_file.split(".")[0].split("_")
  caption = metadata[_id] + " on " + instrument
  audio = wandb.Audio("synth_whale_songs/"+song_file,
          caption = caption,
          sample_rate=32)
  songs.append(audio)
  if instrument in by_instrument:
      by_instrument[instrument].append(audio)
  else:
      by_instrument[instrument] = [audio]

wandb.log({"synth_songs" : songs})
for i, song_list in by_instrument.items():
    wandb.log({i : song_list})
