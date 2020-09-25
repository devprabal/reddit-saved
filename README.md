## Usage

:one: Get reddit credentials by setting up an app [here](https://www.reddit.com/prefs/apps/) by following [this reddit wiki](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps)


:two: Fill [auth.json](auth.json) file with those credentials.


:three: Run [get_files.py](get_files.py) script and then run [trim_data.py](trim_data.py) script.

```bash
python3 get_files.py
```

[:four:] Optionally run [one_liner.py](one_liner.py) script to generate a file which has tab-separated important values from the saved posts and which can be used for searching like [search_script.sh](search_script.sh).

------------------------------------------------------------------------------------------

:question: **HOW** this works

:x: I was using [this](https://www.reddit.com/r/help/comments/f8uyq/is_there_export_import_for_saved_links/) to save manually (I know it sucks). 


:heavy_check_mark: I used the reddit api and created a python script to download the saved messages data and then trimmed that data to my liking and then used `fzf` to search through it.


:two: [updoot.app](https://updoot.app/app) :arrow_right: is another good way to for browsing and searching through saved posts. But it doesn't seem to have an option to export them.

------------------------------------------------------------------------------------------

Maybe in future I will search for better alternatives to automate this task.


But for now the :heavy_check_mark: method works fine.

------------------------------------------------------------------------------------------

[huginn ](https://github.com/huginn/huginn) :arrow_right: to try


[ifttt ](http://ifttt.com/) :arrow_right: didn't seem to work