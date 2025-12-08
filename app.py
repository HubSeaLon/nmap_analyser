from flask import Flask, render_template, request, redirect, url_for # type: ignore
from bdd_config import Config
from models import db, Resultat, Scan, Ip
from services import scan

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

@app.route("/")
def home():
    scans = Scan.query.order_by(Scan.id.desc()).all()

    #resultats = Resultat.query.all()
    ips = Ip.query.all()

    return render_template("index.html", 
                           scans = scans,
                           ips = ips
                           )


@app.route("/upload", methods=["POST"])
def upload():
    files = request.files.getlist('file')

    scan.saveUploadFile(files)

    return redirect(url_for("home"))


@app.route("/results/<int:scanId>")
def results(scanId):
    scans = Scan.query.order_by(Scan.id.asc()).all()

    message = request.args.get("message")

    return render_template("index.html", 
                            scans = scans, 
                            scanId = scanId, 
                            message = message)

