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
    scanId = request.args.get("scanId", type = int)
    ipId = request.args.get("ipId", type = int)

    scans = Scan.query.order_by(Scan.id.desc()).all()

    ips = []
    if scanId:
        ips = scan.getIps(scanId)
    
    resultats = []
    if scanId and ipId:
        results = scan.getIpAndResults(scanId, ipId)
        resultats = results

    return render_template("index.html", 
                           scans = scans,
                           ips = ips,
                           resultats = resultats,
                           selectedScanId=scanId,
                           selectedIpId=ipId)

@app.route("/<int:scanId>")
def redirectionScan(scanId):
    print("Appel de redirectionScan avec scanId = ", scanId)
    return redirect(url_for("home", scanId = scanId))

@app.route("/<int:scanId>/<int:ipId>")
def redirectionScanIpResultat(scanId, ipId):
    print("Appel de redirectionScanIpResultat avec scanId = ", scanId, " et ipId = ", ipId)
    return redirect(url_for("home", scanId = scanId, ipId = ipId))


@app.route("/upload", methods=["POST"])
def upload():
    files = request.files.getlist('file')

    scan.saveUploadFile(files)
    lastScan = Scan.query.order_by(Scan.id.desc()).first()
    return redirect(url_for("redirectionScan", scanId = lastScan.id))

