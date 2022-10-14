from pathlib import Path
from FileCreator import FileCreator
from templates.ViewModel import ViewModel

class TSViewModelCreator(FileCreator):
    """Element.css file creator"""
    def get_absolute_filename(self) -> Path:
        return self._element.full_path / (self._element.name.capitalize() + "ViewModel.ts")

    def _write_file_contents(self):
        self.get_absolute_filename().write_text(ViewModel(self._element.name).strip(), encoding='utf-8')