from contextlib import asynccontextmanager

from aiobotocore.session import get_session


class S3Client:
    def __init__(
            self, bucket_name: str, access_key: str, secret_key: str, endpoint_url: str, **kwargs
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
            **kwargs,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(self, file_path: str):
        object_key = file_path.split("/")[-1]
        async with self.get_client() as client:
            with open(file_path, "rb") as file:
                await client.put_object(Bucket=self.bucket_name, Key=object_key, Body=file)

    async def download_file(self, file_path: str):
        object_key = file_path.split("/")[-1]
        async with self.get_client() as client:
            response = await client.get_object(Bucket=self.bucket_name, Key=object_key)
            async with response["Body"] as stream:
                with open(file_path, "wb") as file:
                    file.write(await stream.read())


async def main():
    s3_client = S3Client(
        bucket_name="my-bucket",
        access_key="my-access-key",
        secret_key="my-secret",
        endpoint_url="http://localhost:9000",
    )

    await s3_client.upload_file("file.txt")