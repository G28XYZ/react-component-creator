def Service(name):
    nameCapitalize = name.capitalize()
    return f"""
import {{ Inject, Service }} from 'typedi';
import {{ {nameCapitalize}Api }} from './ApiHelper/{nameCapitalize}Api';

@Service('{nameCapitalize}Service')
export class {nameCapitalize}Service {{
    @Inject('{name}Api') {name}Api: {nameCapitalize}Api;
}}
"""