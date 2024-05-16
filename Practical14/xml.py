#need pip install xml.dom.minidom
import xml.dom.minidom as minidom
import datetime
import xml.sax
import matplotlib.pyplot as plt  


file = "./Practical14/go_obo.xml"

# biological_process/molecular_function//cellular_component
def init_frequency(s):
    s["biological_process"] = 0
    s["molecular_function"] = 0
    s["cellular_component"] = 0


class MyContentHandler( xml.sax.ContentHandler ):
    def __init__(self, freq):
        self.term = False
        self.namespace = False
        self.freq = freq
        self.content = ""

    def startElement(self, name, attrs):
        # print("start", name)
        if(name == "term"):
            self.term = True
            self.namespace = False
        elif self.term and name == "namespace":
            self.namespace = True
            self.content = ""
        pass
    
    def endElement(self, tag):
        # print("end", tag, self.term, self.namespace)
        if self.namespace and tag == "namespace":
            # check key is existed
            if self.content in self.freq:
                self.freq[self.content] += 1        
            else:
                print("unknown namespace:", self.content)
            self.namespace = False
            
        if self.term and tag == "term":
            self.term = False
            
    # Call when a character is read, note: will repeat few times
    def characters(self, content):
        # print("    ", content)
        if self.term and self.namespace:
            self.content += content


def dom_parse(filename):
    freq = {}
    init_frequency(freq)
    dom = minidom.parse(filename)
    doc = dom.documentElement

    terms = dom.getElementsByTagName("term")
    for term in terms: 
        namespace = term.getElementsByTagName("namespace")[0].firstChild.data 
        freq[namespace] += 1        
    return freq

def sax_parse(filename):
    freq = {}
    init_frequency(freq)

    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # override the default ContextHandler
    Handler = MyContentHandler(freq)
    parser.setContentHandler( Handler )
    parser.parse(file)
    return freq
    

start  = datetime.datetime.now()
domFreq = dom_parse(file)
useTime = datetime.datetime.now() - start
print("DOM time:", useTime.total_seconds())
print(domFreq)

#########################################################################
start  = datetime.datetime.now()
saxFreq = sax_parse(file)
useTime = datetime.datetime.now() - start

print("SAX time:", useTime.total_seconds())
print(saxFreq)

# By check the result SAX is much faster than DOM API
# DOM time: 29.760285
# {'biological_process': 30794, 'molecular_function': 12154, 'cellular_component': 4392}
# SAX time: 7.49912
# {'biological_process': 30794, 'molecular_function': 12154, 'cellular_component': 4392}


def create_barplot(freq, title):
    # refer to https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html#sphx-glr-gallery-lines-bars-and-markers-bar-colors-py
    fig, ax = plt.subplots()

    bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

    ax.bar(freq.keys(), freq.values(), color=bar_colors)

    ax.set_ylabel('Frequency')
    ax.set_title(title)


create_barplot(domFreq, "GO terms by DOM")
create_barplot(saxFreq, "GO terms by SAX")

plt.show()
