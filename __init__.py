from mycroft import MycroftSkill, intent_file_handler


class JaJaDingDong(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('dong.ding.ja.ja.intent')
    def handle_dong_ding_ja_ja(self, message):
        self.speak_dialog('dong.ding.ja.ja')


def create_skill():
    return JaJaDingDong()

