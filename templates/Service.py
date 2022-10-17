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

    @Inject('{name}Api') {name}Api: {nameCapitalize}Api;
    @Inject("{nameCapitalize}SettingsFactory")
    private {name}SettingsFactory: {nameCapitalize}SettingsFactory;
}}
"""