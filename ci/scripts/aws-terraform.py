import json
import subprocess
import argparse

parser = argparse.ArgumentParser(
    description="Run terraform command across environments",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument("--command", type=str, required=True, help="plan | apply")
parser.add_argument(
    "--config",
    type=str,
    required=True,
    help="file path to pipeline configuration",
)
args = parser.parse_args()
config_args = vars(args)

config = json.load(open(config_args["config"]))

for service, service_vars in config["environments"].items():
    for workspace in config["environments"][service]["workspaces"]:
        # generate tfvars ?
        # terraform run
        subprocess.check_call(
            [
                "bash",
                "ci/scripts/aws-terraform-generic.sh",
                config["terraform_directory"],
                config_args["command"],  # command
                service,
                workspace,  # workspace
            ]
        )
