MADICES 2 2024 - SEMANTIC ANNOTATION GROUP
This repository is for the semantic-annotation working group/hackathon that took place during the MADICES 2 2024 Workshop. 

The group worked on two main tasks
1. Unit work: To gather information about semantic unit implementations and find some example documents and create package on PyPi
2. Semantic Annotation of datasets

This contains the following files/folders
- Test_Data - this contains the test data files that we used for the semantic annotation work. These are snippets taken from the Schumann-Clean_oxidation.zip dataset on https://zenodo.org/records/10990048.
- PythonConvertor - this contains a basic python script to convert between the JSON and JSON-LD to demonstrate in the first instance how simple/complex this transformation would be
- Mappings - this contains a very crude description of the mappings used to turn the JSON files in Test_Data to JSON-LD, noting which ontology terms were used to represent the different data fields
- scripts folder & top level python files - these were to create some of the test datasets that sit in Test_Data 
- ontopint_demo.ipynb - this is the Jupyter Notebook to demo the unit work
