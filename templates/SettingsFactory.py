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