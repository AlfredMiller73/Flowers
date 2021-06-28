from django.utils.safestring import mark_safe

class ImageSize:
    def image_show(self, obj):
       if obj.image:
           return mark_safe("<img src='{}' width='50' height='50' />".format(obj.image.url))
       return "None"

    image_show.__name__ = "Картинка"
