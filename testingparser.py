def parseXML(xmlFile):
    '''xml.etree module failed to parse the corrupted XML
        document as it required prior proper format. 
        
        Beautiful soup was able to construct the tree structure 
        despite the corrupted XML.
        
        Problem in the current code base in parsing:
        1. It creates huge chunk of in memory list and dictionary just to be consumed later.
        2. since it loads the XML document at once, this might cause intense CPU bound 
        during load time.
        
        Solution needed: 
        1. Need to eliminate in list and dictionary with generator pipeline
        2. Load the xml into memory in pieces and pass it to the pipeline
        
        '''
    with open(xmlFile,  mode='r') as file:
        soup = BeautifulSoup(file, 'lxml-xml')
        rows = []
        for message_elem in soup.find_all('message'):
            #make '' as a default string if the value returned is None
            channel = message_elem.channel.string or ''
            content = message_elem.content.string or ''
            datetime = message_elem.datetime.string or ''
            direction =  message_elem.direction.string or ''
            message = ''
            network = message_elem.network.string or ''
            recipientEmail =  message_elem.recipientEmail.string or ''
            recipientIMID = message_elem.recipientIMID.string or ''
            recipientYJID = message_elem.recipientYJID.string or ''
            senderEmail = message_elem.senderEmail.string or ''
            senderIMID = message_elem.senderIMID.string or ''
            senderYJID = message_elem.senderYJID.string or ''
            
            #creating a dict out of it and append to rows
            rows.append(dict(
                    channel = channel.strip(),
                    content = content.strip(),
                    datetime = datetime.strip(),
                    direction = direction.strip(),
                    message = message.strip(),
                    network = network.strip(),
                    recipientEmail = recipientEmail.strip(),
                    recipientIMID = recipientIMID.strip(),
                    recipientYJID = recipientYJID.strip(),
                    senderEmail = senderEmail.strip(),
                    senderIMID = senderIMID.strip(),
                    senderYJID = senderYJID.strip()
                ))
            
            #yield dict(.....) would be much more efficient if the dicts are being
            #consumed in some iteration
            #instead of building list out of the function
            return rows

def main():
    l = parseXML('test.xml')
    print l
main()
