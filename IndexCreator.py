from pathlib import Path
from FileCreator import FileCreator

class IndexFileCreator(FileCreator):
    """Optional index.ts file creator"""
    def get_absolute_filename(self) -> Path:
        return self._element.full_path / "index.ts"

    def _write_file_contents(self):
        current_file_contents = self.get_absolute_filename().read_text()
        if current_file_contents.strip():
            return
        self.get_absolute_filename().write_text(
            f"""export {{default}} from "./{self._element.name}";"""
        )