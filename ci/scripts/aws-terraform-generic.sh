#!/bin/bash

set -eu

# need to pass in environments & aws account
USAGE="USAGE:
${0} <terraform-multienv-root> <terraform-command[plan|apply]> <environment> <workspace>"

if [[ $# < 4 ]]; then
    echo "${USAGE}" >&2
    exit 1
fi

TERRAFORM_DIRECTORY=$1
TERRAFORM_CMD=$2
ENV_NAME=$3
WORKSPACE=$4

# Get absolute path of terraform environment
ENV_DIR="$(cd "${TERRAFORM_DIRECTORY}/environments/${ENV_NAME}"; pwd -P)"
pushd ${ENV_DIR} > /dev/null

# remove previous credentials
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN
# aws configure
export AWS_PROFILE=$ENV_NAME

#  terraform init
terraform init
terraform validate
terraform workspace list
terraform workspace select $WORKSPACE

terraform ${TERRAFORM_CMD} -var-file=./variables.tfvars -auto-approve

echo "done setting up ${ENV_NAME}/${WORKSPACE}!"
popd
