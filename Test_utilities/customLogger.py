import logging
import os

class logGen:
    @staticmethod
    def logger():
        # Определение пути к файлу логов
        log_directory = os.path.join(os.path.dirname(__file__), "../Logs")
        log_file = os.path.join(log_directory, "automation.log")

        # Убедитесь, что директория существует
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Настройка логирования
        logging.basicConfig(filename=log_file,
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p",
                            level=logging.INFO,  # Используем один уровень логирования
                            force=True)  # Перезапись конфигурации, если нужно

        logger = logging.getLogger()
        return logger
