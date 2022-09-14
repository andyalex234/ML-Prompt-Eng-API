# Machine Learning prompt Engineering and entity extraction for LLMs API

## Why this project?
The complexity, cost, and skills required to produce LLMs is immense. Only larger companies and other international groups are able to train LLMs at the size of hundreds of billions of parameters. Given the benefit of LLMs to drive business and society, it is useful to learn to use these monster AI models for multiple use in business and social problems. 
The need for specialized skills in prompt engineering will grow fast as more and and more companies start building their business around LLMs and similar products such as DALL-E 2, MidJourney, Bloom, etc. 

## Data
There are two datasets you will use for this project

### Data 1:

This data comes from the client described above.  The columns of this data are as follows

- Domain - the base URL or a reference to the source these item comes from 
- Title - title of the item - the content of the item
- Description - the content of the item
- Body - the content of the item
- Link - URL to the item source (it may not functional anymore sometime)
- Timestamp - timestamp that this item was collected at
- Analyst_Average_Score -  target variable - the score to be estimated 
- Analyst_Rank - score as rank
- Reference_Final_Score - Not relevant for now - it is a transformed quantity


### Data 2:

The data are job descriptions ( together named entities)  and  relationships between entities in json format. 

- Dataset 1: [For development and training](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_dev.txt)
- Dataset 2: [For testing and final reporting](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_test.txt)


## API Documentation

- <code>/bnewscore</code> - for scoring  breaking news that may lead to public unrest
- <code>/jdentities</code> - for extracting entities from job 

>> for detailed information about the api documentation [visit - /docs](http://127.0.0.1:8000/docs)
