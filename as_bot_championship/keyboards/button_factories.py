from aiogram.filters.callback_data import CallbackData

GO_TO_MAIN_MENU = "Перейти в меню"
BACK_TO_MAIN_MENU_CALLBACK = "BACK_TO_MAIN_MENU_CALLBACK"


class HallChoiceFactory(CallbackData, prefix="hall_choice_callback_factory"):
    hall_id: int


class LocationChoiceFactory(CallbackData, prefix="location_choice_callback_factory"):
    hall_id: int
    location_id: int


class LocationPageFactory(CallbackData, prefix="location_page_callback_factory"):
    hall_id: int
    page_num: int


class ServiceChoiceFactory(CallbackData, prefix="service_choice_callback_factory"):
    hall_id: int
    location_id: int
    service_id: int


class ServicePageFactory(CallbackData, prefix="service_page_callback_factory"):
    hall_id: int
    location_id: int
    page_num: int


class OptionChoiceFactory(CallbackData, prefix="option_choice_callback_factory"):
    hall_id: int
    location_id: int
    service_id: int
    option_id: int


class SkipFactory(CallbackData, prefix="skip_callback_factory"):
    location_id: int
    option_id: int


class ConfirmationFactory(CallbackData, prefix="confirmation_callback_factory"):
    service_id: int
    location_id: int
    option_id: int
    confirmed: bool


class ServiceAnswerFactory(CallbackData, prefix="service_answer_factory"):
    callback: str
    request_id: int


class CloseRequestFactory(CallbackData, prefix="close_request_factory"):
    request_id: int
