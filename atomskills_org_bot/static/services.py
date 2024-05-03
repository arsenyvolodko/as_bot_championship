from atomskills_org_bot.models import ServiceModel
from atomskills_org_bot.enums import ServiceNameEnum, ServiceCommentEnum, ServiceChatIdEnum


_NAMES = list(ServiceNameEnum.__members__.values())
_COMMENTS = list(ServiceCommentEnum.__members__.values())
_CHATS = list(ServiceChatIdEnum.__members__.values())

SERVICE_MODELS = {
    name_enum.value: ServiceModel(
        service_name=name_enum,
        comment=_COMMENTS[ind],
        chat_id=_CHATS[ind]
    ) for ind, name_enum in enumerate(_NAMES)
}

for i in SERVICE_MODELS:
    print(SERVICE_MODELS[ServiceNameEnum.SERVICE_NAME_1])
