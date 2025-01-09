variable "project_id" {
  description = "The ID of the GCP project"
  type        = string
}

variable "region" {
  description = "The region to deploy resources"
  type        = string
}

variable "repository_id" {
  description = "The Artifact Registry repository ID"
  type        = string
}

variable "image_tag" {
  description = "Tag for the Docker image in Artifact Registry"
  type        = string
}
