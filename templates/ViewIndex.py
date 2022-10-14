def ViewIndex(name):
    return f"""
import './{name.capitalize()}';

export * from "./{name.capitalize()}ViewModel";
"""