import os
import pandas as pd
import wandb
from google.cloud import storage


run = wandb.init(project="weave_whale", job_type="explore")

# synth songs table
synth_songs = run.use_artifact('stacey/cshanty/synth_samples:latest')
synth_table = synth_songs.get("synth_song_samples")

# original songs table
orig_songs = run.use_artifact('stacey/cshanty/playable_songs:latest') 
orig_table = orig_songs.get("song_samples")

join_table = wandb.JoinedTable(synth_table, orig_table, "song_id") # "orig_id")

run.log({"weave" : join_table})
 
#join_at = wandb.Artifact("synth_summary_3", "analysis_3")
#join_at.add(join_table, "synth_explore")
#run.log_artifact(join_at)

