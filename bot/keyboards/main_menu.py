from keyboards.inline.consts import InlineConstructor


class MainMenuCallbacks:
    youtube = "youtube"
    instagram = "instagram"
    download = "download"
    back = "back"
    reject = "reject"


class MainMenu(InlineConstructor):
    class Actions:
        youtube = {"text": "▶️ YouTube", "callback_data": MainMenuCallbacks.youtube}
        instagram = {"text": "📸 Instagram", "callback_data": MainMenuCallbacks.instagram}
        download = {"text": "⇲ Скачать", "callback_data": MainMenuCallbacks.download}
        back = {"text": "↩︎ Назад", "callback_data": MainMenuCallbacks.back}
        reject = {"text": "😓 Отмена", "callback_data": MainMenuCallbacks.reject}

    @classmethod
    def main_menu(cls):
        schema = [3]
        actions = [cls.Actions.youtube, cls.Actions.instagram, cls.Actions.reject]
        return MainMenu._create_kb(actions, schema)

    @classmethod
    def download_menu(cls):
        schema = [3]
        actions = [cls.Actions.download, cls.Actions.back, cls.Actions.reject]
        return MainMenu._create_kb(actions, schema)
