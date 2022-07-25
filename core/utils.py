import logging
import os
import pathlib
import uuid
from os import path

from django.conf import settings
from django.contrib.admin.utils import NestedObjects
from django.contrib.staticfiles import finders
from django.utils.encoding import force_text
from django.utils.text import capfirst
from PIL import Image

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

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path=result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path
