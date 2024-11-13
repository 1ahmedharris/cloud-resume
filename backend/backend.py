import logging

def main(context: func.Context, req: func.HttpRequest, data) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    context.bindings.outputDocument = data[0]
    context.bindings.outputDocument['count'] += 1
    return func.HttpResponse(
        body=str(data[0]['count'])
    )
