
import re, os
import utility_scripts.compile_publications

files = ["index", "publications", "resume", "progress", "about", "contact", "projects", "resources"]

def main():
    for file in files:
        compileFile(f"{file}.html")

def getContent(file_name):
    if file_name == "publications.html":
        return utility_scripts.compile_publications.generatePublicationHTML()
    else:
        file_name = os.path.join("_pages", file_name)
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read()
    
def getIncludes(content):
    pattern = r'(<include src="(.+\.html)"/>)'
    return re.findall(pattern, content)

def replaceIncludes(content, matches):
    for m in matches:
        repl = getContent(m[1])
        content = content.replace(m[0], repl)
    return content

def writeToFile(file_name, content):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(content)

def compileFile(file_name):
    content = getContent(file_name)
    matches = getIncludes(content)
    content = replaceIncludes(content, matches)
    writeToFile(file_name, content)


if __name__ == "__main__":
    main()



