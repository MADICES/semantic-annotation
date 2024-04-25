#A very crude first attempt to automate converting the json to json-ld
#This has taken the exerp and matched the json fields with the equivalent ontology terms 
#Much more work would need to be done to understand the variation on the documents and their range of fields and field values

from pyld import jsonld
import json

with open('initialfile.json') as input_file:
   json_file = json.load(input_file)
   json_archive = json_file['archive']
   json_data = json_archive['data']
   json_reaction_results = json_data['reaction_results']
   json_reactants_conversions = json_reaction_results['reactants_conversions']
   json_reactor_filling = json_data['reactor_filling']
   json_samples = json_data['samples']

   #NB: This would need to be given or taken from the higher level files
   description = "This is an exerp from one of the measurement entry datasets from the publication: Data-Centric Heterogeneous Catalysis: Identifying Rules and Materials Genes of Alkane Selective Oxidation https://pubs.acs.org/doi/full/10.1021/jacs.2c11117"
   foaf_name = json_data['experimenter'].split(".")

   samples_array = []
   for sample_data in json_samples:
      samples_array.append(sample_data)

   sample_title = "sample " + sample_data['name'] + " dataset"
   sample_desription = "This is the dataset for the catalyst sample "+ sample_data['name']

   reactants_array = []
   for reagent in json_reactants_conversions:
      reactants_array.append(reagent['name'])

   filename = json_data['data_file']
   filename_array = filename.split('.')
   filename_ext = filename_array[1]
   filename_media_type = ""

   if filename_ext == 'xlsx' or filename_ext == 'xls':
      filename_media_type = "https://www.iana.org/assignments/media-types/application/vnd.ms-excel"
   elif filename_ext == "json":
      filename_media_type = "https://www.iana.org/assignments/media-types/application/json"
   elif filename_ext == "pdf":
       filename_media_type = "https://www.iana.org/assignments/media-types/application/pdf"
   elif filename_ext == "csv":
      filename_media_type = "https://www.iana.org/assignments/media-types/text/csv"
   else:
      filename_media_type = "https://www.iana.org/assignments/media-types/text"

   #would need to understand more about the range of reaction types and either build a dictionary or do a search on the voc4cat terms to match with the correct one
   reaction_type = "voc4cat:" + json_data['reaction_class']

context = {
   "dcterms": "https://www.dublincore.org/specifications/dublin-core/dcmi-terms/",
   "dcat": "https://www.w3.org/TR/vocab-dcat-3",
   "foaf": "http://xmlns.com/foaf/spec", 
   "voc4cat": "https://w3id.org/nfdi4cat/voc4cat_",
   "sio": "http://semanticscience.org/ontology/sio",
   "om:": "http://www.ontology-of-units-of-measure.org/resource/om-2"
}

doc = {
   "dcat:dataset": {
      "dct:title": json_data['name'],
      #need to figure out how to match this 
      "dct:description": description,
      "dct:date": json_data['datetime'],
      "dct:format": filename_media_type,
      "dct:location": json_data['location'],
      "dcat:theme_taxonomy": json_data['m_def'],
      "dct:creator": {
      "foaf:agent": {
           "foaf:first_name": foaf_name[0].strip(),
           "foaf:last_name": foaf_name[1].strip(),
         }
     },
     "voc4cat:chemical_conversion": {
         "voc4cat:reaction_name": json_data['reaction_name'],
         "voc4cat:reaction_type": reaction_type, 
         "voc4cat:reactor_feed": [
            reactants_array
         ]
      },
      "sio:sample": {
         "om:value" : {
            "om:measurement" : {
               "om:numerical_value" : str(json_reactor_filling['catalyst_mass']),
               "om:unit" : "om:milligram" #will this always be the case 
            }
         },
         "dcat:dataset" : {
            "dct:title" :  sample_title,
            "dct:description" : sample_desription,
            "dct:identifier" : sample_data['name'],
            "dcat:access_url" : sample_data['reference'],
            "dcat:themeTaxonomy": sample_data['m_def']
        }
      }
   }
}

# compact a document according to a particular context
# see: https://json-ld.org/spec/latest/json-ld/#compacted-document-form
compacted = jsonld.compact(doc, context)

print(json.dumps(compacted, indent=2))

