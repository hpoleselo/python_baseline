from fastapi import FastAPI, Response, status, HTTPException, File, UploadFile, Form
from schemas.post_request import PostRequestPayload
from utils.custom_logger import setup_custom_logger


logger = setup_custom_logger('api_logger')

description = """
# Example API
"""

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
    
        
