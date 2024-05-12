output "lambda_name" {
  description = "lambda name"
  value       = module.lambda.function_name
}

output "lambda_arn" {
  description = "lambda arn"
  value       = module.lambda.arn
}

