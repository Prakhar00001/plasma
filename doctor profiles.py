import spacy

nlp = spacy.load('en_core_web_sm')

def analyze_profile(profile):
  doc = nlp(profile)
  entities = [(X.text, X.label_) for X in doc.ents]
  return entities

profile = "Dr. Anil Saini  is a general practitioner with 10 years of experience"
entities = analyze_profile(profile)
print(entities)