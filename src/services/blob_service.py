import streamlit as st

from azure.storage.blob import BlobServiceClient
from utils.config import Config


def upload_blob(file, filename):
    try:
        service = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        client = service.get_blob_client(container=Config.CONTAINER_NAME, blob=filename)
        client.upload_blob(file, overwrite=True)
        return client.url
    except Exception as e:
        st.error(f"Erro ao enviar o arquivo para o Azure Blob Storage: {e}")
