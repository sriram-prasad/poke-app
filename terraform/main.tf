terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.14"
    }
  }

  backend "gcs" {
    bucket = "rng-poke-app-terraform-state"
    prefix = "terraform/state"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# Artifact Registry Module
module "artifact_registry" {
  source        = "./modules/artifact_registry"
  region        = var.region
  repository_id = var.repository_id
}

# Cloud Run Module
module "cloud_run" {
  source = "./modules/cloud_run"
  region = var.region
  image  = "australia-southeast2-docker.pkg.dev/${var.project_id}/${var.repository_id}/poke-app:${var.image_tag}"
}
