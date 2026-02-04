import kagglehub

# Download latest version
cereals_path = kagglehub.dataset_download("crawford/80-cereals")

print("Path to dataset files:", cereals_path)