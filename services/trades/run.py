from loguru import logger
from src.kraken_api import KrakenMockAPI
from quixstreams import Application

def main(
    kafka_broker_address: str ,
    kafka_topic: str ,
    product_id: str ,
    
):
    """
    It does 2 tasks:
    - Read data from kraken api 
    - and push data to the kafka topic

    Args:
        none

    Returns:
        one

    """
    logger.info("Starting the trades service")

    kraken_api = KrakenMockAPI(pair="MATIC/USD")

    # Initialize quixstream application
    # This is class handle all the low level details to connect to kafka
    app = Application(broker_address='localhost:9092')






    while True:
        trades = kraken_api.get_trades(pair="MATIC/USD")

        for trade in trades:
            # push trade to kafka
            # TODO

            logger.info(f"Push trade tokafka: {trade}")





if __name__ == "__main__":
    main()
