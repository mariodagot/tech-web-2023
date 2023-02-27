import logging
import json
import azure.functions as func


def get_pokemon(req: func.HttpRequest, table_client: func.TableService) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a GET request for Pokemon entity.')

    # Retrieve the partition key and row key from the request URL
    partition_key = req.route_params.get('partition_key')
    row_key = req.route_params.get('row_key')

    # Define the name of the table to use for the Pokemon entity
    table_name = 'Pokemon'

    if partition_key and row_key:
        # Retrieve a single Pokemon entity
        try:
            entity = table_client.get_entity(table_name, partition_key, row_key)
            return func.HttpResponse(json.dumps(entity), status_code=200)
        except Exception as e:
            return func.HttpResponse(f'Error: {str(e)}', status_code=500)
    else:
        # Retrieve a list of all Pokemon entities
        try:
            entities = table_client.query_entities(table_name)
            return func.HttpResponse(json.dumps(entities), status_code=200)
        except Exception as e:
            return func.HttpResponse(f'Error: {str(e)}', status_code=500)
