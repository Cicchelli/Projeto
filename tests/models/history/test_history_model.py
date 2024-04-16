"""Module providing a function printing python version."""

import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    """Function printing python version."""
    dict_1 = {
        "text_to_translate": "Hello, I like videogame",
        "translate_from": "en",
        "translate_to": "pt",
    }
    dict_2 = {
        "text_to_translate": "Do you love music?",
        "translate_from": "en",
        "translate_to": "pt",
    }

    history = json.loads(HistoryModel.list_as_json())
    assert isinstance(history, list)
    for index, item in enumerate([dict_1, dict_2]):
        assert "_id" in history[index]
        assert item["text_to_translate"] == history[index]["text_to_translate"]
        assert item["translate_from"] == history[index]["translate_from"]
        assert item["translate_to"] == history[index]["translate_to"]
