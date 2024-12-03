from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime   

class Trade(BaseModel):
            symbol: List[str]   
            price: float
            qty: float
            timestamp: datetime
            timestamp_ms: int            

class KrakenMockAPI:
    def __init__(self, symbol: List[str]):
        self.symbol = symbol

    def get_trades(self) -> List[Trade]:
        """
        Returns a list of Trade objects.
        """

        mock_trades = [
            Trade(symbol=self.symbol,
                    price=0.5117,
                    qty=40.0,
                    timestamp="2023-09-25T07:49:37.708706Z",
                    timestamp_ms=1663981377708
                    ),
                                  
            Trade(symbol=self.symbol,
                    price=0.5887,
                    qty=40.0,
                    timestamp="2023-09-25T07:49:37.708706Z",
                    timestamp_ms=1663981377708
                    )
        ]

        return mock_trades















