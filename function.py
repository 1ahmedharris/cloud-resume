import logging
import os
import json
from azure.cosmos import CosmosClient, exceptions
import azure.functions as func

# Connection settings from environment variables
COSMOS_DB_ENDPOINT = os.environ["COSMOS_DB_ENDPOINT"]
COSMOS_DB_KEY = os.environ["COSMOS_DB_KEY"]
DATABASE_NAME = "aitc-db"   # Replace with your actual database name
TABLE_NAME = "VisitorCountTable"         # Replace with your actual container name

# Initialize Cosmos client
client = CosmosClient(COSMOS_DB_ENDPOINT, COSMOS_DB_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(TABLE_NAME)

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Define partition key and row key values to match your Cosmos DB table entry
        partition_key = "visitor-counter"
        row_key = "visitor-count"

        # Read the current visitor count from Cosmos DB
        item = container.read_item(item=row_key, partition_key=partition_key)
        visitor_count = item.get("visitorCount", 0)

        # Increment and update the visitor count
        visitor_count += 1
        item["visitorCount"] = visitor_count
        container.upsert_item(item)

        # Return the updated count as JSON
        return func.HttpResponse(
            json.dumps({"visitor_count": visitor_count}),
            status_code=200,
            mimetype="application/json"
        )
    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"Error accessing Cosmos DB: {str(e)}")
        return func.HttpResponse("An error occurred while retrieving the visitor count.", status_code=500)
