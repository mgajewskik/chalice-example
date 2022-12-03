from chalice.app import Chalice

app = Chalice(app_name="example")


@app.route("/")
def index():
    return {"app": "example"}
