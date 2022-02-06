from mycroft import MycroftSkill, intent_file_handler


class RoboInteract(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('interact.robo.intent')
    def handle_interact_robo(self, message):
        action = message.data.get('action')

        self.speak_dialog('interact.robo', data={
            'action': action
        })


def create_skill():
    return RoboInteract()

