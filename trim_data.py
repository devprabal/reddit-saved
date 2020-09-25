import json
import os

data_download_dir = "data_download"

if not os.path.exists(data_download_dir):
    print("Run get_files.py script first")
    exit(1)

folder_names = []
for i in os.listdir(data_download_dir):
    folder_names.append(i)

file_names = []
for j in folder_names:
    for i in os.listdir(data_download_dir+"/"+j):
        full_file_path = data_download_dir+"/"+j+"/"+i
        file_names.append(full_file_path)

mydict = {}
mydict["children"] = []

myset = set()

for fp_path in file_names:
    data = {}
    with open(fp_path, "r") as read_file:
        data = json.load(read_file)

    for i in range(len(data['data']['children'])):
        permalink = data['data']['children'][i]['data'].get('permalink')
        if permalink not in myset:
            myset.add(permalink)
            child_info = {}
            child_info['kind'] = data['data']['children'][i]['kind']
            child_info["subreddit_name_prefixed"] = data['data']['children'][i]['data'].get('subreddit_name_prefixed')
            child_info["title"] = data['data']['children'][i]['data'].get('title')
            child_info["selftext"] = data['data']['children'][i]['data'].get('selftext')
            child_info["thumbnail"] = data['data']['children'][i]['data'].get('thumbnail')
            child_info["permalink"] = data['data']['children'][i]['data'].get('permalink')
            child_info["created"] = data['data']['children'][i]['data'].get('created')
            if data['data']['children'][i]['kind'] == 't1':
                child_info['body'] = data['data']['children'][i]['data'].get('body')
            if data['data']['children'][i]['kind'] == 't3':
                child_info['url'] = data['data']['children'][i]['data'].get('url')
            mydict["children"].append(child_info)

print("No. of saved posts = ", str(len(mydict['children'])))

final_file = "trimmed_saved_posts.json"
with open(final_file, "w") as write_file:
    json.dump(mydict, write_file)

print("Done.\nYou can now view ", final_file)