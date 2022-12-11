terraform {
  required_version = "1.1.9"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 2, < 5"
    }
    # random = {
    #   source = "hashicorp/random"
    #   version = "3.4.3"
    # }
  }
}
