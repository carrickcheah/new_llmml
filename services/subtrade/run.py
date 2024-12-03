from loguru import logger
from kraken_api.mock import KrakenMockAPI, Trade


def main(
    # kafka_topic: str,
    # kafka_broker_address: str,
    # kraken_api: str,
):
    """
    Do 2 things:
    - read data from kraken websocket api,
    - write data to kafka topic.

    Args:
    - kafka_topic: str, kafka topic name.
    - kafka_broker_address: str, kafka broker address.
    - kraken_api: str, kraken api address.
    
    """

    logger.info("Starting subtrade service")

    kraken_api = KrakenMockAPI(symbol=["PEPE/USD"])

    while True:
        trades = kraken_api.get_trades()

        for trade in trades:
            logger.info(f"Writing trade to Kafka: {trade}")
            # write_trade_to_kafka(kafka_topic, kafka_broker_address, trade)




if __name__ == "__main__":

    main(
        # kafka_topic="trade2",
        # kafka_broker_address="localhost:9092",
    )

