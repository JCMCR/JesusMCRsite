import requests
from optparse import OptionParser
from calendar import datetime
import re

#Clean input
parser = OptionParser();
parser.add_option("-d", "--date", dest="date", help="The date of the bulletin as three integers: 'year month day' (default: today)", type="int", nargs=3, default=datetime.date.today().timetuple());
parser.add_option("-u", "--url", dest="url", help="The input url", type="str", default="http://groupspaces.com/jesus-mcr/e/557715?s=aaa5a08d&utm_medium=email&utm_source=group-mail&utm_term=group-mail-85460");
(options, args) = parser.parse_args();
date = datetime.date(options.date[0], options.date[1], options.date[2]);
url = options.url;
#Get bulletin content
content = requests.get(url).text;

searchString = "(?<=framedocument\.write\(\\\\).+(?=\);\\\\n\\\\nvar resizePreviewFrame)";
searchString = "(?<=framedocument\.write\(\\\\\').+(?=\\\\\\\\n\\\\\'\);\\\\n\\\\nvar resizePreviewFrame)";
searchString = "(?<=framedocument\.write\(\\\').+(?=\\\\n\'\);\n\nvar resizePreviewFrame)";
searchString = "(?<=framedocument\.write\(\\\').+(?=\\\\n\'\);\n\nvar resizePreviewFrame)";
searchString = "<iframe id=\"html_preview_iframe\".+}\n</script>"
bulletin = re.search(searchString, content, re.DOTALL).group(0);
#searchString = "<link rel=\"stylesheet\".+media=\"screen, projection, print\">";
#styleSheet = re.search(searchString, content).group(0);
#searchString = "<script.+</script>";
#script = re.search(searchString, content).group(0);
#searchString = "<head>.+</head>";
#head = re.search(searchString, content, re.DOTALL).group(0);

#Write page
fout = open("{:}-Bulletin.html".format(date), 'w');

fout.write(
"""---
title: {:} Bulletin
layout: defaultPlain
categories: private bulletin
logoLink: /
menu1: Main Site
menu1Link: /
menu2: Current Students
menu2Link: /private/

---
""".format(date));
fout.write("<script src=\"http://media.groupspaces.com/js/prototype/1.6.1/prototype.js\"></script>");

fout.write("</br><div class=\"email email_preview_not_admin \">");
fout.write(bulletin);
fout.write("</div>");
fout.write("</body></html>")

fout.close();
