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
