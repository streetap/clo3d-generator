from google.cloud import storage
from datetime import datetime

class CloudStorage:
    def __init__(self, bucket_name: str):
        self.client = storage.Client()
        self.bucket = self.client.bucket(bucket_name)
        
    def upload_image(self, image_data: bytes, design_id: str) -> str:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        blob_name = f"renders/{design_id}/{timestamp}.png"
        blob = self.bucket.blob(blob_name)
        blob.upload_from_string(image_data, content_type='image/png')
        return blob.public_url