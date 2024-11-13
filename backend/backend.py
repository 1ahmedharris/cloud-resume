
from azure.cosmos import CosmosClient, PartitionKey, PatchOperation

# Replace with your Cosmos DB endpoint and key
endpoint = "COSMOS_DB_ENDPOINT" 
key = "COSMOS_DB_KEY" 

# Replace with your database and container name
database_name = "TablesDB"
container_name = "VisitorCountTable"

client = CosmosClient(endpoint, key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Replace with your document ID and partition key
document_id = "visitor-count"
partition_key = "visitor-counter"

# Increment the 'count' field by 1
patch_operations = [
    PatchOperation.Increment("/visitorCount", 1)
]

response = container.patch_item(
    item=document_id, 
    partition_key=partition_key, 
    patch_operations=patch_operations
)

print(response.resource)
