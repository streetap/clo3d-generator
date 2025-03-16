from typing import Dict
import json

class MeasurementParser:
    REQUIRED_FIELDS = ['chest', 'waist', 'hip', 'length']
    
    def parse(self, file_path: str) -> Dict[str, float]:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        for field in self.REQUIRED_FIELDS:
            if field not in data["measurements"]:
                raise ValueError(f"Missing required measurement: {field}")
                
        return {k: float(v) for k, v in data["measurements"].items()}