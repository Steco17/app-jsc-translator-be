
output "lambda_image_uri" {
 description = "image uri for repository"
 value       = module.lambda_ecr.repository_url
}