from enum import Enum

from aiogram.fsm.state import State

from atomskills_org_bot.enums import ServiceNameEnum


class ServiceStateEnum(Enum):
    SERVICE_STATE_1 = State(ServiceNameEnum.SERVICE_NAME_1.name)
    SERVICE_STATE_2 = State(ServiceNameEnum.SERVICE_NAME_2.name)
    SERVICE_STATE_3 = State(ServiceNameEnum.SERVICE_NAME_3.name)
    SERVICE_STATE_4 = State(ServiceNameEnum.SERVICE_NAME_4.name)
    SERVICE_STATE_5 = State(ServiceNameEnum.SERVICE_NAME_5.name)
    SERVICE_STATE_6 = State(ServiceNameEnum.SERVICE_NAME_6.name)
    SERVICE_STATE_7 = State(ServiceNameEnum.SERVICE_NAME_7.name)
    SERVICE_STATE_8 = State(ServiceNameEnum.SERVICE_NAME_8.name)
    SERVICE_STATE_9 = State(ServiceNameEnum.SERVICE_NAME_9.name)
    SERVICE_STATE_10 = State(ServiceNameEnum.SERVICE_NAME_10.name)
