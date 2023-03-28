from fastapi import FastAPI,Depends,Request,HTTPException
from starlette.responses import RedirectResponse
from fastapi.security import APIKeyHeader
# import uvicorn

# from user import Users_id,UserInDB,User
# from test import scraper_1
from nandan import scraper_1
from tirupati import scraper_2
from mahabali import scraper_3


app = FastAPI()

nandan=scraper_1()
tirupati=scraper_2()
mahabali=scraper_3()
# author
API_KEY = "pratyanj"
# API_KEY = "12c666fe-6fcc-4e25-aa32-5d398ac6dfdf70d28731-5377-41b7-ab83-8ce1a710f0dcd5b52729-74e6-4837-886a-c5a5fbea8d77"

# Create an instance of the APIKeyHeader security scheme
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

# Define a dependency that will check the API key
async def check_api_key(api_key: str = Depends(api_key_header)):
    # if not api_key or api_key != f"Bearer {API_KEY}":
    if not api_key or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Enter invalid API key")

# # Define a protected route that requires the API key
# @app.get("/login for TO", dependencies=[Depends(check_api_key)])
# def protected():
#     return {"message": "login successful!"}
# *************************************scraper***********************************
@app.get("/tirupaticourier/{cid}",dependencies=[Depends(check_api_key)])
async def scraper_runner(cid:int):
    return tirupati.scrapedata(cid)

@app.get("/nandancourier/{cid}",dependencies=[Depends(check_api_key)])
async def scraper_runner(cid:int):
    return nandan.scrapedata(cid)
    
@app.get("/mahabalicourier/{cid}",dependencies=[Depends(check_api_key)])
async def scraper_runner(cid:int):
    return mahabali.scrapedata(cid)
# **********************************scraper********************************************
# --------------main page as docs----------------------------
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    response = RedirectResponse(url='/docs')
    return response
# ------------------------------------------------------------

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=30000)

