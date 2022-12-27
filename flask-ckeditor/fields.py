from markupsafe import Markup, escape
from wtforms.fields import TextAreaField
from wtforms.widgets import html_params


class CKEditorTextAera:
    """
    Renders a CKEditor 'textarea'
    """

    validation_attrs = ["required", "maxlength", "minlength"]

    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        flags = getattr(field, "flags", {})
        for k in dir(flags):
            if k in self.validation_attrs and k not in kwargs:
                kwargs[k] = getattr(flags, k)
        return Markup(
            "<textarea %s>\r\n%s</textarea>"
            % (html_params(name=field.name, **kwargs), escape(field._value()))
        )


class CKEditorField(TextAreaField):
    widget = CKEditorTextAera()
