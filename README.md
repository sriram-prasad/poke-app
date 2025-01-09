# RNG Poke App

## Overview
[RNG Poke App](https://poke-service-528760684336.australia-southeast2.run.app) is a web application designed to enhance the experience of generating and managing Pokémon data. The app stores Pokémon data in a PostgreSQL database, reducing the need for repeated API calls and improving performance. It also tracks analytics, such as the number of times a Pokémon has been generated, enabling insightful data-driven decisions.

## Features
- **Pokémon Generation**: Dynamically generate random Pokémon and store the data.
- **Cloud Native**: Runs on Google Cloud Platform (GCP) services for scalability and reliability.
- **Dockerized Deployment**: Ensures portability and consistency across environments.
- **TODO: Analytics**: Track generation counts for each Pokémon.

## Architecture
This project uses the following components:

1. **Google Cloud Platform (GCP):**
   - Cloud Run: For hosting the Dockerized Flask web app.
   - Artifact Registry: To store container images.

2. **Infrastructure as Code (IaC):**
   - Terraform: Manages infrastructure provisioning with a modular approach.

3. **Continuous Integration and Deployment (CI/CD):**
   - GitHub Actions: Automates the build, test, and deployment pipelines.

## Project Structure
```
.
├── Dockerfile
├── README.md
├── app
│   ├── app.py
│   ├── services.py
│   ├── templates
│   │   └── index.html
│   └── tests
│       └── app_tests.py
├── requirements.txt
└── terraform
    ├── main.tf
    ├── modules
    │   ├── artifact_registry
    │   │   ├── main.tf
    │   │   ├── outputs.tf
    │   │   └── variables.tf
    │   └── cloud_run
    │       ├── main.tf
    │       ├── outputs.tf
    │       └── variables.tf
    ├── terraform.tfvars
    ├── tf-credentials.json
    └── variables.tf
```

## Usage
- Access the web app through the deployed [Cloud Run URL](https://poke-service-528760684336.australia-southeast2.run.app).
- View Pokémon generation data and analytics directly in the app.

## Future Enhancements
- Build and integrate the Cloud SQL PostgreSQL component.
- Map Cloud Run URL to a proper domain.
- Implement analytics dashboards.
- Optimise database queries for better performance.
- Add support for additional Pokémon API features.

