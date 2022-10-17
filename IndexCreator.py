from pathlib import Path
from FileCreator import FileCreator
from templates.ViewIndex import ViewIndex
from templates.ServiceIndex import ServiceIndex
from templates.DomainIndex import DomainIndex
class IndexFileCreator(FileCreator):
    """Optional index.ts file creator"""
    def get_absolute_filename(self) -> Path:
        return self._element.full_path / "index.ts"

    def _write_file_contents(self):
        current_file_contents = self.get_absolute_filename().read_text()
        if current_file_contents.strip():
            print('⛔   файлы уже существуют, ничего не создал ' + str(self._element.full_path))
            return
        print('✔️   создал ' + str(self._element.full_path))
        if 'view' in str(self._element.full_path):
            self.get_absolute_filename().write_text(ViewIndex(self._element.name))
        if 'service' in str(self._element.full_path):
            self.get_absolute_filename().write_text(ServiceIndex(self._element.name))
        if 'domain' in str(self._element.full_path):
            self.get_absolute_filename().write_text(DomainIndex(self._element.name))