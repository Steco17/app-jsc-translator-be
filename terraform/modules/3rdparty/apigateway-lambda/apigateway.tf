module "api_gateway" {
  source = "terraform-aws-modules/apigateway-v2/aws"

  version = "4.0.0"
  name          = "${var.name}-apigw"
  description   = var.description
  protocol_type = "HTTP"

  cors_configuration = {
    allow_headers = ["content-type", "x-amz-date", "authorization", "x-api-key", "x-amz-security-token", "x-amz-user-agent"]
    allow_methods = ["*"]
    allow_origins = ["*"]
  }
  
  # Custom domain
  domain_name                 = "" 
  domain_name_certificate_arn = ""
  create_api_domain_name = true

  # Routes and integrations
  integrations = {
    "$default" = {
      lambda_arn = var.lambda_arn
      timeout_milliseconds   = 12000
    }
  }

  tags = {
    Name = "http-${var.name}-apigw"
  }
}