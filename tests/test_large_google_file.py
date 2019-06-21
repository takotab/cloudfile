from cloudfile.check_downloaded import file_downloaded


def test_large_file_error():
    assert not file_downloaded("tests/assests/pose_resnet_50_256x192.pth.tar")


def test_large_download():
    assert 0 == 1
