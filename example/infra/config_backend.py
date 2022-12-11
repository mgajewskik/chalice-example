import json
import pathlib

INFRA = pathlib.Path(__file__).parent.resolve()
TF_FILE_NAME = "chalice.tf.json"

BACKEND_REGION = "us-west-2"
BACKEND_BUCKET = "chalice-tf-state"
BACKEND_KEY = "chalice.tfstate"

# TODO move this into main config.py file

terraform = json.loads(INFRA.joinpath(TF_FILE_NAME).read_text())
backend = {
    "backend": {
        "s3": {"region": BACKEND_REGION, "bucket": BACKEND_BUCKET, "key": BACKEND_KEY}
    }
}
terraform["terraform"].update(backend)

with open(INFRA.joinpath(TF_FILE_NAME), "w") as f:
    json.dump(terraform, f, indent=2)
