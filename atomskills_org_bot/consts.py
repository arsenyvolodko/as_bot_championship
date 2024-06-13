from aiogram.fsm.state import State

COMMENT_AWAITING_STATE = State("COMMENT_AWAITING_STATE")
CONFIRMATION_AWAITING_STATE = State("CONFIRMATION_AWAITING_STATE")
COMMON_CHAT_ID = -1002198856707

START_TEXT = ("Этот бот позволяет направить обращение по выбранной тематике.\n"
              # "Для просмотра доступных сервисов и их описания используйте команду /help.\n"
              "Чтобы направить обращение, перейдите в меню, используя кнопку ниже, и следуйте инструкциям.")

CANCEL_TEXT = "Отмена"
CONFIRM_TEXT = "Продолжить"
SKIP_COMMENT_TEXT = "Пропустить"

MARK_AS_CLOSE_TEXT = "Отметить как выполненное"
MARK_AS_CLOSED_CALLBACK = "MARK_AS_RESOLVED_CALLBACK"

BACK_TO_MENU = 'В меню ⤵️'
BACK = 'Назад ⤵️'

HALL_CHOICE_TEXT = 'Выберите павильон расположения компетенции.'
LOCATION_CHOICE_TEXT = 'Выберите компетенцию где Вы на ГЭ.'
SERVICE_CHOICE_TEXT = 'Выберите тематику обращения.'
OPTION_CHOICE_TEXT = 'Укажите цель обращения.'
COMMENT_CHOICE_TEXT = 'Введите дополнительный комментарий для представителей сервиса. Если вы считаете, что вся неоходимая информация уже была Вами указана, Вы можете пропустить этот шаг.'

STATUS_INFO = "Статус обращения: {}."
# HELP_TEXT = ""
# for key in SERVICE_MODELS:
#     HELP_TEXT += f"<b>{key}</b>: {SERVICE_MODELS[key].comment.value}.\n\n"
# HELP_TEXT += f"В случае технических неисправностей с ботом обращаться к @arseny_volodko"
