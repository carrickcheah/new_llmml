from datetime import datetime
from pydantic import BaseModel, field_validator
from typing import Optional

class Trade(BaseModel):
    """
    A trade from the Kraken API.
    """
    pair: str
    price: float
    volume: float
    timestamp: datetime
    timestamp_ms: int
    
    @classmethod
    def from_kraken_api_response(
        cls,
        pair: str,
        price: float,
        volume: float,
        timestamp: datetime,
    ) -> "Trade":
        return cls(
            pair=pair,
            price=price,
            volume=volume,
            timestamp=timestamp,
            timestamp_ms=cls._datestr2milliseconds(timestamp),
        )
    
    @staticmethod
    def _datestr2milliseconds(datestr: str) -> int:
        return int(datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp() * 1000)

    def to_str(self) -> str:
        # pydantic method to convert the model to a dict
        return self.model_dump_json()