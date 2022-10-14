from pathlib import Path
from FileCreator import FileCreator
from templates.IService import IService

class IServiceCreator(FileCreator):
    """IService file creator"""
    def get_absolute_filename(self) -> Path:
        return self._element.full_path / ("I" + self._element.name.capitalize() + "Service.ts")

    def _write_file_contents(self):
        self.get_absolute_filename().write_text(IService(self._element.name).strip(), encoding='utf-8')