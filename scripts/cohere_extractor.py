import cohere
import sys
import os

sys.path.append(os.path.abspath(os.path.join('..')))
from config import config

#set up
api_key = config["COHERE_API_KEY"]
# Create and retrieve a Cohere API key from os.cohere.ai
co = cohere.Client(api_key)


class cohereExtractor():
    def __init__(self, train_datsets: list, test_datasets: list):
        self.train_datasets = train_datsets
        self.test_datasets = test_datasets

    def make_prompt(self):
        example_prompts = list()
        job_descriptions = list()
        task = "Task: Extract job description entites from this text: "
        prompt = ""
        for data in self.train_datasets[:3]:
            job_description = "JOB DESCRIPTION: " + data['document'] + task 
            example_prompts.append(job_description + "\n".join( [(token['entityLabel'] + ": " + token['text']) for token in data['tokens'] ]) + "\n---\n")
        
        for test_data in self.test_datasets[:3]:
            job_desc= "JOB DESCRIPTION: " + test_data['document'] + task
            job_descriptions.append(job_desc)

        prompts = example_prompts + job_descriptions
        prompt = "/n".join(prompts)
        return prompt

    def extract(self):
        try:
            extraction = co.generate(
                model='large',
                prompt=self.make_prompt(),
                max_tokens=100,
                temperature=0.9,
                stop_sequences=["---"])
            return(extraction.generations[0].text[:-1])
        except cohere.CohereError as e:
                print(e.message)
                print(e.http_status)
                print(e.headers)


