variable "region" {
  description = "The region in which the Cloud Run service should be deployed"
  type        = string
}

variable "image" {
  description = "The container image to deploy to Cloud Run"
  type        = string

}

variable "service_name" {
  description = "The name of the Cloud Run service"
  type        = string
}