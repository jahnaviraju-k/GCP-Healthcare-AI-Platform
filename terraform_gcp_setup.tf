resource "google_storage_bucket" "data_bucket" {
  name     = "healthcare-data-bucket"
  location = "US"
}

resource "google_bigquery_dataset" "healthcare_dataset" {
  dataset_id = "healthcare_dataset"
  location   = "US"
}

resource "google_artifact_registry_repository" "docker_repo" {
  location     = "us-central1"
  repository_id = "healthcare-ai-docker"
  format       = "DOCKER"
}
