from huggingface_hub import snapshot_download

try:
    path = snapshot_download(
        repo_id="project-boli/irula",
        repo_type="dataset",
        local_dir="irula_dataset"
    )

    print("\nDataset downloaded successfully!")
    print("Dataset location:", path)

except Exception as e:
    print("\nDownload failed!")
    print(e)