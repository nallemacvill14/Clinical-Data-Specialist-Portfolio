# PHI De-identification Protocol (HIPAA Safe Harbor Method)

To maintain data privacy in Clinical AI training, I apply the *Safe Harbor Method* to remove all 18 identifiers from electronic Protected Health Information (e-PHI).

### Steps for Data Sanitization:
1. *[span_6](start_span)Direct Identifiers Removal:* Stripping Names, Social Security Numbers, and Medical Record Numbers (MRNs).[span_6](end_span)
2. *[span_7](start_span)Geographic Redaction:* Removing all geographic subdivisions smaller than a State (City, Zip Codes).[span_7](end_span)
3. *[span_8](start_span)Temporal Shifting:* Redacting all dates (except year) directly related to an individual (Birth date, Admission date).[span_8](end_span)
4. *[span_9](start_span)Contact Info Purge:* Deleting Phone numbers, Fax numbers, and Email addresses.[span_9](end_span)

[span_10](start_span)[span_11](start_span)This protocol ensures that clinical datasets are compliant for secondary research and machine learning purposes.[span_10](end_span)[span_11](end_span)
