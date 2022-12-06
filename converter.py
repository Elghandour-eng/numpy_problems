
from bs4 import BeautifulSoup
import json
#Fro Remote Page
#import urllib
#url = 'Link'
#response = urllib.request.urlopen(url)
response = open("Numpy in Lecture.html",'r', encoding="utf8") 
text = response.read()
soup = BeautifulSoup(text, 'lxml')
# see some of the html
dictionary = {'nbformat': 4, 'nbformat_minor': 1, 'cells': [], 'metadata': {}}
for d in soup.findAll("div"):
    if 'class' in d.attrs.keys():
        for clas in d.attrs["class"]:
            if clas in ["jp-RenderedText", "jp-InputArea-editor","jp-MarkdownCell"]:
                # code cell
                #print(clas)
                if clas == "jp-InputArea-editor":
                    cell = {}
                    cell['metadata'] = {}
                    cell['outputs'] = []
                    cell['source'] = [d.get_text()]
                    cell['execution_count'] = None
                    cell['cell_type'] = 'code'
                    dictionary['cells'].append(cell)
                elif clas == "jp-MarkdownCell":
                    cell = {}
                    cell['metadata'] = {}
                    cell['outputs'] = []
                    cell['source'] = [d.decode_contents()]
                    cell['execution_count'] = None
                    cell['cell_type'] = 'markdown'
                    dictionary['cells'].append(cell)    

                else:
                    
                    cell = {}
                    cell['metadata'] = {}
                    
                    cell['source'] = [d.decode_contents()]
                    cell['cell_type'] = 'markdown'
                    dictionary['cells'].append(cell)
open('final.ipynb', 'w').write(json.dumps(dictionary))
