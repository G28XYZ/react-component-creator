from pathlib import Path
from FileCreator import FileCreator
from templates.Settings import Settings

class SettingsCreator(FileCreator):
    """Settings file creator"""
    def get_absolute_filename(self) -> Path:
        return self._element.full_path / (self._element.name.capitalize() + "Settings.ts")

    def _write_file_contents(self):
        self.get_absolute_filename().write_text(Settings(self._element.name).strip(), encoding='utf-8')