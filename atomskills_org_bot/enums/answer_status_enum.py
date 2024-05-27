from enum import Enum


class AnswerStatusEnum(Enum):
    IGNORED = "Еще не принято в работу"
    RESOLVED = "Принято в работу ✅"
    DENIED = "отклонено ❌"

    minutes_5_10 = "5-10 минут"
    minutes_10_20 = "10-20 минут"
    minutes_20_30 = "20-30 минут"
    minutes_30_60 = "30 минут - час"
    DENY = "отклонить ❌"

    @classmethod
    def get_answer_options(cls) -> list["AnswerStatusEnum"]:
        return [
            cls.minutes_5_10,
            cls.minutes_10_20,
            cls.minutes_20_30,
            cls.minutes_30_60,
            cls.DENY,
        ]
