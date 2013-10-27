import csv
from StringIO import StringIO
from lxml import etree

def FBCDataReader(filename):
    with open(filename, 'r') as csvfile:
        body_parser = etree.XMLParser(recover=True)
        data_reader = csv.reader(csvfile, delimiter=',', quotechar='"', )
        next(data_reader, None)  # skip the headers
        for row in data_reader:
            identifier = row[0]
            title = row[1]
            body = '<body>' + row[2] + '</body>'
            parsed_body = etree.parse(StringIO(body), body_parser)
            if len(row) > 3:
                tags = row[3].strip().split()
            else:
                tags = []
            
            body_text = StringIO()
            body_code = StringIO()
            
            for element in parsed_body.getroot().iter():
                if element.tag == 'code':
                    body_code.write(element.text)
                else:
                    body_text.write(element.text)
 
            yield (identifier, title, body, body_text.getvalue(), body_code.getvalue(), tags)

if __name__ == '__main__':
    for (identifier, title, body, body_text, body_code, tags) in FBCDataReader("Train.csv"):
        print tags
        print body_code

