from atomskills_org_bot.utils.services import SERVICE_MODELS

START_TEXT = ("Этот бот позволяет при необходимости направить обращение в соответсвующий сервис.\n"
              "Для просмотра доступных сервисов и их описания используйте команду /help.\n"
              "Чтобы направить обращение, выберите необходимый сервис среди клавиш на клавиатуре и следуйте инструкциям.")

CANCEL_CALLBACK = "CANCEL_CALLBACK"
STATUS_INFO = "Статус обращения: {}."

HELP_TEXT = ""
for key in SERVICE_MODELS:
    HELP_TEXT += f"<b>{key}</b>: {SERVICE_MODELS[key].comment.value}.\n"
