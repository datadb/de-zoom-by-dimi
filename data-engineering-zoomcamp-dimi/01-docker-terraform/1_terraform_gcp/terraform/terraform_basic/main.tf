terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
# Credentials only needs to be set if you do not have the GOOGLE_APPLICATION_CREDENTIALS set
#  credentials = "/workspaces/de-zoom-by-dimi/data-engineering-zoomcamp-dimi/01-docker-terraform/terrademo/keys/my-creds.json"
  project = "mydezoomcamp2024"
  region  = "europe-west1"
}

resource "google_storage_bucket" "mydezoomcamp2024demobucket" {
  name          = "my-dezoomcamp-2024-terra-bucket-by-dimidb"
  location      = "EU"
  # Optional, but recommended settings:
  storage_class = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled     = true
  }

  lifecycle_rule {
    action {
      type = "AbortIncompleteMultipartUpload"
    }
    condition {
      age = 1 // days
    }
  }

  force_destroy = true
}

/*

resource "google_bigquery_dataset" "dataset" {
  dataset_id = "<The Dataset Name You Want to Use>"
  project    = "<Your Project ID>"
  location   = "US"
}

*/