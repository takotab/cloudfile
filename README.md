# Cloudfile
Cloudfile will download (large) files to the original position.


[![codecov](https://codecov.io/gh/takotab/cloudfile/branch/master/graph/badge.svg)](https://codecov.io/gh/takotab/cloudfile)

# Installation
`pip install cloudfile`

# Usage
`cloudfile restore`
This will restore the keys with the corresponding urls in `cloudfile.json`. Add `--hard=True` to download all file even if they already exist.

`cloudfile add_link file url`
Add a file to `cloudfile.json` the location should be `file` and `link` is the download location. Please ensure it's the actual file not the share page.
You can use: [https://syncwithtech.blogspot.com/p/direct-download-link-generator.html](https://syncwithtech.blogspot.com/p/direct-download-link-generator.html) to convert a link to the actual file.

`cloudfile del_link file`
Delete a link from `cloudfile.json`

`cloudfile download file`
Download the file even if the file already exists.

#TODO
- be able to also upload files 
- 
