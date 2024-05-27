### Some scripts for personal use


## 1. [**`python_staff/s3_client.py`**](python_staff/s3_client.py)
- Base async client for S3
- Usage:
```python
from s3_client import S3Client

s3_client = S3Client(
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key',
    region_name='region_name',
    bucket_name='bucket_name'
)

# Upload file
await s3_client.upload_file("file.txt")
```

## 2. [**`bash_scripts/set_wacom_monitors.sh`**](bash_scripts/set_wacom_monitors.sh`)

- Script for setting up Wacom tablet for multiple monitors
- Usage:
```bash
bash set_wacom_monitors.sh
```
