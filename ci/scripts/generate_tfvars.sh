#!/bin/bash

set -eu

USAGE="USAGE:

This script creates variables.tfvars for an environment in 
~./environments

${0} <environnment-name> <image-tag>"

if [[ $# -ne 2 ]]; then
    echo "${USAGE}" >&2
    exit 1
fi

## Set vars
SCRIPT_DIR=$( cd $( dirname "${BASH_SOURCE[0]}" ); pwd -P )
pushd ${SCRIPT_DIR} > /dev/null
# Get absolute path to config directory
CONFIG_DIR=$(cd "${SCRIPT_DIR}/../configs"; pwd -P)
# Get absolute path to environment directory
ENV_DIR=$(cd "../../terraform/environments/${1}"; pwd -P)
ENVIRONMENT=$(basename $(cd ${ENV_DIR}; pwd -P))
IMAGE_TAG=$2

###  Functions 
function copy_tfvars(){
    pushd ${CONFIG_DIR} > /dev/null
    [ -f variables.tfvars ] && mv variables.tfvars $ENV_DIR
    popd
}
function replace_vars(){
    pushd ${CONFIG_DIR} > /dev/null
    # update vars
    sed -e "s|ENVIRONMENT|$ENVIRONMENT|g" -e "s|REGION|us-east-1|g" -e "s|IMAGE_TAG|$IMAGE_TAG|g" "variables.tfvars.tpl" > variables.tfvars
    popd
}

# 
replace_vars
copy_tfvars