terraform {
  backend "local" {
    path = "./dev/.tfstate"
  }
}
