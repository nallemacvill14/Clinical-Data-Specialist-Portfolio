# Simple Python script for Clinical Keyword Extraction
# Objective: Categorize patient notes for targeted documentation review.

patient_notes = [
    "Patient presents with symptoms of clinical depression and anxiety.",
    "Hypertension noted during routine checkup, BP 140/90.",
    "Acute episode of panic disorder during clinical interview."
]

def categorize_clinical_notes(notes):
    categories = {"Mental Health": [], "Cardiovascular": []}
    
    for note in notes:
        if "depression" in note.lower() or "panic" in note.lower():
            categories["Mental Health"].append(note)
        elif "hypertension" in note.lower() or "bp" in note.lower():
            categories["Cardiovascular"].append(note)
            
    return categories

# Output for Data Structuring
structured_data = categorize_clinical_notes(patient_notes)
print(structured_data)
