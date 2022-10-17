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