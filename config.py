import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).parent.resolve()
CHALICE_CONFIG = "example/.chalice/config.json"
INFRA = ROOT.joinpath("infra")

# TODO move all scripts into this file and create parser for flags
# TODO refactor this script for production


tf_output = json.loads(
    subprocess.run(
        ["terraform", "output", "-json"],
        check=True,
        cwd=INFRA,
        capture_output=True,
    ).stdout
)
print(tf_output)

# https://aws.github.io/chalice/topics/configfile.html
config = json.loads(ROOT.joinpath(CHALICE_CONFIG).read_text())

env = {}
for key in tf_output.keys():
    env.update({key.upper(): tf_output[key]["value"]})

config["stages"]["dev"]["environment_variables"].update(env)

tags = {}
config["stages"]["dev"]["tags"].update(tags)


with open(ROOT.joinpath(CHALICE_CONFIG), "w") as f:
    json.dump(config, f, indent=4)
