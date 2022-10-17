def ViewIndex(name):
    return f"""
import './{name.capitalize()}ViewModel';

export * from "./{name.capitalize()}";
"""