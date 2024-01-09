from mycroft import MycroftSkill, intent_file_handler


class Srbpcv(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('srbpcv.intent')
    def handle_srbpcv(self, message):
        self.speak_dialog('srbpcv')


def create_skill():
    return Srbpcv()

