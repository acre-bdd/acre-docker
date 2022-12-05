import os
from configobj import ConfigObj
from pylogx import log


class Settings:
    @staticmethod
    def read(settings):
        for setting in reversed(settings):
            sp = setting.split(",")
            for st in reversed(sp):
                filename = st.replace(".", "/")
                Settings.read_file(filename)

    @staticmethod
    def read_file(file):
        sf = f"etc/settings/{file}"
        log.debug(f"reading settings file {sf}")
        co = ConfigObj(sf)
        for key, value in co.items():
            if key in os.environ:
                log.warning("key '{key}' already set to {os.environ[key]}, skipping ({value})")
                continue
            os.environ[key] = value
