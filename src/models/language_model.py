from database.db import db

from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, json_data):
        super().__init__(json_data)

    def to_dict(self):
        language_data = self.data.get("name")
        acronym_data = self.data.get("acronym")

        if language_data is None or acronym_data is None:
            raise ValueError("Name or acronym data is missing")

        return {"name": language_data, "acronym": acronym_data}
