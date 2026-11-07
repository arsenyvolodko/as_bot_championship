from as_bot_championship.db.tables import Location, Option, Service, Hall

halls = [
    *[Hall(name=f"Павильон №{num}") for num in range(1, 4)]
]

locations = [
    Location(name="Электромонтаж", hall_id=1),
    Location(name="Фрезерные работы на станках ЧПУ", hall_id=1),
    Location(name="Токарные работы на станках ЧПУ", hall_id=1),
    Location(name="Слесарные работы с металлом", hall_id=1),
    Location(name="Сварочные технологии", hall_id=1),
    Location(name="Бережливое производство", hall_id=1),
    Location(name="Системы связи БАС", hall_id=1),
    Location(name="Аддитивное производство и обратный инжиниринг", hall_id=1),
    Location(name="Технологии композитов", hall_id=1),
    Location(name="Технологии ИИ в комплексных беспилотных системах (БАС)", hall_id=1),
    Location(name="Проектирование, конструирование и производственная инженерия БАС", hall_id=1),
    Location(name="Летающая робототехника (БАС)", hall_id=1),
    Location(name="Эксплуатация беспилотных авиационных систем (БАС)", hall_id=1),

    Location(name="Цифровая метрология", hall_id=2),
    Location(name="Промышленный дизайн", hall_id=2),
    Location(name="Охрана труда", hall_id=2),
    Location(name="Неразрушающий контроль", hall_id=2),
    Location(name="Цифровая трансформация", hall_id=2),
    Location(name="Цифровая подстанция", hall_id=2),
    Location(name="Управление персоналом", hall_id=2),
    Location(name="Теория решения изобретательских задач (ТРИЗ)", hall_id=2),
    Location(name="Сетевое и системное администрирование (СиСА)", hall_id=2),
    Location(name="Рационализация процессов проведения испытаний изделий приборостроения", hall_id=2),
    Location(name="Монтажник радиоэлектронной аппаратуры и приборов", hall_id=2),
    Location(name="Магистральные линии связи. Строительство и эксплуатация ВОЛП", hall_id=2),
    Location(name="Корп. защита от внутренних угроз информационной безопасности", hall_id=2),
    Location(name="Квантовые технологии", hall_id=2),
    Location(name="Инженерия космических систем", hall_id=2),
    Location(name="Инженер технолог машиностроения", hall_id=2),
    Location(name="Инженер по расчету прочности", hall_id=2),
    Location(name="Изготовление прототипов", hall_id=2),

    Location(name="Управление жизненным циклом (управление программой)", hall_id=3),
    Location(name="Сметное дело", hall_id=3),
    Location(name="Роботизация и автоматизация технологических процессов, сварочные технологии (Демо)", hall_id=3),
    Location(name="Разработка и внедрение ИИ-решений", hall_id=3),
    Location(name="Промышленная экология (проект химия)", hall_id=3),
    Location(name="Промышленная робототехника", hall_id=3),
    Location(name="Охрана окружающей среды", hall_id=3),
    Location(name="Машинное обучение и большие данные", hall_id=3),
    Location(name="Информационная безопасность", hall_id=3),
    Location(name="Инженерный дизайн CAD", hall_id=3),
    Location(name="Аппаратчик химических производств/технологий (проект химия)", hall_id=3),
    Location(name="Автоматизация бизнес процессов", hall_id=3),
    Location(name="Электроника", hall_id=3),
    Location(name="Цифровое бережливое производство", hall_id=3),
    Location(name="Управление коммуникациями", hall_id=3),
    Location(name="Управление качеством", hall_id=3),
    Location(name="Промышленная автоматика", hall_id=3),
    Location(name="Обслуживание и ремонт оборудования релейной защиты и автоматики", hall_id=3),
    Location(name="Лаб. хим. анализ", hall_id=3),
    Location(name="Автоматизация технологических процессов и производств (Мехатроника)", hall_id=3),
    Location(name="Организация производства изделий из полимеров (проект химия)", hall_id=3),
]

services = [
    Service(name="Обеспеч. компетенции (ЭКСПО)", chat_id=-1004341939486),  # service_id = 1
    Service(name="Обеспеч. компетенции (СКЛАД - Для РОСАТОМА)", chat_id=-1004477091259),  # service_id = 2
    Service(name="Застройка", chat_id=-1004431139187),  # service_id = 3
    Service(name="Электрика", chat_id=-1004392373507),  # service_id = 4
    Service(name="Вода, Вентиляция, канализация, сжатый воздух", chat_id=-1003804396391),  # service_id = 5
    Service(name="ИТ - Компьютеры, сеть и интернет (Для Росатома)", chat_id=-1004300694748),  # service_id = 6
    Service(name="Безопасность", chat_id=-1004385457272),  # service_id = 7
    Service(name="Уборка", chat_id=-1004447080126),  # service_id = 8
]

options = [
    Option(name="Не хватает ТВ", comment="", service_id=1),
    Option(name="Не хватает мебели", comment="", service_id=1),
    Option(name="Не хватает принтера/-ов", comment="", service_id=1),
    Option(name="Иное", comment="", service_id=1),

    Option(name="Расходные материалы", comment="", service_id=2),
    Option(name="Инструменты", comment="", service_id=2),
    Option(name="Канцелярские товары", comment="", service_id=2),
    Option(name="Несоответствие оборудования Илу", comment="", service_id=2),
    Option(name="Иное", comment="", service_id=2),

    Option(name="Проблемы со стенами", comment="", service_id=3),
    Option(name="Дверь не закрывается / не открывается", comment="", service_id=3),
    Option(name="Сломанная мебель", comment="", service_id=3),
    Option(name="Иное", comment="", service_id=3),

    Option(name="Пропало электричество в розетке 220V", comment="", service_id=4),
    Option(name="Пропало электричество в розетках 380V", comment="", service_id=4),
    Option(name="Установить дополнительные розетки", comment="", service_id=4),
    Option(name="Вызов инженера-электрика для подключения или переподключения оборудования.", comment="", service_id=4),
    Option(name="Иное", comment="", service_id=4),

    Option(name="Проблемы с вентиляцией", comment="", service_id=5),
    Option(name="Проблема со сжатым воздухом", comment="", service_id=5),
    Option(name="Проблема с водой / канализацией", comment="", service_id=5),
    Option(name="иное", comment="", service_id=5),

    Option(name="Не хватает ПК, Экранов, иного оборудования", comment="", service_id=6),
    Option(name="Проблемы с ПК", comment="", service_id=6),
    Option(name="Проблемы с проводной сетью", comment="", service_id=6),
    Option(name="Проблемы с WI-FI", comment="", service_id=6),
    Option(name="Поврежден сетевой кабель", comment="", service_id=6),
    Option(name="Иное", comment="", service_id=6),

    Option(name="Охрана", comment="", service_id=7),
    Option(name="Группа быстрого реагирования", comment="", service_id=7),
    Option(name="иное", comment="", service_id=7),

    Option(name="Уборка компетенции", comment="", service_id=8),
    Option(name="Компетенция не убрана с прошлого дня", comment="", service_id=8),
    Option(name="Требуется уборка на компетенции прямо сейчас", comment="", service_id=8),
]
