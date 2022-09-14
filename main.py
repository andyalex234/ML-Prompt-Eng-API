from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

class JDEntity(BaseModel):
    domain: str
    title: str
    description: str
    body: str
    link: str
    timestamp: str
    analyst_average_score: float
    analyst_rank: float
    reference_final_score: float

class JobDescription(BaseModel):
    job_discription: str

app = FastAPI()

# /bnewscore - for scoring breaking news that may lead to public unrest

@app.get('/bnewscore')
async def bnewscore(news):
    return {"socre": news}

# /jdentities - for extracting entities from job description
@app.post('/jdentities')
async def jdentities(job_discription: JobDescription):
    return {"job": job_discription}
