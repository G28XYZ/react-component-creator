from pathlib import Path
from FileCreator import FileCreator

class Creator(FileCreator):
    def get_absolute_filename(self) -> Path:
        if self._ending_file == 'index.ts':
           return self._element.full_path / self._option_folder / self._ending_file
        return self._element.full_path / self._option_folder / (self._start_file + self._element.name.capitalize() + self._ending_file)

    def _write_file_contents(self):
        current_file_contents = self.get_absolute_filename().read_text()
        if current_file_contents.strip():
            print('⛔ файл уже существуют, ничего не создал ' + str(self.get_absolute_filename()))
            return
        print('✔️ создал ' + str(self.get_absolute_filename()))
        self.get_absolute_filename().write_text(self._callback(self._element.name), encoding='utf-8')