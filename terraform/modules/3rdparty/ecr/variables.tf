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

variable "lambda_ecr" {
  description = "Lambda Container Registry"
  type        = string
}
