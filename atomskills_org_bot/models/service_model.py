from pydantic import BaseModel

from atomskills_org_bot.enums.service_comment_enum import ServiceCommentEnum
from atomskills_org_bot.enums.service_name_enum import ServiceNameEnum


class ServiceModel(BaseModel):
    service_name: ServiceNameEnum
    comment: ServiceCommentEnum
    chat_id: int
