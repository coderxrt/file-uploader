from flask import Flask,jsonify,request, render_template, url_for
import os
app = Flask(__name__)
app.config["USER_FILES"] = "sdcard/FileCollector/static/uploads"
if not os.path.exists(app.config["USER_FILES"]):
  os.makedirs(app.config["USER_FILES"], exist_ok=True)

@app.route("/upload", methods=["POST","GET"])
def upload():
  files = request.files.getlist("files")
  if not files:
    return render_template("home.html",error="No files found for processing...")
  for file in files:
    if file.filename == "" or not file:
      return render_template("home.html",error="Could not validate a correct File type.")
    try:
      file.save(os.path.join(app.config["USER_FILES"], file.filename))
    except Exception as e:
       return render_template("home.html",error=f"Error {error}")
  return render_template("home.html",status="Your File(s) has been uploaded successfully to our server. Please contact Dukee the programmer for more info.....")
       
@app.route("/", methods=["POST", "GET"])
def home():
  return render_template("home.html")
       
if __name__ == "__main__":
    app.run(debug=True)