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