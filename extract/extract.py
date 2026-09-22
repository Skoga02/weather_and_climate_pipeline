from azure.storage.blob import BlobServiceClient
import pandas as pd

def upload_to_blob(df: pd.DataFrame, blob_name: str):
    client = BlobServiceClient.from_connection_string(CONN_STRING)
    container = client.get_container_client("raw-weather")
    container.upload_blob(name=blob_name, data=df.toparquet(), overwrite=True)
