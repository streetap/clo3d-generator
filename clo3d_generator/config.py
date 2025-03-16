from dataclasses import dataclass
from typing import Dict

@dataclass
class AppConfig:
    clo3d_api_key: str
    gcs_bucket: str
    designs: Dict[str, str]