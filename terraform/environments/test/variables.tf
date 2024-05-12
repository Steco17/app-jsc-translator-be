variable "env_name" {
  type        = string
  description = "Environment name"
  validation {
    condition     = length(var.env_name) > 0
    error_message = "env_name must not be an empty string"
  }
}

variable "region" {
  description = "Region"
  type        = string
  validation {
    condition     = length(var.region) > 0
    error_message = "Region cannot be empty!"
  }

  validation {
    condition = contains([
      "us-east-1", "us-east-4", "us-west-1", "us-west-2", "us-west-3", "us-west-4", "us-central1",
      "northamerica-northeast-1", "southamerica-east-1", "europe-west-1", "europe-west-2", "europe-west-3",
      "europe-west-4", "europe-west-6", "asia-east-1", "asia-east-2", "asia-northeast-1", "asia-northeast-2",
      "asia-northeast-3", "asia-southeast-1", "asia-southeast-2", "australia-southeast-1"
    ], var.region)
    error_message = "Use an approved region!"
  }
}
variable "image_tag" {
  type        = string
  description = "Translate Lambda Image Tag"
  validation {
    condition     = length(var.image_tag) > 0
    error_message = "image_tag must not be an empty string"
  }
}