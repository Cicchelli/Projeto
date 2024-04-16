from flask import Blueprint
from models.history_model import HistoryModel


history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def get_history():
    history = HistoryModel.list_as_json()
    return history, 200
