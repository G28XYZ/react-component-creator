from pathlib import Path
from FileCreator import FileCreator
from templates.SettingsFactory import SettingsFactory

class SettingsFactoryCreator(FileCreator):
    """SettingsFactory file creator"""
    def get_absolute_filename(self) -> Path:
        return self._element.full_path / (self._element.name.capitalize() + "SettingsFactory.ts")

    def _write_file_contents(self):
        self.get_absolute_filename().write_text(SettingsFactory(self._element.name).strip(), encoding='utf-8')