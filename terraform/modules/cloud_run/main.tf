resource "google_cloud_run_v2_service" "rng-poke-service" {
  name                = "poke-service"
  location            = var.region
  deletion_protection = false
  ingress             = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      image = var.image
    }
  }
}

resource "google_cloud_run_service_iam_member" "allUsers" {
  service  = var.service_name
  location = var.region
  role     = "roles/run.invoker"
  member   = "allUsers"
}