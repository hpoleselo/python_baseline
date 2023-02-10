from fastapi import FastAPI, Response, status, HTTPException
from schemas.post_request import PostRequestPayload
from utils.custom_logger import setup_custom_logger


logger = setup_custom_logger('api_logger')

description = """
# Dashboard Interface API
API that provides interface with the Dashboard, like:
- Inserting Project to be tracked.
- Get active projects array.
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
        