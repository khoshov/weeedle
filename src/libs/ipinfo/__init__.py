"""
    =============================
      Получение информации о IP
    =============================

    Модуль позволяет получить географическую информацию по IP-адресу (IPv4 и IPv6).
    Данные берутся из бесплатных API и сохраняются в локальную базу данных и кэш.


    Установка
    ---------
    Добавить "libs.ipinfo" в INSTALLED_APPS:
        INSTALLED_APPS = [
            ...
            'libs.ipinfo',
        ]

    Опционально, для добавления данных в request.META:
        MIDDLEWARE = [
            'libs.ipinfo.middleware.IPInfoMiddleware',
        ]

    Настройки
    ---------
    IPINFO_CACHE_TIMEOUT
        type            int
        default         24*3600
        description     Количество секунд, в течении которого информация о IP
                        в кэше считается актуальной.

    IPINFO_DB_TIMEOUT
        type            int
        default         7*24*3600
        description     Количество секунд, в течении которого информация о IP
                        в локальной базе данных считается актуальной.

    IPINFO_META_KEY
        type            str
        default         IP_INFO
        description     Ключ записи в request.META в случае, если используется
                        IPInfoMiddleware.

    Пример: получение информации по IP
    ----------------------------------
    from libs.ipinfo.utils import get_info
    info = get_info('195.144.219.29')
    info.city == 'Tolyatti'

    Пример: получение информации из объекта request (необходим модуль django-ipware)
    -----------------------------------------------
    from libs.ipinfo.utils import get_request_info
    info = get_request_info(request)
    info.city == 'Tolyatti'

"""

default_app_config = 'libs.ipinfo.apps.Config'
