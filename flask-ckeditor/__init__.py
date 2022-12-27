from typing import Union, Literal

from flask import Flask, Markup, Blueprint, render_template
from .fields import CKEditorField


class CKEditor:

    app: Flask = None
    serve_local: bool = False
    editor_type: Literal['classic ', 'inline', 'balloon', 'balloon-block', 'decoupled-document'] = 'classic'
    enable_csrf: bool = None
    enable_csp_nonce: bool = None
    upload_endpoint: str = None
    lenguage: str = None
    license_key: str = None

    def __init__(self, app: Flask = None) -> None:
        if app:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['ckeditor'] = self

        blueprint = Blueprint('ckeditor', __name__, template_folder='templates', static_url_path='/ckeditor' + app.static_url_path)
        app.register_blueprint(blueprint)

        self.app = app
        self.license_key = app.config.get('CKEDITOR_LICENSE_KEY', None)
        self.editor_type = app.config.get('CKEDITOR_EDITOR_TYPE', 'classic')
        self.local_path = app.config.get('CKEDITOR_LOCAL_PATH', None)
        self.lenguage = app.config.get('CKEDITOR_LANGUAGE', None)
        self.enable_csrf = app.config.get('CKEDITOR_ENABLE_CSRF', None)
        self.upload_endpoint = app.config.get('CKEDITOR_UPLOAD_ENDPOINT', None)

        @app.context_processor
        def inject_context_variables() -> dict:
            return dict(ckeditor=self)
    
    def load(self, editor_type: str = None, 
             local_path: bool = False, 
             enable_csp_nonce: bool = False, version='35.4.0'):
        
        return Markup(render_template('load_ckeditor.jinja', 
                                      version=version,
                                      editor_type=editor_type or self.editor_type,
                                      local_path=local_path or self.local_path,
                                      csp_enabled=enable_csp_nonce or self.enable_csp_nonce
                                      ))

    def config(self, target: Union[CKEditorField, str], use_htmx: bool = None,
               upload_endpoint: str = None, enable_csrf: bool = None, 
               editor_type: str = None):
        target_id = target if isinstance(target, str) else target.name

        return Markup(render_template('config_target.jinja',
                                     target_id=target_id,
                                     editor_type=editor_type or self.editor_type,
                                     use_htmx=use_htmx,
                                     upload_endpoint=upload_endpoint or self.upload_endpoint,
                                     enable_csrf=enable_csrf or self.enable_csrf))
