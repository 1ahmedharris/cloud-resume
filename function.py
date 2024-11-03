import logging
import os
import json
from azure.cosmos import CosmosClient, exceptions
import azure.functions as func

# Environment variables
COSMOS_DB_ENDPOINT = os.environ["COSMOS_DB_ENDPOINT"]
COSMOS_DB_KEY = os.environ["COSMOS_DB_KEY"]
DATABASE_NAME = "aitc-db"   # Replace with actual database name
TABLE_NAME = "VisitorCountTable"         # Replace with actual container name

# Initialize Cosmos client
client = CosmosClient(COSMOS_DB_ENDPOINT, COSMOS_DB_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(TABLE_NAME)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Function triggered to update visitor count.")
    try:
        # Define partition key and row key to match your Cosmos DB entry
        partition_key = "visitor-counter"
        row_key = "visitor-count"

        # Read current visitor count
        logging.info("Attempting to read item from Cosmos DB.")
        item = container.read_item(item=row_key, partition_key=partition_key)
        visitor_count = item.get("visitorCount", 0)
        logging.info(f"Current visitor count: {visitor_count}")

        # Increment and update count
        visitor_count += 1
        item["visitorCount"] = visitor_count
        container.upsert_item(item)
        logging.info(f"Visitor count updated to: {visitor_count}")

        # Return updated count as JSON
        return func.HttpResponse(
            json.dumps({"visitor_count": visitor_count}),
            status_code=200,
            mimetype="application/json"
        )
    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"Error accessing Cosmos DB: {str(e)}")
        return func.HttpResponse("Error accessing Cosmos DB.", status_code=500)
    except Exception as e:
        logging.error(f"General error: {str(e)}")
        return func.HttpResponse("An unexpected error occurred.", status_code=500)
