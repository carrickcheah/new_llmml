# Step by step guidance of this module

## Session 1

This module focuses on building an ingest microservice with two main tasks:  

1. Read data from the Kraken API.  
2. Push the data to Kafka Topic 1.  

### Basic set up ofproject structure

a

### Task 2: running redpanda locally  

- create docker-compose folder
- create Makefile
- bash$ start-redpanda ,and makesure Redpanda is running locally.

### Task 3   Mock trade data

The first mock ensures the code functions correctly.  
subtrade.run_mock.py and subtrade.kraken_api.mock.py is the template.  

The second mock integrates QuixStream to push data to a Kafka topic.  
subtrade.run_mock_2.py and subtrade.kraken_api.mock_2.py is the template.  

### Task 4   Extract config with pydantic settings


### Task 5 Kraken websocket API integration


### Task 6 Kraken websocket API integration


### Task 7 Kraken websocket API integration


### Reflection on the lessons learnt  


## Session 2

- dockerize trade producer  
      - write docker file  
      - build docker image  
      - Run a docker container

- add precommit hooks for automatic linting and formatting  

- build candle service ( transform mirco service )  
      - write docker file  

### Task 1

