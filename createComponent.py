#!/usr/bin/env python3.10
"""Хелпер для создания React компонентов.
Спрашивает, создаём компонент в components или pages,
затем спрашивает, какой элемент создаём.
Если для pages элемент указываем MyComponent, создаст:
    pages/MyComponent/MyComponent.tsx
    pages/MyComponent/MyComponent.module.css
    pages/MyComponent/index.ts (опционально)
Если указать MyComponent/Element, создаст:
    pages/MyComponent/Element.tsx
    pages/MyComponent/Element.module.css
    pages/MyComponent/index.ts (опционально)
"""
from pathlib import Path
from typing import Literal, TypeAlias, Iterable
from ElementClass import Element
from FileCreator import FileCreator

from TSViewModelCreator import TSViewModelCreator
from TSXCreator import TSXFileCreator
from IndexCreator import IndexFileCreator

SRC_DIR = Path(__file__).parent / "react"

BaseFolder: TypeAlias = Literal["domain", "service", "view"]


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# class CSSFileCreator(FileCreator):
#     """Element.module.css file creator"""
#     def get_absolute_filename(self) -> Path:
#         return self._element.full_path / (self._element.name + ".module.css")

#     def _write_file_contents(self):
#         pass


class AskParams:
    """Ask params from user, parse it and create Element structure"""
    def __init__(self):
        self._element: Element

    def ask(self, folder, name) -> Element:
        """Ask all parameters — element folder and name"""
        # base_folder = self._ask_base_folder()
        # self._element = self._parse_as_element(
        #     self._ask_element(base_folder),
        #     base_folder
        # )
        base_folder = folder
        self._element = self._parse_as_element(name, base_folder)
        return self._element

    def _parse_as_element(self,
            element_str: str,
            base_folder: BaseFolder) -> Element:
        element_as_list = element_str.split("/")
        element_name = element_as_list[-1]
        if len(element_as_list) > 1:
            # user entered: MyCourses/AuthorCourses
            relative_path = "/".join(element_as_list[:-1])
        else:
            # user entered: AuthorCourses
            relative_path = element_name
        return Element(
            full_path=SRC_DIR / base_folder / relative_path,
            name=element_name
        )

    def ask_ok(self, filenames: Iterable[str]) -> None:
        filenames = "\n\t".join(filenames)
        while True:
            print(f"\nИтак, создаём файлы:\n"
                  f"{Colors.HEADER}\t{filenames} {Colors.ENDC}\n\n")
            match input("Ок? [Y]/N: ").strip().lower():
                case "y" | "": return
                case "n": exit("Ок, выходим, ничего не создал.")
                case _: print("Не понял, давай ещё раз.")

    def _ask_base_folder(self) -> BaseFolder:
        while True:
          folder = input("name dir: ")
          return folder
            # match input("d — domain, s — service, v - view: ").strip().lower():
            #     case "d": return "domain"
            #     case "s": return "service"
            #     case "v": return "view"
            #     case _: print("Не понял, давай ещё раз.")

    def _ask_element(self, base_folder: BaseFolder) -> str:
        return input(f"Куда кладём? {base_folder}/").strip()


class ElementFilesCreator:
    """Handles files creation"""
    def __init__(self, element: Element):
        self._element = element
        self._file_creators: list[FileCreator] = []

    def create(self):
        for file_creator in self._file_creators:
            file_creator.create()

    def register_file_creators(self, *file_creators: type[FileCreator]):
        for fc in file_creators:
            self._file_creators.append(fc(
                element=self._element
            ))

    def get_relative_filenames(self) -> tuple[str, ...]:
        return tuple(fc.get_relative_filename() for fc in self._file_creators)


def main():
    asker = AskParams()
    component = input(f"Название компонента? ").strip().lower()
    for folder in ['view', 'domain', 'service']:
      element = asker.ask(folder, component)
      element_creator = ElementFilesCreator(element)
      if folder == 'view':
        element_creator.register_file_creators(
            TSXFileCreator,
            # CSSFileCreator,
            IndexFileCreator,
            TSViewModelCreator
        )
      element_creator.register_file_creators(
            # CSSFileCreator,
            IndexFileCreator
        )
      # asker.ask_ok(element_creator.get_relative_filenames())
      element_creator.create()
    print(f"Всё создал и весь такой молодец!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass