# This python script creates HTML index files to read the backup data from colmsg

import os
import sys
import html

# This is your nick name, or how you want the member to call you
NICK_NAME="<b>としくん</b>"

# This is the output path where the HTML files are saved
# The HTML files will be by month and saved in folders by member name
OUTPUT_PATH="/Prog/colmsg_html/t"


MEMBER_LIST=[]
MONTH_LIST=[]
MAIN_LIST=[]

HTML_HEADER=" \
<html> \
<head> \
<style> \
 td { font-size: 9pt; background-color: #f0f0f0; color: #333; padding: 10px; border: 1px solid #ccc}  \
 td:hover {background-color:#cce5ff}  \
</style> \
</head> \
<body> \
<table> \
<tr><td width='130'>Date / Time (GMT)</td><td>Message</td></tr> \
"

HTML_FOOTER=" \
</table> \
</body> \
</html> \
"

def readTxtFile(file_path):
  f=open(file_path, 'r', encoding='utf-8')
  content=f.read()
  return content

def addUniqueMember(member):
  if member not in MEMBER_LIST:
    MEMBER_LIST.append(member)

def addUniqueMonth(month):
  if month not in MONTH_LIST:
    MONTH_LIST.append(month)
    
def getTimeString(file_name):
  parts=file_name.split('_')
  if len(parts) > 2:
    return parts[2][0:4] + "-" + parts[2][4:6] + "-" + parts[2][6:8] + " " + parts[2][8:10] + ":" + parts[2][10:12]  
  return ""

def getYearMonth(file_name):
  parts=file_name.split('_')
  if len(parts) > 2:
    year_month = parts[2][0:6]  # Get the first 6 characters (YYYYMM)
    return year_month
  return None

def getMemberName(item_path):
  normalized_path = os.path.normpath(item_path)
  path_parts = normalized_path.split(os.path.sep)
  last_folder = path_parts[-1] if len(path_parts) > 0 else None
  return last_folder
  
  
def getGroupName(item_path):
  normalized_path = os.path.normpath(item_path)
  path_parts = normalized_path.split(os.path.sep)
  second_last_folder = path_parts[-2] if len(path_parts) > 1 else None
  return second_last_folder
  
def getFileNamesFromColMsg(parent_directory):
    # List to store all file names
    file_names = []

    # Loop through each item in the parent directory
    for item in os.listdir(parent_directory):
        item_path = os.path.join(parent_directory, item)
        # Check if the item is a directory
        if os.path.isdir(item_path):
            # List all files in the subdirectory
            for file_name in os.listdir(item_path):
                member=getGroupName(item_path) + "-" + getMemberName(item_path)
                month=getYearMonth(file_name)
                addUniqueMember(member)
                addUniqueMonth(month)
                content=""
                if file_name.lower().endswith(".txt"):
                  content=html.escape(readTxtFile(item_path+"/"+file_name)).replace('\n', '<br>')
                file_names.append((member,month,getTimeString(file_name),file_name, os.path.normpath(item_path), content))
                
    return file_names
    
def genMonthlyPackContent(member, month):
    selected=(member, month)
    matching=[record for record in MAIN_LIST if record[:2] == selected]
    return matching

def getMessageFileName(member, month):
    directory= OUTPUT_PATH + "/" + member
    if not os.path.exists(directory):
      os.makedirs(directory)
    return directory + "/" + member + month +".html" 

def getTxtContent(record):
    html=""
    html+="<tr><td>" + record[2] + "</td>"
    html+="<td>"+record[5].replace("%%%", NICK_NAME)+"</td>"
    html+="</tr>\n"
    return html

def getJpgContent(record):
    html=""
    html+="<tr><td>" + record[2] + "</td>"
    html+="<td><img src='" + record[4] + "/" + record[3] + "' /></td>"
    html+="</tr>\n"
    return html

def getMp4Content(record):
    html=""
    html+="<tr><td>" + record[2] + "</td>"
    html+="<td><video controls><source src='"+record[4]+ "/" + record[3]+ "' type='video/mp4'></video></td>"
    html+="</tr>\n"
    return html


def genMessageFile(member, month, content):
    html="";
    html+=HTML_HEADER
    for record in content:
      if record[3].endswith(".txt"):
        html+=getTxtContent(record)
      elif record[3].endswith(".jpg"):
        html+=getJpgContent(record)
      elif record[3].endswith(".mp4"):
        html+=getMp4Content(record)
    html+=HTML_FOOTER

    with open(getMessageFileName(member, month), 'w', encoding='utf-8') as file:
      file.write(html)

def loopList():
    for member in MEMBER_LIST:
      for month in MONTH_LIST:
        content=genMonthlyPackContent(member, month)
        if content:
          genMessageFile(member, month, content)


if __name__ == "__main__":

    if len(sys.argv) >=3:
        parent_dir = sys.argv[1]          
        OUTPUT_PATH = sys.argv[2]  
        if len(sys.argv) ==4:    
            NICK_NAME = sys.argv[3]
        
        print(f"Generating messages from: {parent_dir} and saving to: {OUTPUT_PATH}")
        MAIN_LIST=getFileNamesFromColMsg(parent_dir)
        MEMBER_LIST.sort()
        MONTH_LIST.sort()
        loopList()
    else:
        print("Usage: colmsg_html <INPUT PATH> <OUTPUT PATH> [NICK NAME]")    
        print("   INPUT PATH is the folder where the source files are located by group level");
        print("   OUTPUT PATH is the folder where you want to store the generated HTML files");
        print("   NICK NAME is your nick name, or how you want the member to call you (optional)");
        