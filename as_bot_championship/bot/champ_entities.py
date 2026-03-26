from as_bot_championship.db.tables import Location, Option, Service, Hall

halls = [
    *[Hall(name=f"Павильон №{num}") for num in range(1, 4)]
]

locations = [
    Location(name="Технологии композитов", hall_id=1),
    Location(name="Промышленная механика", hall_id=1),
    Location(name="Сварочные технологии", hall_id=1),
    Location(name="Аддитивные технологии", hall_id=1),
    Location(name="Бетонные работы", hall_id=1),
    Location(name="Прототипы", hall_id=1),
    Location(name="Электромонтаж", hall_id=1),
    Location(name="Водитель спец. автомобиля", hall_id=1),
    Location(name="Промавтоматика", hall_id=1),
    Location(name="Электроника", hall_id=1),
    Location(name="Каракури", hall_id=1),
    Location(name="Разработка бизнесс процессов", hall_id=1),

    Location(name="Квантовые технологии", hall_id=2),
    Location(name="Охрана труда", hall_id=2),
    Location(name="Охрана окружающей среды", hall_id=2),
    Location(name="Неразрушающий контроль", hall_id=2),
    Location(name="Математическое моделировнаие", hall_id=2),
    Location(name="Вывод из эксплуатации", hall_id=2),
    Location(name="Инженер технолог", hall_id=2),
    Location(name="Инженерное проектирование", hall_id=2),
    Location(name="ПСР", hall_id=2),
    Location(name="Инженер конструктор", hall_id=2),
    Location(name="ТСЭО", hall_id=2),
    Location(name="Строительный контроль", hall_id=2),
    Location(name="Программная роботизация", hall_id=2),

    Location(name="Мехатроника", hall_id=3),
    Location(name="Корп.защита", hall_id=3),
    Location(name="ПРБ", hall_id=3),
    Location(name="Сметное дело", hall_id=3),
    Location(name="Управление коммуникациями", hall_id=3),
    Location(name="Геодезия", hall_id=3),
    Location(name="Графический дизайн", hall_id=3),
    Location(name="СИСА", hall_id=3),
    Location(name="РЗА", hall_id=3),
    Location(name="УЖЦ", hall_id=3),
    Location(name="Управление качеством", hall_id=3),
    Location(name="ЛХА", hall_id=3),
    Location(name="Радиационный контроль", hall_id=3),
    Location(name="Информационная безопасность", hall_id=3),
    Location(name="Машинное обучение", hall_id=3),
]

services = [
    Service(name="Обеспечение компетенции", chat_id=-1003713437737),  # service_id = 1
    Service(name="Застройка", chat_id=-1003802105205),  # service_id = 2
    Service(name="Электрика", chat_id=-1003774380183),  # service_id = 3
    Service(name="Питьевая вода", chat_id=-1003758010670),  # service_id = 4
    Service(name="Вода, Вентиляция, канализация, сжатый воздух", chat_id=-1003650680014),  # service_id = 5
    Service(name="Мебель и обеспечение компетенции", chat_id=-1003846328914),  # service_id = 6
    Service(name="ИТ - Компьютеры, сеть и интернет", chat_id=-1003722525312),  # service_id = 7
    Service(name="Безопасность", chat_id=-1003879387133),  # service_id = 8
    Service(name="Цифровая платформа", chat_id=-1003709176704),  # service_id = 9
    Service(name="Уборка", chat_id=-1003702161283),  # service_id = 10
]

options = [
    Option(name="Расходные материалы", comment="", service_id=1),
    Option(name="Инструменты", comment="", service_id=1),
    Option(name="Канцелярские товары", comment="", service_id=1),
    Option(name="Несоответствие оборудования Илу", comment="", service_id=1),
    Option(name="Проблема с ТВ", comment="", service_id=1),
    Option(name="Проблема со звуком\микрофоном", comment="", service_id=1),
    Option(name="Проблема с принтером", comment="", service_id=1),
    Option(name="Компьютеры, мониторы, ИТ-техника", comment="", service_id=1),
    Option(name="Установка ПО", comment="", service_id=1),
    Option(name="Иное", comment="", service_id=1),

    Option(name="Проблемы со стенами", comment="", service_id=2),
    Option(name="Дверь не закрывается / не открывается", comment="", service_id=2),

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
    Option(name="Иное", comment="", service_id=5),

    Option(name="Нехватка мебели", comment="", service_id=6),
    Option(name="Несоответствующая мебель", comment="", service_id=6),
    Option(name="Сломанная мебель", comment="", service_id=6),
    Option(name="Иное", comment="", service_id=6),

    Option(name="Проблемы с компьютерами", comment="", service_id=7),
    Option(name="Проблемы с ПО", comment="", service_id=7),
    Option(name="Проблемы с проводной сетью", comment="", service_id=7),
    Option(name="Проблемы с wi-fi", comment="", service_id=7),
    Option(name="Поврежден сетевой кабель", comment="", service_id=7),
    Option(name="Иное", comment="", service_id=7),

    Option(name="Охрана", comment="", service_id=8),
    Option(name="Группа быстрого реагирования", comment="", service_id=8),
    Option(name="Иное", comment="", service_id=8),

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
