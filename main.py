import scrape
import output


links = []
infos = []
index = 1

resume = 'resume.pdf'

with open("links.txt") as f:
    for line in f:
        links.append(line)

for link in links:
    print(f"scraping link {index} of {len(links)}")
    newdesc = scrape.getInfo(link)
    infos.append(newdesc)
    print("scraped")
    index += 1
    
index = 1
for info in infos:
    print(f"generating cover letter {index} of {len(infos)}")
    resp = output.genResp(info, resume)
    f = open(f"letters/{info.title}.md", "w")
    f.write(resp)
    print("generated - it may take a minute for the text file to populate")
    index += 1
    
    
