from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

class Scan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)

class Ip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15), nullable=False)
    ip_status = db.Column(db.String(20), nullable=False)

    scan_id = db.Column(db.Integer, db.ForeignKey('scan.id'), nullable=False)

class Resultat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(50), nullable=False)
    port = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    scan_id = db.Column(db.Integer, db.ForeignKey('scan.id'), nullable=False)
    ip_id = db.Column(db.Integer, db.ForeignKey('ip.id'), nullable=False)


