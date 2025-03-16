import requests
from typing import Dict

class CLO3DClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.clo3d.com/v1"
        
    def generate_image(self, design_id: str, measurements: Dict[str, float]) -> bytes:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(
            f"{self.base_url}/designs/{design_id}/render",
            json={"measurements": measurements},
            headers=headers
        )
        response.raise_for_status()
        return response.content