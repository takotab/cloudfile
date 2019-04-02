from cloudfile.__main__ import MainCloudFile


def test_enable():
    MainCloudFile().enable_google_drive()
