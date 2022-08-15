import click
from config.logger import get_logger
from salmorejo.service import Manager
from . import get_callback_from_script, get_set_k8s_objects_from_str

logger = get_logger()

@click.group()
def root():
    '''
    Simple CLI
    '''
    print("\nSalmorejo is on its way !!")      

@root.command(name='watch', help='watching objects after providing the path of the python script which contains the function `callback(object)` and the comma-separated-string with the desired kubernetes objects (i.e. `watch /home/scripts/my_script.py pods,services)')
@click.argument('callback_path', type=click.Path(exists=True))
@click.argument('k8s_objects')
def watch(callback_path, k8s_objects):
    try:
        callback = get_callback_from_script(callback_path)
        objects = get_set_k8s_objects_from_str(k8s_objects)
        Manager(callback, objects).start()
    except Exception as e:
        logger.error(f"error: {e}")
