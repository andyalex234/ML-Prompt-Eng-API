from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
import sys
import json
import pandas as pd

class FileUpload(BaseModel):
    file: Union[str, bytes]

sys.path.append('../scripts')

from scripts.cohere_extractor import cohereExtractor


app = FastAPI()


@app.post('/jdentities')
async def extract_entities_from_file(file: UploadFile = File() ):
    extracted_entities = []
    try:
        df = pd.read_csv(file.file)
        co = cohereExtractor(df)
        result = co.extract()
        extracted_entities.append(result)
    except Exception as e:
        pass
    return json.dumps(extracted_entities)

# /jdentities - for extracting entities from job description
@app.post('/jdentities')
async def jdentities(job_discription: JobDescription):
    return {"job": job_discription}


