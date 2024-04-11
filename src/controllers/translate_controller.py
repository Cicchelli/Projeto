from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

translate_controller = Blueprint("translate_controller", __name__)

@translate_controller.route("/", methods=["GET"])
def get_translate():
    default_translation = {
        "text_to_translate": "O que deseja traduzir?",
        "translate_from": "pt",
        "translate_to": "en",
        "translated": "What do you want to translate?"
    }
    languages = LanguageModel.list_dicts()
    return render_template("index.html", languages=languages, **default_translation)

@translate_controller.route("/", methods=["POST"])
def post_translate():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translated = GoogleTranslator(source=translate_from, target=translate_to).translate(text_to_translate)

    default_translation = {
        "text_to_translate": text_to_translate,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "translated": translated
    }

    languages = LanguageModel.list_dicts()
    return render_template("index.html", languages=languages, **default_translation)