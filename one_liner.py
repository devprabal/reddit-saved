import json
import os

mydict = {}
with open("trimmed_saved_posts.json", 'r') as read_file:
    mydict = json.load(read_file)

filename = "oneliner.txt"

content_list = []

for i in range(len(mydict['children'])):
    content = ""
    kind = mydict['children'][i]['kind']
    if kind == "t3":
        subreddit_name_prefixed = mydict['children'][i]['subreddit_name_prefixed']
        title = mydict['children'][i]['title']
        created = mydict['children'][i]['created']
        permalink = mydict['children'][i]['permalink']
        permalink = "https://www.reddit.com"+permalink

        content = str(int(created))+"\t"+title+"\t"+subreddit_name_prefixed+"\t"+permalink
        content_list.append(content)

with open(filename, 'w') as write_file:
    for i in content_list:
        write_file.write(i + os.linesep)

print("Done.\nYou can now search easily through file "+filename+" using any suitable tool.")
