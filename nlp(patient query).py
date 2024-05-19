import spacy

nlp = spacy.load('en_core_web_sm')

def analyze_query(query):
  doc = nlp(query)
  entities = [(X.text, X.label_) for X in doc.ents]
  return entities

query = "I have a headache and I want to see a doctor tomorrow"
entities = analyze_query(query)
print(entities)