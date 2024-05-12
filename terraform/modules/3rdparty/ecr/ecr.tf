# dapp
module "lambda_ecr" {
    
  source = "cloudposse/ecr/aws"
  version     = "0.41.0"
  namespace              = var.project_name
  stage                  = var.env
  name                   = var.lambda_ecr
  image_tag_mutability  = "IMMUTABLE" 
  scan_images_on_push    = true
  use_fullname           = false
  regex_replace_chars	   = "/[^a-zA-Z0-9-/-_]/"
  
}
