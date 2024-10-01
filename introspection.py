def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [at for at in dir(obj) if not callable(getattr(obj, at))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},

    return info


number_info = introspection_info(42)
print(number_info)
print()

string_info = introspection_info('Hello')
print(string_info)
print()

list_info = introspection_info([5, 50, 25.5, 'Hello'])
print(list_info)
