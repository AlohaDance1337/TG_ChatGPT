from configparser import ConfigParser


def get_token(section: str) -> str:
    config = ConfigParser()
    config.read(r"E:\Программирование\Парсер_Kwork\bot\core\config.ini")
    return config[section]["TG_Bot"]
