# Deploy Containerized Website

## Overview

Welcome, DevOps engineers! This challenge evaluates your proficiency in **Infrastructure as Code (IaC)**, **cloud platforms**, and **Docker**. Your primary task is to deploy a containerized static website using the provided HTML file. You'll achieve this by creating a **Dockerfile** and leveraging an IaC tool of your choice (such as **Terraform**, **AWS CloudFormation**, **CDK**, or **Pulumi**) to provision the necessary cloud resources. The ultimate goal is to make your deployed website **publicly accessible**.

We've provided a simple [`helloworld.html`](helloworld.html) file, which you'll use as the content for your static website.

---

## Requirements

Here's a detailed breakdown of what's expected:

1.  **Static Website:**

    - Use the provided [`helloworld.html`](helloworld.html) file as the website.
    - Make this static content accessible on a publicly accessible web server.

2.  **Containerization:**

    - **Build and Serve:** Containerize the static website so that it can be built into a Docker image and served from within the container.
    - **Lightweight Base Image:** Choose a lightweight base image for your Dockerfile to optimize image size and performance. Configure it to serve our static website. Popular choices include `nginx` (web server) or `alpine` (for a minimal Linux distribution).
    - Develop a robust and efficient `Dockerfile` that automates the process of building your containerized website. This file should include all necessary instructions to prepare the environment and serve the [`helloworld.html`](helloworld.html) file.

3.  **Infrastructure as Code (IaC):**

    - **Resource Provisioning:** Utilize an IaC tool of your choice (e.g., **Terraform**, **AWS CloudFormation**, **CDK**, or **Pulumi**) to provision all the cloud resources required to host your containerized website. This includes, but is not limited to, compute instances (e.g., EC2, ECS Fargate), networking components, and any load balancing or security groups needed.
    - **Cloud Platform Choice:** You may choose any major cloud platform (e.g., AWS, Azure, GCP) to deploy your solution.
    - **Public Accessibility:** Ensure that the deployed website is publicly accessible via a URL.

4.  **Logging:**
    - **Enable Logging:** Configure appropriate logging for your deployed container. This could involve directing container logs to a centralized logging service (e.g., AWS CloudWatch Logs, Azure Monitor, Google Cloud Logging) to facilitate troubleshooting and monitoring.

---

## Deliverables

Upon completion, your submission should include the following:

1.  **`README.md` File:**

    - **Setup Instructions:** Provide clear, step-by-step instructions on how to set up the environment (e.g., configuring cloud provider credentials, installing necessary CLIs, running `terraform init` or equivalent IaC commands).
    - **Deployment Steps:** Detail the commands and procedures required to deploy your solution from scratch.
    - **Testing the Live Website:** Explain how to verify that the website is live and accessible, including the URL to access it.

2.  **Source Code Repository:**
    - **`Dockerfile`:** Your complete and functional Dockerfile.
    - **IaC Templates:** All your IaC templates (e.g., `.tf` files for Terraform, `.yaml` or `.json` for CloudFormation, source code for CDK/Pulumi) used to provision the infrastructure.

---

## Preparing for the Interview

**[Next Steps...](../../next-steps-real-time.md)**
