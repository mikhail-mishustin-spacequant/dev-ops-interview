# Main Terraform configuration file
# This is a starter template - implement your cloud provider of choice

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
  
  # Uncomment to use a backend for state storage
  # backend "s3" {
  #   bucket = "terraform-state-bucket"
  #   key    = "devops-interview/terraform.tfstate"
  #   region = "us-west-2"
  # }
}

provider "aws" {
  region = var.region
  
  # Ensure resources are tagged properly
  default_tags {
    tags = var.default_tags
  }
}

# Define a module for VPC
module "vpc" {
  source = "./modules/vpc"
  
  vpc_name       = "${var.prefix}-vpc"
  vpc_cidr       = var.vpc_cidr
  azs            = var.availability_zones
  private_subnets = var.private_subnets
  public_subnets  = var.public_subnets
}

# Define a module for EKS (Kubernetes)
module "eks" {
  source = "./modules/eks"
  
  cluster_name    = "${var.prefix}-cluster"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnet_ids
  instance_types  = var.eks_instance_types
  desired_capacity = var.eks_desired_capacity
  min_size        = var.eks_min_size
  max_size        = var.eks_max_size
}

# Define a module for ECR (Container Registry)
module "ecr" {
  source = "./modules/ecr"
  
  repository_name = "${var.prefix}-repo"
  image_tag_mutability = "IMMUTABLE"  # Best practice for immutable infrastructure
}

# Output important information
output "eks_cluster_endpoint" {
  value = module.eks.cluster_endpoint
}

output "ecr_repository_url" {
  value = module.ecr.repository_url
}
