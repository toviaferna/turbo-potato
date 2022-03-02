import logging
import pathlib
from django.contrib.admin.utils import NestedObjects
from django.utils.text import capfirst
from django.utils.encoding import force_text
from os import path
from PIL import Image
import uuid
import os

logger = logging.getLogger(__name__)

def get_deleted_objects(objs):
    """
    get related objects to delete
    """
    collector = NestedObjects(using='default')
    collector.collect(objs)

    def format_callback(obj):
        opts = obj._meta
        no_edit_link = '%s: %s' % (capfirst(opts.verbose_name),
                                   force_text(obj))
        return no_edit_link

    to_delete = collector.nested(format_callback)
    protected = [format_callback(obj) for obj in collector.protected]
    model_count = {model._meta.verbose_name_plural: len(
        objs) for model, objs in collector.model_objs.items()}
    return to_delete, model_count, protected

def create_thumbnail(imagepath: str, basewidth: int, force=False) -> bool:
    thumbfilename = "{}_th{}".format(
        path.splitext(imagepath)[0],
        path.splitext(imagepath)[1],
    )
    if not path.exists(thumbfilename) or force:
        try:
            img = Image.open(imagepath)
            wpercent = basewidth / float(img.size[0])
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            thumbfilename = "{}_th{}".format(
                path.splitext(imagepath)[0],
                path.splitext(imagepath)[1],
            )
            img.save(thumbfilename)
            return True
        except Exception as e:
            logger.error(f"Error creaing thumbnail for {imagepath} - {repr(e)}")
    return False

def rename_img(instance, filename): 
    path = "auth/images/"
    new_filename = uuid.uuid4()
    ext = pathlib.Path(filename).suffix
    return os.path.join(path, "{0}{1}".format(new_filename, ext))