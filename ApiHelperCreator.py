from pathlib import Path
from FileCreator import FileCreator
from templates.ApiHelper import ApiHelper

class ApiHelperCreator(FileCreator):
    """ApiHelper file creator"""
    def get_absolute_filename(self) -> Path:
        return self._element.full_path / "../apiHelper" /(self._element.name.capitalize() + "Api.ts")

    def _write_file_contents(self):
        self.get_absolute_filename().write_text(ApiHelper(self._element.name).strip(), encoding='utf-8')