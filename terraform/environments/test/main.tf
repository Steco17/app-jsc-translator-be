
module "translate-ecr" {
  
    source = "../../modules/3rdparty/ecr"

    lambda_ecr = "translate"
}

module "translate-lambda" {
    source = "../../modules/3rdparty/lambda"

    lambda_name = "translate-${var.env_name}"
    lambda_image_uri = module.translate-ecr.lambda_image_uri
    lambda_description = "Translate API"

    env = var.env_name

    depends_on = [ module.translate-ecr ]
}

# module "translate-apigw" {
#     source = "../../modules/3rdparty/apigateway-lambda"

#     name = "translave-${var.env_name}"
#     lambda_arn = module.translate-lambda.lambda_arn
#     description = "API gateway to server backend (lambda) routes"

#     depends_on = [ module.translate-lambda ]

# }