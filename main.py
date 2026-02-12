from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from pydantic import BaseModel, ConfigDict
from scripts.helloworld import hello_world
from scripts.check_skill_dependencies import check_skill_dependencies_api

class skillRequest(BaseModel):
    skill: int
    token: str

    model_config = ConfigDict(extra='ignore')

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/api/account/{accountId}")
async def return_values(accountId: str, skillRequest: skillRequest):
    res = check_skill_dependencies_api(accountId, skillRequest.token, skillRequest.skill)
    return res

@app.get("/api/account/{accountId}")
async def return_hello(accountId: str):
    return {"accountId": accountId, "message": hello_world()}

@app.post("/api/account/{accountId}/skill/{skillId}/test")
async def test(accountId: str, skillId: int, token: Annotated[str, Depends(oauth2_scheme)]):
    res = check_skill_dependencies_api(accountId, token, skillId)
    return res

