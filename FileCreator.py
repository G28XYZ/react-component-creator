from abc import abstractmethod, ABC
from pathlib import Path
from ElementClass import Element

SRC_DIR = Path(__file__).parent / "react"

class FileCreator(ABC):
    def __init__(self, element: Element, option_folder='', ending_file='', start_file='', callback=lambda name:name):
        self._element = element
        self._option_folder = option_folder
        self._ending_file = ending_file
        self._start_file = start_file
        self._callback = callback

    def create(self) -> None:
        """Creates empty file and then fill with contents"""
        self._create_empty_file()
        self._write_file_contents()

    def get_relative_filename(self) -> str:
        """Returns relative filename as str for logging"""
        relative_path_start_index = 1 + len(str(SRC_DIR.resolve()))
        result = str(
            self.get_absolute_filename().resolve()
        )[relative_path_start_index:]
        return result

    def _create_empty_file(self):
        """Init file if not exists"""
        self.get_absolute_filename().parent.mkdir(parents=True, exist_ok=True)
        self.get_absolute_filename().touch(exist_ok=True)

    @abstractmethod
    def get_absolute_filename(self) -> Path:
        """Returns file in Path format"""
        pass

    @abstractmethod
    def _write_file_contents(self) -> None:
        """Fill file with contents"""
        pass