variable "env" {
  description = "Project Environment"
  type        = string
  default     = "dev"
}
variable "project_name" {
  description = "Project Name"
  type        = string
  default     = "UBet Infrastructure"
}

variable "lambda_name" {
  description = "lambda function name"
  type = string
}
variable "lambda_description" {
  description = "lambda function description"
  type = string
}

variable "lambda_image_uri" {}