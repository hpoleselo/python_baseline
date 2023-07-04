from fastapi import FastAPI, Response, status, HTTPException, File, UploadFile, Form
from schemas.post_request import PostRequestPayload
from utils.custom_logger import setup_custom_logger
from config import configuration


logger = setup_custom_logger('api_logger')

description = """
# Example API
"""

# This is set in the config package in the yaml file
isLocalTesting = configuration['local_testing']

def check_credentials_from_api_wrt_gcp(gcp_project_name: str,
                                       gcp_table_name: str):
    """
    Checks if given API is able to authenticate with GCP.
    """
    from google.api_core.exceptions import NotFound, BadRequest
    from google.auth.exceptions import DefaultCredentialsError
    
    try:
        table = 'project_metrics_daily_new'
        bigquery_client, project_id, dataset_id, table_name, table_id = big_query_config(table)
    except DefaultCredentialsError as e:
        logger.error(f"As soon as the API started it could not retrieve credentials from GCP. {e}")

check_credentials_from_api_wrt_gcp()

app = FastAPI(description=description,
              title="FastAPI Example",
              version="0.0.1",
              contact={
                  "name": "Henrique Poleselo",
                  "email": "hpoleselo@example.com"
              },
              license_info={
                  "name": "Apache 2.0",
                  "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
              },
              redoc_url=None,)

@app.post("/new_data")
def insert_new_data_to_somewhere(body: PostRequestPayload):
    logger.print(f"Inserting new data to a DB...")

    succeeded = True

    if succeeded:
        logger.info("Succesfull.")
        # TODO: Add HTTP response
        return "Ok"
    else:
        return "Not ok."

@app.post('/file_log_upload')
async def create_upload_file(uploader_name: str = Form(...),
                             file : UploadFile = File(default=None)):
                             
    file_location = f'images/{uploader_name}_{file.filename}'
    logger.info(f"File will be outputted to {file_location}")
    return "Ok."
    
        
