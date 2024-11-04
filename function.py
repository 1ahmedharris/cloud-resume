import os
import azure.functions as func
from azure.cosmos import CosmosClient, exceptions

# Set up the environment variables
COSMOS_DB_ENDPOINT = os.getenv("https://aitc-db.table.cosmos.azure.com:443/")
COSMOS_DB_KEY = os.getenv("NOyS8hh3lWLG9sAdh9iRUkxohF1yzOFCsuZVrzNk6u0MULWjfnDk1HotDiibAH4To1gKajOCUVGNACDbVo9DZg==")
DATABASE_NAME = "TablesDB"  # Replace with your actual database name
CONTAINER_NAME = "VisitorCountTable"  # Replace with your actual table/container name

# Define partition key and document ID
PARTITION_KEY = "visitor-counter"  # Your actual partition key value
DOCUMENT_ID = "visitor-count"  # RowKey for the document

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Initialize Cosmos DB client
        client = CosmosClient(COSMOS_DB_ENDPOINT, COSMOS_DB_KEY)
        database = client.get_database_client(DATABASE_NAME)
        container = database.get_container_client(CONTAINER_NAME)

        # Retrieve the item with the specified partition key and document ID
        try:
            item = container.read_item(item=DOCUMENT_ID, partition_key=PARTITION_KEY)
            visitor_count = item.get("visitorCount", 0)  # Adjust 'visitorCount' if needed
            return func.HttpResponse(
                body=f'{{"visitor_count": {visitor_count}}}',
                status_code=200,
                mimetype="application/json"
            )
        except exceptions.CosmosHttpResponseError as e:
            # Handle specific error if item does not exist or other issues arise
            return func.HttpResponse(
                body=f'{{"error": "Error retrieving visitor count: {e.message}"}}',
                status_code=500,
                mimetype="application/json"
            )
    except Exception as e:
        # Handle any general errors related to Cosmos DB connection or configuration
        return func.HttpResponse(
            body=f'{{"error": "Connection failed: {str(e)}"}}',
            status_code=500,
            mimetype="application/json"
        )
