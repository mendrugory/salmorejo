from importlib.machinery import SourceFileLoader
from k8s.watcher import is_object_allowed

def get_callback_from_script(path):
    module = SourceFileLoader("module", path).load_module()
    return module.callback
    
def get_set_k8s_objects_from_str(objects_str):
    objects = objects_str.replace(" ", "").split(",")
    non_allowed_objects = tuple((o for o in objects if not is_object_allowed(o)))
    
    if non_allowed_objects:
        error_message = _get_non_allowed_objects_error_message(non_allowed_objects)
        raise Exception(error_message)
    
    return set(objects)

def _get_non_allowed_objects_error_message(non_allowed_objects):
    if len(non_allowed_objects) == 1:
        return f"{non_allowed_objects[0]} is not supported"

    return f"{','.join(non_allowed_objects)} are not supported"