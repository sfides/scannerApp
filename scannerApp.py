import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    photo = request.files.get("photo")

    if not photo or photo.filename == "":
        # No file selected
        return "No photo uploaded. Please go back and choose a file."


    filename = secure_filename(photo.filename)


    save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)


    photo.save(save_path)


    return f"Photo saved as: {save_path}"

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0")
