from pathlib import Path
from FileCreator import FileCreator
from templates.TSX import TSX

class TSXFileCreator(FileCreator):
    """Element.tsx file creator"""
    def get_absolute_filename(self) -> Path:
        return self._element.full_path / (self._element.name.capitalize() + ".tsx")

    def _write_file_contents(self):
        self.get_absolute_filename().write_text(TSX(self._element.name).strip())