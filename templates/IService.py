def IService(name):
    return f"""
export interface I{name.capitalize()}Service {{
}}
"""