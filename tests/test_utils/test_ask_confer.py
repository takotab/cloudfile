from cloudfile.ask_confermation import query_yes_no


def test_ask_confer(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "Y")
    assert query_yes_no("ee")
    monkeypatch.setattr("builtins.input", lambda: "yes")
    assert query_yes_no("ee")
    monkeypatch.setattr("builtins.input", lambda: "Ye")
    assert query_yes_no("ee")
    monkeypatch.setattr("builtins.input", lambda: "n")
    assert not query_yes_no("ee")
    monkeypatch.setattr("builtins.input", lambda: "no")
    assert not query_yes_no("ee")

