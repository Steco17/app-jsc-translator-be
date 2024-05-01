
variable "region" {
  description = "Region for the subnetwork"
  type        = string
  validation {
    condition     = length(var.region) > 0
    error_message = "Region cannot be empty!"
  }

  validation {
    condition = contains([
      "us-east1", "us-east4", "us-west1", "us-west2", "us-west3", "us-west4", "us-central1",
      "northamerica-northeast1", "southamerica-east1", "europe-west1", "europe-west2", "europe-west3",
      "europe-west4", "europe-west6", "asia-east1", "asia-east2", "asia-northeast1", "asia-northeast2",
      "asia-northeast3", "asia-southeast1", "asia-southeast2", "australia-southeast1"
    ], var.region)
    error_message = "Use an approved region!"
  }
}

variable "company" {
  description = "The company name to add to naming convention."
  type        = string
    validation {
    condition     = length(var.company) > 0
    error_message = "company must not be an empty string"
  }
}

variable "environment" {
  description = "work environment (matches /terraform/environments/{ENV} ) - e.g. sandbox | dev | uat |  prod"
  type        = string
    validation {
    condition     = length(var.environment) > 0
    error_message = "environment cannot be empty!"
  }
}

variable "log_retention" {
  description = "Log retention of access logs of state bucket."
  default     = 90
  type        = number
    validation {
    condition     = var.log_retention > 0
    error_message = "log_retention needs to be greater than 0!"
  }
}

variable "log_bucket_purpose" {
  description = "Name to identify the bucket's purpose"
  default     = "logging"
  type        = string
    validation {
    condition     = length(var.log_bucket_purpose) > 0
    error_message = "log_bucket_purpose cannot be empty!"
  }
}

variable "state_bucket_purpose" {
  description = "Name to identify the bucket's purpose"
  default     = "terraform-state"
  type        = string
    validation {
    condition     = length(var.state_bucket_purpose) > 0
    error_message = "state_bucket_purpose cannot be empty!"
  }
}

variable "log_bucket_versioning" {
  description = "A string that indicates the versioning status for the log bucket."
  default     = "Disabled"
  type        = string
  validation {
    condition     = contains(["Enabled", "Disabled", "Suspended"], var.log_bucket_versioning)
    error_message = "Valid values for versioning_status are Enabled, Disabled, or Suspended."
  }
}

variable "state_bucket_tags" {
  type        = map(string)
  default     = { Automation : "Terraform" }
  description = "Tags to associate with the bucket storing the Terraform state files"
}

variable "log_bucket_tags" {
  type        = map(string)
  default     = { Automation : "Terraform", Logs : "Terraform" }
  description = "Tags to associate with the bucket storing the Terraform state bucket logs"
}

variable "terraform_user" {
  description = "The username for the infrastructure provisioning user."
  type        = string
  default     = "terraform-user"
    validation {
    condition     = length(var.terraform_user) > 0
    error_message = "terraform_user name cannot be empty!"
  }
}

variable "terraform_user_permissions" {
  description = "The permissions for the infrastructure provisioning."
  type        = list(string)
  default     = ["s3:CreateBucket"]
}
