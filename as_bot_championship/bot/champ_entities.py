from as_bot_championship.db.tables import Location, Option, Service, Hall

halls = [
    *[Hall(name=f"Павильон №{num}") for num in range(1, 4)],
    Hall(name="\"Шахматка\"")
]

locations = [
    Location(name="Бетонные строительные работы", hall_id=1),
    Location(name="Каракури", hall_id=1),
    Location(name="Промышленная механика и монтаж", hall_id=1),
    Location(name="Технологии композитов", hall_id=1),
    Location(name="Аддитивные технологии", hall_id=1),
    Location(name="Водитель спец.автомобиля", hall_id=1),
    Location(name="Изготовление прототипов", hall_id=1),
    Location(name="Промышленная автоматика", hall_id=1),
    Location(name="Сварочные технологии", hall_id=1),
    Location(name="Электромонтаж", hall_id=1),
    Location(name="Электроника", hall_id=1),
    Location(name="Комната лидеров команд", hall_id=1),
    Location(name="Склад для ТМЦ", hall_id=1),
    Location(name="Зона информации", hall_id=1),
    Location(name="Зона проверки на алкоголь", hall_id=1),
    Location(name="Склад для ТМЦ", hall_id=1),

    Location(name="Вывод из экспл. объектов атом. энергии", hall_id=2),
    Location(name="Инженерное проектирование", hall_id=2),
    Location(name="Математическое моделирование", hall_id=2),
    Location(name="Строительный контроль", hall_id=2),
    Location(name="Цифровое ПСР предприятие", hall_id=2),
    Location(name="Инженерный дизайн CAD", hall_id=2),
    Location(name="Инженер-технолог машиностроения", hall_id=2),
    Location(name="Квантовые технологии (СП Квант)", hall_id=2),
    Location(name="Неразрушающий контроль", hall_id=2),
    Location(name="Охрана окружающей среды", hall_id=2),
    Location(name="Охрана труда", hall_id=2),
    Location(name="Сметное дело", hall_id=2),
    Location(name="Тех.системы энергетических объектов", hall_id=2),
    Location(name="Программная роботизация", hall_id=2),
    Location(name="Зона информации", hall_id=2),
    Location(name="Зона проверки на алкоголь", hall_id=2),

    Location(name="Геодезия", hall_id=3),
    Location(name="Информационная безопасность", hall_id=3),
    Location(name="Корп. защита от внутр. угроз без-ти", hall_id=3),
    Location(name="Продуктовая разработка", hall_id=3),
    Location(name="Сетевое и сис. администрирование", hall_id=3),
    Location(name="Управление жизненным циклом", hall_id=3),
    Location(name="Управление качеством", hall_id=3),
    Location(name="Анал.контроль (лаб-хим анализ)", hall_id=3),
    Location(name="Машинное обучение и большие данные", hall_id=3),
    Location(name="Автоматизация тех.процессов", hall_id=3),
    Location(name="Обслуживание оборуд. релейной защиты", hall_id=3),
    Location(name="Радиационный контроль", hall_id=3),
    Location(name="Управ. комм-ми/Антикриз. реаг-ие", hall_id=3),
    Location(name="Разработка приложений на 1С", hall_id=3),
    Location(name="Графический дизайн", hall_id=3),
    Location(name="Зона информации", hall_id=3),
    Location(name="Зона проверки на алкоголь", hall_id=3),

    Location(name="Штаб организаторов", hall_id=4),
]

services = [
    Service(name="Обеспечение компетенции", chat_id=-1002696338559),                 # service_id = 1
    Service(name="Застройка", chat_id=-1002548316765),                               # service_id = 2
    Service(name="Электрика", chat_id=-1002638696932),                               # service_id = 3
    Service(name="Питьевая вода", chat_id=-1002545994172),                           # service_id = 4
    Service(name="Вентиляция, канализация, сжатый воздух", chat_id=-1002699446019),  # service_id = 5
    Service(name="Мебель", chat_id=-1002521497717),                                  # service_id = 6
    Service(name="Сеть, интернет и ИТ", chat_id=-1002269795231),                     # service_id = 7
    Service(name="Безопасность", chat_id= -1002595001452),                           # service_id = 8
    Service(name="Цифровая платформа", chat_id=-1002546473905),                      # service_id = 9
    Service(name="Уборка", chat_id=-1002450269099),                                  # service_id = 10
]


options = [
    Option(name="Расходные материалы", comment="", service_id=1),
    Option(name="Инструменты", comment="", service_id=1),
    Option(name="Канцелярские товары", comment="", service_id=1),
    Option(name="Несоответствие оборудования Илу", comment="", service_id=1),
    Option(name="Проблема с ТВ", comment="", service_id=1),
    Option(name="Проблема со звуком\микрофоном", comment="", service_id=1),
    Option(name="Проблема с принтером", comment="", service_id=1),
    Option(name="Проблема с компьютером", comment="", service_id=1),
    Option(name="Иное", comment="", service_id=1),

    Option(name="Проблемы со стенами", comment="", service_id=2),
    Option(name="Проблемы с дверью", comment="", service_id=2),
    Option(name="Иное", comment="", service_id=2),

    Option(name="Пропало электричество в розетке 220V", comment="", service_id=3),
    Option(name="Пропало электричество в розетке 380V", comment="", service_id=3),
    Option(name="Установить доп. розетки", comment="", service_id=3),
    Option(name="Требуется инженер-электрик", comment="", service_id=3),
    Option(name="Иное", comment="", service_id=3),

    Option(name="Нужна вода в бутылках 19 л", comment="", service_id=4),
    Option(name="Нужны стаканчики для воды", comment="", service_id=4),
    Option(name="Нужна бутилированная вода", comment="", service_id=4),
    Option(name="Иное", comment="", service_id=4),

    Option(name="Проблемы с вентиляцией", comment="", service_id=5),
    Option(name="Проблема со сжатым воздухом", comment="", service_id=5),
    Option(name="Проблема с водой/канализацией", comment="", service_id=5),

    Option(name="Нехватка мебели", comment="", service_id=6),
    Option(name="Несоответствующая мебель", comment="", service_id=6),
    Option(name="Сломанная мебель", comment="", service_id=6),
    Option(name="Иное", comment="", service_id=6),

    Option(name="Нет интернета (проводное подкл.)", comment="", service_id=7),
    Option(name="Нет интернета (wi-fi)", comment="", service_id=7),
    Option(name="Поврежден сетевой кабель", comment="", service_id=7),
    Option(name="Иное", comment="", service_id=7),

    Option(name="Охрана", comment="", service_id=8),
    Option(name="Группа быстрого реагирования", comment="", service_id=8),

    Option(name="Регистрация", comment="", service_id=9),
    Option(name="Схема оценок", comment="", service_id=9),
    Option(name="Назначение наставников", comment="", service_id=9),
    Option(name="Формирование команд", comment="", service_id=9),
    Option(name="Назначение аспектов", comment="", service_id=9),
    Option(name="Оценивание", comment="", service_id=9),
    Option(name="Блокировки данных", comment="", service_id=9),
    Option(name="Аналитика и сертификаты", comment="", service_id=9),
    Option(name="иное", comment="", service_id=9),

    Option(name="Уборка компетенции", comment="", service_id=10),
    Option(name="Компетенция не убрана с прошлого дня", comment="", service_id=10),
    Option(name="Требуется уборка прямо сейчас", comment="", service_id=10),

]
