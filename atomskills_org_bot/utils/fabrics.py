from aiogram.filters.callback_data import CallbackData


class ServiceAnswerCallback(CallbackData, prefix="service_answer_callback"):
    callback: str
    request_id: int
