import wandb

run = wandb.init(project="whalesong")
#wandb.log({"example" : [wandb.Audio("best_whale.wav", caption="Best whale", sample_rate=32)]})
#wb_song = wandb.Audio("best_whale.wav", caption="Best whale", sample_rate=32)

other_songs = [
["88006034", "88006034.wav", "Bowhead Whale", "Bailie Is., Beaufort Sea X", "03-Oct-1988"],
["55113001", "55113001.wav", "Humpback Whale", "St. David's Island, Bermuda", "30-Apr-1953"],
["6301900Y", "6301900Y.wav", "Humpback Whale", "Argus Island, Bermuda", "26-Mar-1963"],
["54024008", "54024008.wav", "Long-Finned Pilot Whale", "Trinity Bay, Newfoundland", "18-Jul-1954"]
]

ref_urls = ["https://cis.whoi.edu/science/B/whalesounds/WhaleSounds/78018002.wav", "https://cis.whoi.edu/science/B/whalesounds/WhaleSounds/88006034.wav", "https://whoicf2.whoi.edu/science/B/whalesounds/WhaleSounds/55113001.wav", "https://whoicf2.whoi.edu/science/B/whalesounds/WhaleSounds/6301900Y.wav", "https://whoicf2.whoi.edu/science/B/whalesounds/WhaleSounds/54024008.wav"]

song_at = wandb.Artifact("ref_songs_new", type="ref_songs_new")

columns = ["id", "song", "species", "location", "date"]
#table = wandb.Table(columns=columns)
for ru, s in zip(ref_urls, other_songs[1:]):
  # create an artifact by reference???
  song_at.add_reference(ru, name=ru)
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
run.log_artifact(song_at)
run.finish()
