from pydantic import BaseModel

from atomskills_org_bot.enums import *


class ServiceModel(BaseModel):
    service_name: ServiceNameEnum
    comment: ServiceCommentEnum
    chat_id: int
    state: ServiceStateEnum
