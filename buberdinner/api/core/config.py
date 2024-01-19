import functools

from buberdinner.api.core.settings.app import AppSettings
from buberdinner.api.core.settings.base import AppEnvTypes, BaseAppSettings
from buberdinner.api.core.settings.development import DevAppSettings
from buberdinner.api.core.settings.production import ProdAppSettings
from buberdinner.api.core.settings.test import TestAppSettings

environments: dict[AppEnvTypes, type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
    AppEnvTypes.test: TestAppSettings,
}


@functools.lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()
