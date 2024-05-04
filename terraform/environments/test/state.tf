terraform {
  backend "s3" {
    bucket  = "jsc-test-state-s3"
    encrypt = true
    key     = "test/terraform/.tfstate"
    region  = "us-east-1"
  }
}