import logging
import azure.functions as func 
from azure.storage.blob import ContainerClient
import sys
import os
from sys import path
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)
from azure.storage.blob import BlobServiceClient



def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')
    container = req.params.get('container')
    if not container:

        return func.HttpResponse(

            "Warning, missing parameter",

            status_code=200

        )

    if container:
        # The name of containers that you need to create.
        lista_container = ['Original_files', 'Cleaned_files']
        container = f'{container}_files'
        if container in lista_container :
            connection_string = "<your_connection_string>"
            blob_service_client = BlobServiceClient.from_connection_string(connection_string)
                    # Instantiate a new ContainerClient
            container_client = blob_service_client.get_container_client(container)
                        # Create new container in the service
            container_client.create_container()
                        # List containers in the storage account
            list_response = blob_service_client.list_containers()

            return func.HttpResponse("Container created with success!!" , status_code=200)

        else:
            return func.HttpResponse(f'Name not allowed!, these are the allowed names: {lista_container}', status_code = 200)

        

        
