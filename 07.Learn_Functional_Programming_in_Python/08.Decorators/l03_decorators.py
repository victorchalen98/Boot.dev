def configure_plugin_decorator(func):
    def wrapper(*args):
        kwargs = dict(args)  
        return func(**kwargs)
    return wrapper

@configure_plugin_decorator
def configure_backups(**kwargs):
    return kwargs

plugin_config = configure_backups(
    ("path", "~/duplicates"),
    ("prefix", "duplicate_"),
    ("extension", ".rtf"),
)

print(plugin_config)
