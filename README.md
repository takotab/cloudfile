# Cloudfile
Cloudfile can upload and download (large) files to the original position.


[![codecov](https://codecov.io/gh/takotab/cloudfile/branch/master/graph/badge.svg)](https://codecov.io/gh/takotab/cloudfile)

# Installation
`pip install cloudfile`

# Usage
`python -m cloudfile restore`

This will restore the keys with the corresponding urls in `cloudfile.json`. Add `--hard=True` to download all file even if they already exist.

`python -m cloudfile add_file`

Uploud the file to google drive and adds the link to `cloudfile.json`. To use this option you need to install Google Client Library and login to your google account. This means executing `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`. The files will be called `cloudfile_{filename}` and by default will be accessible to anyone who has the link.

`python -m cloudfile add_link file url`

Add a file to `cloudfile.json` the location should be `file` and `link` is the download location. Please ensure it's the actual file not the share page.
You can use: [https://syncwithtech.blogspot.com/p/direct-download-link-generator.html](https://syncwithtech.blogspot.com/p/direct-download-link-generator.html) to convert a link to the actual file.

`python -m cloudfile del_link file`

Delete a link from `cloudfile.json`

`python -m cloudfile download file`

Download the file even if the file already exists.

# TODO
- instructions on making api credetials
- make zip of files
- add_folder
- Handle larger files (<5MB)
- Make a google drive folder `cloudfile` 
