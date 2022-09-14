from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# /bnewscore - for scoring breaking news that may lead to public unrest

@app.get('/bnewscore')
async def newscore(news):
    return {"socre": news}

# /jdentities - for extracting entities from job description
@app.get('/jdentities')
async def jdentities(job):
    return {"job": job}

