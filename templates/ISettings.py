def ISettings(name):
    nameCapitalize = name.capitalize()
    return f"""
import {{ IModel }} from "@itcs/react-mvvm"

/** Интерфейс настроек журналов **/
export interface I{nameCapitalize}Settings extends IModel {{
}}
"""