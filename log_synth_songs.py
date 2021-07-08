import wandb

run = wandb.init(project="cshanty", job_type="local_viz")
dataset_at = run.use_artifact("synth_samples:latest")
songs_dir = dataset_at.download()
