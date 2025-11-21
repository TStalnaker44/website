
import csv, os, json

## Publication Page

PUB_PAGE = """
<html>
  <head>
    <title>Publications</title>
    <include src="shared.html"/>
    <link rel="stylesheet" href="css/pubs.css">
  </head>
  <body>

    <include src="navbar.html"/>
    <div class="section-container">
      <h1>Publications</h1>
    </div>

    <p style="text-align: center;">Find all my publications on my 
    <a href="https://scholar.google.com/citations?user=f_ZZDNYAAAAJ" target="_blank">Google Scholar page</a>.</p>

    %s

  </body>
</html>
"""

## HTML Templates
TITLE    = "<h3>%s</h3>"
AUTHORS  = "<div><i class=\"fa fa-user\"></i> %s</div>"
VENUE    = "<div><i class=\"fa fa-book\"></i> %s (<a href=\"%s\">%s</a>)</div>"
INFO     = "<div><i class=\"fa fa-info-circle\"></i> %s, <strong>%s</strong> - [<a href=\"%s\" target=\"_blank\">pdf</a>]</div>"      
AWARD    = "<div><i class=\"fa fa-trophy\"></i> %s</div>"
ABSTRACT = "<details><summary>Show Abstract</summary><div class=\"abstract\">%s</div></details>"      
      
def generatePublicationHTML():
    html = loadPublicationsJSON()
    return PUB_PAGE % html

def loadPublicationsJSON():
    pub_file = os.path.join("data", "publications.json")
    with open(pub_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    html = ""
    for entry in data[::-1]:
        html += assemblePublicationJSON(entry)
    return html
        

def assemblePublicationJSON(data):
    entry = "<div class=\"section-container\">"
    entry += TITLE % data["title"]
    entry += AUTHORS % formatAuthors(data["authors"])
    entry += VENUE % (data["venue"]["name"], data["venue"]["link"], data["venue"]["abbr"])
    entry += INFO % (data["info"]["pages"], data["info"]["year"], data["pdf_link"])
    if data.get("award", ""):
        entry += AWARD % data["award"]
    entry += ABSTRACT % data["abstract"]
    entry += "</div>"
    return entry

def formatAuthors(authors):
    ret = ""
    for i, author in enumerate(authors):
        name = author["first"] + " " + author["last"]
        if name == "Trevor Stalnaker":
            name = f"<strong>{name}</strong>"
        ret += name
        if i == len(authors) - 2:
            ret += ", and "
        elif i < len(authors)-1:
            ret += ", "
    return ret
      