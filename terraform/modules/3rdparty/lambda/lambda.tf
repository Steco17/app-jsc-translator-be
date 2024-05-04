module "lambda" {

    source  = "cloudposse/lambda-function/aws"
    version = "0.5.3"
 
    function_name = var.lambda_name
    description   = var.lambda_description

    image_uri    = "${var.lambda_image_uri}"
    package_type = "Image"
    publish = true

    timeout = 360
    memory_size = 1536

}
