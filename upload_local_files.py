import os
import pandas as pd
import wandb
from google.cloud import storage

# remote bucket reference
bucket_name ="wandb-artifact-refs-public-test"
bucket = storage.Client().get_bucket(bucket_name)
print(bucket)
blob = bucket.blob("whalesong/song_metadata.csv") #"gs://" + bucket_name + "/whalesong/song_metadata.csv")
print(blob)
blob.upload_from_filename("song_metadata.csv")

