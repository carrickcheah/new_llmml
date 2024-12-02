# Mock the kraken API
from pydantic import BaseModel
from typing import List
import json
from datetime import datetime
# from websocket import create_connection
from loguru import logger



class Trade(BaseModel):
    """
    A sample trade from the kraken API

                "symbol": "MATIC/USD",
                "side": "sell",
                "price": 0.5117,
                "qty": 40.0,
                "ord_type": "market",
                "trade_id": 4665906,
                "timestamp": "2023-09-25T07:49:37.708706Z"

    """
    pair: str
    price: float
    volume: float
    timestamp: datetime
    timestamp_ms: int

class KrakenMockAPI:
    """
    returns a list of trades from the kraken API
    """

    def __init__(self,pair: str):
        self.pair = pair

    def get_trades(self, pair: str) -> List[Trade]:
        mock_trade = [
            Trade(pair=self.pair, price=0.5117, volume=40.0, timestamp=datetime.now(), timestamp_ms=1632546577708),
            Trade(pair=self.pair, price=0.5887, volume=40.0, timestamp=datetime.now(), timestamp_ms=1632546577708),
        ]

        return mock_trade





        