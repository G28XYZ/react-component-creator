def DomainIndex(name):
    nameCapitalize = name.capitalize()
    return f"""
import './{nameCapitalize}SettingsFactory';

export * from './I{nameCapitalize}Settings';
export * from './{nameCapitalize}SettingsFactory';
"""