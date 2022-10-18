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
        react/service/MyComponent/apiHelper/urls/MyComponentUrls.ts
        react/service/MyComponent/index.ts
        react/service/MyComponent/MyComponentService.ts
        react/service/MyComponent/IMyComponentService.ts
    - domain
        react/domain/MyComponent/index.ts
        react/domain/MyComponent/MyComponentSettings.ts
        react/domain/MyComponent/IMyComponentSettings.ts
        react/domain/MyComponent/MyComponentSettingsFactory.ts

для запуска скрипта перейди в папку c компонентом в котором нужно создать/добавить папку react с компонентами
например: webgui_frontend_app_react/packages/local/SystemSettings
закинь туда файл react-creator.py
в консоли запусти его командой: python -B react-creator.py

Примечание: нейминг компонента будет создан в CamelCase,
            но только пока по первому знаку из введенного названия.
            Например reboot -> Reboot
"""


from abc import abstractmethod, ABC
from pathlib import Path
from typing import Literal, TypeAlias
from dataclasses import dataclass

SRC_DIR = Path(__file__).parent / "react"

BaseFolder: TypeAlias = Literal["domain", "service", "view"]

def ApiHelper(name):
    nameCapitalize = name.capitalize()
    return f"""
import {{ Inject, Service }} from "typedi";

import {{ RequestFactory }} from "../../../../Core/react/service/api/RequestFactory";
import {{ RequestMethod }} from "../../../../Core/react/service/api";
import * as Urls from "./urls";

/** Сервис api, инкапсулирующий запросы к серверу **/
@Service("{nameCapitalize}Api")
export class {nameCapitalize}Api {{
  @Inject("RequestFactory")
  private requestFactory: RequestFactory;
}}
"""

def DomainIndex(name):
    nameCapitalize = name.capitalize()
    return f"""
import './{nameCapitalize}SettingsFactory';

export * from './I{nameCapitalize}Settings';
export * from './{nameCapitalize}SettingsFactory';
"""

def IService(name):
    nameCapitalize = name.capitalize()
    return f"""
import {{ I{nameCapitalize}Settings }} from "../../domain/{name}";

/** Интерфейс сервиса для настроек **/
export interface I{name.capitalize()}Service {{
    /** Загрузить Настройки **/
    load{nameCapitalize}Settings(): Promise<void>;

    /** Получить Настройки **/
    get{nameCapitalize}Settings(): I{nameCapitalize}Settings;
}}
"""
def ISettings(name):
    nameCapitalize = name.capitalize()
    return f"""
import {{ IModel }} from "@itcs/react-mvvm"

/** Интерфейс настроек **/
export interface I{nameCapitalize}Settings extends IModel {{
}}
"""

def Service(name):
    nameCapitalize = name.capitalize()
    return f"""
import {{ Inject, Service }} from 'typedi';
import {{ {nameCapitalize}Api }} from '../apiHelper/{nameCapitalize}Api';
import {{ I{nameCapitalize}Settings, {nameCapitalize}SettingsFactory }} from "../../domain/{name}";
import * as Urls from "../apiHelper/urls";

@Service('{nameCapitalize}Service')
export class {nameCapitalize}Service implements I{nameCapitalize}Service {{
    private {name}Settings: I{nameCapitalize}Settings;

    // Получить настройки
    get{nameCapitalize}Settings() {{
        return this.{name}Settings;
    }}

    // Загрузить настройки
    async load{nameCapitalize}Settings() {{
        try {{
            const {{ ...data }} = this.{name}SettingsFactory.create{nameCapitalize}Settings(
                await this.{name}Api.get{nameCapitalize}Settings()
            );
        this.{name}Settings = {{...data}};
        }} catch (e) {{
            throw new Error();
        }}
    }}

    @Inject('{nameCapitalize}Api') {name}Api: {nameCapitalize}Api;
    @Inject("{nameCapitalize}SettingsFactory")
    private {name}SettingsFactory: {nameCapitalize}SettingsFactory;
}}
"""

def ServiceIndex(name):
    return f"""
import './{name.capitalize()}Service';

export * from "./I{name.capitalize()}Service";
"""

def Settings(name):
    nameCapitalize = name.capitalize()
    return f"""
import {{ Model, DataField }} from "@itcs/react-mvvm";

import {{ I{nameCapitalize}Settings }} from "./I{nameCapitalize}Settings";

/** Модель, описывающая настройки **/
export class {nameCapitalize}Settings extends Model implements I{nameCapitalize}Settings {{
    @DataField [key:string]: any;
}}
"""

def SettingsFactory(name):
    nameCapitalize = name.capitalize()
    return f"""
import {{ Service }} from "typedi";

import {{ I{nameCapitalize}Settings }} from "./I{nameCapitalize}Settings";
import {{ {nameCapitalize}Settings }} from "./{nameCapitalize}Settings";

/** Фабрика настроек **/
@Service("{nameCapitalize}SettingsFactory")
export class {nameCapitalize}SettingsFactory {{
  /**
   * Создать экземпляр настроек
   * @param data Данные, полученные с сервера.
   */
  create{nameCapitalize}Settings(data: any): I{nameCapitalize}Settings {{
    return {nameCapitalize}Settings.create(data);
  }}
}}
"""

def TSX(name):
    nameCapitalize = name.capitalize()
    return f"""
import React, {{ FC }} from "react";
import {{ view, ViewProps, ViewType }} from "@itcs/react-mvvm";
import {{ {nameCapitalize}ViewModel }} from "./{nameCapitalize}ViewModel";

interface {nameCapitalize}Props extends ViewProps<{nameCapitalize}ViewModel> {{
    viewModel: {nameCapitalize}ViewModel;
}}

export const {nameCapitalize}: FC<{nameCapitalize}Props> = () => {{
    return (
        <ExtPortal extComponentId={{"{name}React"}}>
            <{nameCapitalize}Component />
        </ExtPortal>
        )
}};

const {name}: FC<{nameCapitalize}Props> = ({{ viewModel }}) => {{
    return <></>
}};

const {nameCapitalize}Component: ViewType<{nameCapitalize}Props> = React.memo(view("{nameCapitalize}ViewModel")({name} as FC));
"""

def ViewIndex(name):
    return f"""
import './{name.capitalize()}ViewModel';

export * from "./{name.capitalize()}";
"""

def ViewModel(name):
    return f"""
import {{ observable }} from 'mobx';
import {{ Inject, Service }} from 'typedi';
import {{ ViewModel }} from '@itcs/react-mvvm';
import {{ {name.capitalize()}Service }} from '../../service/{name}/{name.capitalize()}Service';

@Service('{name.capitalize()}ViewModel')
export class {name.capitalize()}ViewModel extends ViewModel {{
    /** Глобальный объект App */
    app = (window.globalThis as any).App
    /** Признак прав пользователя **/
    @observable isAdmin: boolean = this.app.getMainView().getViewModel().get().isAdmin;

    /** Инициализация ViewModel */
    protected onInit() {{}}

    @Inject('{name.capitalize()}Service') {name}Service: {name.capitalize()}Service;
}}
"""

def Urls(name):
    return f"""
export default {{
    {name}: cgi_rest_service_url ? cgi_rest_service_url + '' : '/services/'
}}
"""

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


SRC_DIR = Path(__file__).parent / "react"

@dataclass
class Element:
    full_path: Path
    name: str

class FileCreator(ABC):
    def __init__(self, element: Element, option_folder='', ending_file='', start_file='', callback=lambda name:name):
        self._element = element
        self._option_folder = option_folder
        self._ending_file = ending_file
        self._start_file = start_file
        self._callback = callback

    def create(self) -> None:
        """Creates empty file and then fill with contents"""
        self._create_empty_file()
        self._write_file_contents()

    def get_relative_filename(self) -> str:
        """Returns relative filename as str for logging"""
        relative_path_start_index = 1 + len(str(SRC_DIR.resolve()))
        result = str(
            self.get_absolute_filename().resolve()
        )[relative_path_start_index:]
        return result

    def _create_empty_file(self):
        """Init file if not exists"""
        self.get_absolute_filename().parent.mkdir(parents=True, exist_ok=True)
        self.get_absolute_filename().touch(exist_ok=True)

    @abstractmethod
    def get_absolute_filename(self) -> Path:
        """Returns file in Path format"""
        pass

    @abstractmethod
    def _write_file_contents(self) -> None:
        """Fill file with contents"""
        pass


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

    def register_file_creators(self, options):
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