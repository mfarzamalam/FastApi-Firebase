import pyrebase
from fastapi import FastAPI


config = {
    "apiKey": "AIzaSyBiM7pShglQoWESauwAhsmnDFYzFrBwj3k",
    "authDomain": "testing-with-fastapi.firebaseapp.com",
    "projectId": "testing-with-fastapi",
    "storageBucket": "testing-with-fastapi.appspot.com",
    "messagingSenderId": "117877501282",
    "appId": "1:117877501282:web:b7916553b4c2d24cf8503b",
    "measurementId": "G-JLPNZ0GLGC",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.post("/signup/")
async def signup(email: str, password: str):
    try:
        auth.create_user_with_email_and_password(email, password)
        return {"msg": "Success"}
    except Exception as e:
        return {"error": e}



@app.post("/login/")
async def login(email: str, password: str):
    try:
        login_user = auth.sign_in_with_email_and_password(email, password)
        return {"msg": login_user}
    except Exception as e:
        return {"error": e}



@app.get("/get_user_detail/")
async def get_user_detail(user_token: str):
    try:
        login_user = auth.get_account_info(user_token)
        data_dict = {}
        data_dict = login_user.get('users')[0]
        data_dict.pop('passwordHash')
        data_dict.pop('passwordUpdatedAt')
        data_dict.pop('providerUserInfo')
        data_dict.pop('validSince')
        data_dict.pop('lastRefreshAt')
        return data_dict
    except Exception as e:
        return {"error": e}