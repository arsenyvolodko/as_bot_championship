from aiogram.fsm.state import State

COMMENT_AWAITING_STATE = State("COMMENT_AWAITING_STATE")
CONFIRMATION_AWAITING_STATE = State("CONFIRMATION_AWAITING_STATE")

START_TEXT = (
    "Этот бот позволяет направить обращение по выбранной тематике. Для начала использования перейдите в меню, используя кнопку ниже и следуйте инструкциям.\n")

CANCEL_TEXT = "Отмена"
CONFIRM_TEXT = "Продолжить"
SKIP_COMMENT_TEXT = "Пропустить"

MARK_AS_CLOSE_TEXT = "Отметить как выполненное"
MARK_AS_CLOSED_CALLBACK = "MARK_AS_RESOLVED_CALLBACK"

BACK_TO_MENU = 'В меню ⤵️'
BACK = 'Назад ⤵️'

HALL_CHOICE_TEXT = 'Выберите павильон расположения компетенции, где что-то требуется сделать/исправить.'
LOCATION_CHOICE_TEXT = 'Выберите компетенцию, где что-то требуется сделать/исправить'
SERVICE_CHOICE_TEXT = 'Выберите тематику вашего обращения.'
OPTION_CHOICE_TEXT = 'Укажите цель обращения.'
COMMENT_CHOICE_TEXT = 'Введите дополнительный комментарий для представителей отделов. Если вы считаете, что вся необходимая информация уже была Вами указана, Вы можете пропустить этот шаг.'

STATUS_INFO = "Статус обращения: {}."
