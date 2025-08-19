import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json

class CleanPatientData(beam.DoFn):
    def process(self, element):
        record = json.loads(element)
        if record.get("age") and record.get("patient_id"):
            yield {
                "patient_id": record["patient_id"],
                "age": int(record["age"]),
                "gender": record["gender"],
                "diabetes": int(record.get("diabetes", 0)),
                "hypertension": int(record.get("hypertension", 0))
            }

options = PipelineOptions(
    project="your-gcp-project",
    region="us-central1",
    temp_location="gs://your-bucket/tmp",
    runner="DataflowRunner"
)

with beam.Pipeline(options=options) as p:
    (p
     | "Read from GCS" >> beam.io.ReadFromText("gs://your-bucket/raw/patients.json")
     | "Clean Data" >> beam.ParDo(CleanPatientData())
     | "Write to BigQuery" >> beam.io.WriteToBigQuery(
            "your_project.healthcare_dataset.patients",
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
        ))
