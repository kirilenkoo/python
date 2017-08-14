import re
urls = ["http://www.pitt.edu/check", "https://www.pitt.edu/check", "https://owijoej.owijeoif.pitt.edu/oiweo", "http://oijwoef.oiwjeoif.pitt.edu/jowijef/joisjd/oiwejf?jojw=oiwe&owiejf=owief"
        , "ftp://www.pitt.edu/slkdjf", "http://sdf.google.edu/slkji", "http://addmission.pitt.com/slji", "http://www.pitt.edu/"]

matchStr = "^(http://|https://)\S+\.pitt\.edu/\S*$"
for url in urls:
    if re.match(matchStr, url):
        print "match"
    else:
        print "not match"
