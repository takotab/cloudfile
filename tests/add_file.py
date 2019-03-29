import cloudfile


def test_add_file():
    filename = "foo/bar_new.txt"
    with open(filename, "w") as f:
        f.write("hello world")
    cloudfile.add_file(filename)
