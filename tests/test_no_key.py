import os
import pytest

from cloudfile.google.google_drive import get_service


# @pytest.fixture()
# def rename_name():
#     yield
#     print("teardown")


def test_no_key():
    os.rename("credentials.json", "_credentials.json")
    os.rename("token.pickle", "_token.pickle")
    with pytest.raises(FileNotFoundError):
        get_service()
    os.rename("_credentials.json", "credentials.json")
    os.rename("_token.pickle", "token.pickle")
