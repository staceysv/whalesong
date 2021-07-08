# Watkins Marine Mammal Database
# https://whoicf2.whoi.edu/science/B/whalesounds/index.cfm

import wandb

run = wandb.init(project="cshanty", job_type="upload")

bucket = "gs://wandb-artifact-refs-public-test/whalesong"
dataset_at = wandb.Artifact('sample_songs', type="raw_data")
dataset_at.add_reference(bucket)
run.log_artifact(dataset_at)
run.finish()
