def ServiceIndex(name):
    return f"""
import './{name.capitalize()}Service';

export * from "./I{name.capitalize()}Service";
"""