
from azure.cosmos import CosmosClient, PartitionKey, PatchOperation

# Replace with your Cosmos DB endpoint and key
endpoint = "YOUR_COSMOS_DB_ENDPOINT" 
key = "YOUR_COSMOS_DB_KEY" 

# Replace with your database and container name
database_name = "YOUR_DATABASE_NAME"
container_name = "YOUR_CONTAINER_NAME"

client = CosmosClient(endpoint, key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Replace with your document ID and partition key
document_id = "YOUR_DOCUMENT_ID"
partition_key = "YOUR_PARTITION_KEY"

# Increment the 'count' field by 1
patch_operations = [
    PatchOperation.Increment("/count", 1)
]

response = container.patch_item(
    item=document_id, 
    partition_key=partition_key, 
    patch_operations=patch_operations
)

print(response.resource)
