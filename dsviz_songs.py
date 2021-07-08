import os
import wandb
from google.cloud import storage

bucket_name ="wandb-artifact-refs-public-test"
bucket = storage.Client().get_bucket(bucket_name)
for blob in bucket.list_blobs(prefix="whalesong/"):
  print(blob.name)

run = wandb.init(project="whalesong_ref", job_type="show_samples")

songs = [
["78018002", "78018002.wav","Bowhead Whale", "Barrow, Alaska CC2A", "10-May-1978"],
["88006034", "88006034.wav", "Bowhead Whale", "Bailie Is., Beaufort Sea X", "03-Oct-1988"],
["55113001", "55113001.wav", "Humpback Whale", "St. David's Island, Bermuda", "30-Apr-1953"],
["6301900Y", "6301900Y.wav", "Humpback Whale", "Argus Island, Bermuda", "26-Mar-1963"],
["54024008", "54024008.wav", "Long-Finned Pilot Whale", "Trinity Bay, Newfoundland", "18-Jul-1954"]
]

dataset_at = run.use_artifact("sample_songs:latest")
songs_dir = dataset_at.download()
for s in os.listdir(songs_dir):
  print(s)

run.finish()

#"https://storage.googleapis.com/wandb-artifact-refs-public-test/whalesong/54024008.wav"

#ref_urls = ["https://cis.whoi.edu/science/B/whalesounds/WhaleSounds/78018002.wav", "https://cis.whoi.edu/science/B/whalesounds/WhaleSounds/88006034.wav", "https://whoicf2.whoi.edu/science/B/whalesounds/WhaleSounds/55113001.wav", "https://whoicf2.whoi.edu/science/B/whalesounds/WhaleSounds/6301900Y.wav", "https://whoicf2.whoi.edu/science/B/whalesounds/WhaleSounds/54024008.wav"]

#columns = ["id", "song", "species", "location", "date"]
#table = wandb.Table(columns=columns)
#for ru, s in zip(ref_urls, other_songs[1:]):
  # create an artifact by reference???
#  song_at.add_reference(ru, name=ru)
 # wb_song = wandb.Audio(ru, caption=s[3], sample_rate=32)
  #table.add_data(s[0], s[1], s[2], s[3], s[4])

#ref_song = "https://whoicf2.whoi.edu/science/B/whalesounds/WhaleSounds/54024001.wav"
  

##### as objects
#table.add_data("78018002", wb_song, "Bowhead Whale", "Barrow, Alaska CC2A", "10-May-1978")
#for s in other_songs:
#  wb_s = wandb.Audio(s[1], caption=s[3] + "/" + s[4], sample_rate=32)
#  s[1] = wb_s
#  table.add_data(*s)

#song_at.add(table, "sample_songs")
#run.log_artifact(song_at)
#run.finish()
