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
