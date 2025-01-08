resource "google_artifact_registry_repository" "container_repo" {
  location      = var.region
  repository_id = var.repository_id
  description   = "Container repository for storing Docker images"
  format        = "DOCKER"
}