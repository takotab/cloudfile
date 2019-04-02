# Cloudfile
Cloudfile can upload and download (large) files to the original position.


[![codecov](https://codecov.io/gh/takotab/cloudfile/branch/master/graph/badge.svg)](https://codecov.io/gh/takotab/cloudfile) [![Downloads](https://pepy.tech/badge/cloudfile)](https://pepy.tech/project/cloudfile)

# Installation
- `pip install cloudfile`
- If you only want to use cloudfile to restore you are done. 
- To also upload you need to install Google Client Library, make an API key, and login to your google account. This means executing:
  -  `python -m cloudfile enable_google_drive`
  - This will install the Google Client Library and open https://developers.google.com/drive/api/v3/quickstart/python
  - On site, click on `Enable the Drive API` to make an API key. Save the file in the root directory as `credentials.json`.

# Usage
- `python -m cloudfile restore`

    This will restore the keys with the corresponding urls in `cloudfile.json`. Add `--hard=True` to download all file even if they already exist.

- `python -m cloudfile add folder`
    Uplouds file or the content of the folder to google drive and adds the link to `cloudfile.json`. 

- `python -m cloudfile add_file file`

    Uploud the file to google drive and adds the link to `cloudfile.json`.  The files will be called `cloudfile_{filename}` and by default will be accessible to anyone who has the link.

- `python -m cloudfile add_link file url`

    Add a file to `cloudfile.json` the location should be `file` and `link` is the download location. Please ensure it's the actual file not the share page.
    You can use: [https://syncwithtech.blogspot.com/p/direct-download-link-generator.html](https://syncwithtech.blogspot.com/p/direct-download-link-generator.html) to convert a link to the actual file.

- `python -m cloudfile del_link file`

    Delete a link from `cloudfile.json`

- `python -m cloudfile download file`

    Download the file even if the file already exists.

# TODO
- make zip of files
- Handle larger files (<5MB)
- Make a google drive folder `cloudfile` 
