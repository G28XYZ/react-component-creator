#!/usr/bin/env python3.10
"""Хелпер для создания React компонентов под архитектуру проекта.
Спрашивает название компонента.
Затем по введённому названию создаст:
    - view
        react/view/MyComponent/index.ts
        react/view/MyComponent/MyComponent.tsx
        react/view/MyComponent/MyComponentViewModel.ts
    - service
        react/service/MyComponent/apiHelper/MyComponentApi.ts
        react/service/MyComponent/index.ts
        react/service/MyComponent/MyComponentService.ts
        react/service/MyComponent/IMyComponentService.ts
    - domain
        react/domain/MyComponent/index.ts
        react/domain/MyComponent/MyComponentSettings.ts
        react/domain/MyComponent/IMyComponentSettings.ts
        react/domain/MyComponent/MyComponentSettingsFactory.ts

для запуска скрипта перейди в папку c компонентом в котором нужно создать/добавить папку react с компонентами
например: webgui_frontend_app_react\packages\local\SystemSettings
закинь туда файл react-creator.py
в консоли запусти его командой: python -B react-creator.py

Примечание: нейминг компонента будет создан в CamelCase,
            но только пока по первому знаку из введенного названия.
            Например reboot -> Reboot
"""

from pathlib import Path
from typing import Literal, TypeAlias
from Creator import Creator
from ElementClass import Element
from FileCreator import FileCreator

from templates.main import TSX, ApiHelper, DomainIndex, IService, ISettings, Service, ServiceIndex, Settings, SettingsFactory, Urls, ViewIndex, ViewModel


SRC_DIR = Path(__file__).parent / "react"

BaseFolder: TypeAlias = Literal["domain", "service", "view"]

FolderOptions = {
    'view': [
        {'option_folder': '', 'callback': TSX, 'ending_file': '.tsx', 'start_file': ''},
        {'option_folder': '', 'callback': ViewModel, 'ending_file': 'ViewModel.ts', 'start_file': ''},
        {'option_folder': '', 'callback': ViewIndex, 'ending_file': 'index.ts', 'start_file': ''},
    ],
    'service': [
        {'option_folder': '', 'callback': Service, 'ending_file': 'Service.ts', 'start_file': ''},
        {'option_folder': '', 'callback': IService, 'ending_file': 'Service.ts', 'start_file': 'I'},
        {'option_folder': '../apiHelper', 'callback': ApiHelper, 'ending_file': 'Api.ts', 'start_file': ''},
        {'option_folder': '../apiHelper/urls', 'callback': Urls, 'ending_file': 'Urls.ts', 'start_file': ''},
        {'option_folder': '', 'callback': ServiceIndex, 'ending_file': 'index.ts', 'start_file': ''},
    ],
    'domain': [
        {'option_folder': '', 'callback': Settings, 'ending_file': 'Settings.ts', 'start_file': ''},
        {'option_folder': '', 'callback': ISettings, 'ending_file': 'Settings.ts', 'start_file': 'I'},
        {'option_folder': '', 'callback': SettingsFactory, 'ending_file': 'SettingsFactory.ts', 'start_file': ''},
        {'option_folder': '', 'callback': DomainIndex, 'ending_file': 'index.ts', 'start_file': ''},
    ],
}
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

class AskParams:
    def __init__(self):
        self._element: Element

    def ask(self, folder, name) -> Element:
        base_folder = folder
        self._element = self._parse_as_element(name, base_folder)
        return self._element

    def _parse_as_element(self,
            element_str: str,
            base_folder: BaseFolder) -> Element:
        element_as_list = element_str.split("/")
        element_name = element_as_list[-1]
        if len(element_as_list) > 1:
            relative_path = "/".join(element_as_list[:-1])
        else:
            relative_path = element_name
        return Element(
            full_path=SRC_DIR / base_folder / relative_path,
            name=element_name
        )

class ElementFilesCreator:
    def __init__(self, element: Element):
        self._element = element
        self._file_creators: list[FileCreator] = []

    def create(self):
        for file_creator in self._file_creators:
            file_creator.create()

    def register_file_creators(self, options: type[FileCreator]):
        for option in options:
            self._file_creators.append(Creator(
                element=self._element,                  # Подготовленный элемент под создание файла
                option_folder=option['option_folder'],  # Опциональный каталог
                ending_file=option['ending_file'],      # Окончание в названии файла
                start_file=option['start_file'],        # Приставка в названии файла
                callback=option['callback'],            # Функция с шаблоном внутреннего кода файла
            ))

    def get_relative_filenames(self) -> tuple[str, ...]:
        return tuple(fc.get_relative_filename() for fc in self._file_creators)

def main():
    asker = AskParams()
    component = input(f"{Colors.OKBLUE}Название компонента:   {Colors.HEADER}").strip().lower()
    for folder, options in FolderOptions.items():
        # Записать введенное название компонента и название каталога folder
        element = asker.ask(folder, component)
        # Создать элемент для будущего файла
        element_creator = ElementFilesCreator(element)
        # Собрать все опции по файлу через options
        element_creator.register_file_creators(options)
        # Создать файл
        element_creator.create()
    print(f"{Colors.OKGREEN}Всё создал и весь такой молодец!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass