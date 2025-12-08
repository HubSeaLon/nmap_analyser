from models import db, Scan, Resultat, Ip
import re

def saveUploadFile(files):
    uploaded_files = []
    
    for file in files:
        filename = file.filename
        pathFile = f"uploads/{filename}"
        file.save(pathFile)
        
        # Enregistrement en BDD
        scan = Scan(filename=filename)
        db.session.add(scan)
        db.session.commit()

        uploaded_files.append(filename)
        
        analyzeFile(pathFile, scan.id) 

    return uploaded_files

def analyzeFile(pathFile, scanId):
    analysis_results = []
    
    with open(pathFile, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    currentIp = None
    hostUp = False

    for line in lines:
         
        line = line.strip() # Supprimer les espaces inutiles

        if "Nmap scan report for" in line:
            match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
            if match:
                currentIp = match.group(1)
                hostUp = False # Reset statut nouvelle IP
            continue
            
        if currentIp and "Host is up" in line:
            hostUp = True
            ipStatus = "EN LIGNE"
            print("Host up:", currentIp)

            ip = Ip(ip = currentIp,
                    ip_status = ipStatus,
                    scan_id = scanId
                    )

            db.session.add(ip)
            db.session.commit()

            continue 
        
        if currentIp and hostUp:
            port_match = re.search(r'(\d+)/([a-zA-Z0-9]+)\s+(\w+)\s+([\w\-\_\.]+)', line)

            if port_match:
                port = port_match.group(1)
                protocol = port_match.group(2)
                status = port_match.group(3)
                service = port_match.group(4)

                resultat = Resultat(
                    service = service,
                    port = f"{port}/{protocol}",
                    status = status, 
                
                    scan_id = scanId,
                    ip_id = ip.id
                )
                
                db.session.add(resultat)
                db.session.commit()
                
                analysis_results.append({
                    "ip": currentIp,
                    "ip_status": ipStatus,
                    "service": service,
                    "port": f"{port}/{protocol}",
                    "status": status,
                    "scan_id": scanId
                })

    print("Analysis Results:", analysis_results)

               

        