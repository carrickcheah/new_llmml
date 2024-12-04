from loguru import logger
from kraken_api.mock_2 import KrakenMockAPI, Trade
from quixstreams import Application
from config import config



def main(
    kafka_topic: str,
    kafka_broker_address: str,
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

    kraken_api = KrakenMockAPI(symbol="BTC/USD")


    # Define an application that will connect to Kafka
    app = Application(
        broker_address=kafka_broker_address,
    )

    topic = app.topic(name=kafka_topic, value_serializer="json")


    # Create a Producer instance
    with app.get_producer() as producer:

        while True:
            trades = kraken_api.get_trades()

            for trade in trades:
                # Serialize an event using the defined Topic 
                message = topic.serialize(
                    key=trade.symbol, 
                    value=trade.to_str(),
                )

                # Produce a message into the Kafka topic
                producer.produce(
                    topic=topic.name, value=message.value, key=message.key
                )

                logger.info(f"Produced message: {trade}")





if __name__ == "__main__":

    main(
        kafka_topic=config.kafka_topic,
        kafka_broker_address=config.kafka_broker_address,
    )

