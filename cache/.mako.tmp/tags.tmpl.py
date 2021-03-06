# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1432159290.982479
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/tags.tmpl'
_template_uri = u'tags.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        cat_items = context.get('cat_items', UNDEFINED)
        title = context.get('title', UNDEFINED)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        hidden_categories = context.get('hidden_categories', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cat_items = context.get('cat_items', UNDEFINED)
        title = context.get('title', UNDEFINED)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        def content():
            return render_content(context)
        hidden_categories = context.get('hidden_categories', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<article class="tagindex">\n    <header>\n        <h1>')
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n    </header>\n')
        if cat_items:
            if items:
                __M_writer(u'            <h2>')
                __M_writer(unicode(messages("Categories")))
                __M_writer(u'</h2>\n')
            __M_writer(u'        <ul class="postlist">\n')
            for text, link in cat_items:
                if text and text not in hidden_categories:
                    __M_writer(u'                <li><a class="reference" href="')
                    __M_writer(unicode(link))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a></li>\n')
            __M_writer(u'        </ul>\n')
            if items:
                __M_writer(u'            <h2>')
                __M_writer(unicode(messages("Tags")))
                __M_writer(u'</h2>\n')
        if items:
            __M_writer(u'        <ul class="postlist">\n')
            for text, link in items:
                if text not in hidden_tags:
                    __M_writer(u'                <li><a class="reference listtitle" href="')
                    __M_writer(unicode(link))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a></li>\n')
            __M_writer(u'        </ul>\n')
        __M_writer(u'</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 0, "39": 2, "44": 34, "50": 4, "62": 4, "63": 7, "64": 7, "65": 9, "66": 10, "67": 11, "68": 11, "69": 11, "70": 13, "71": 14, "72": 15, "73": 16, "74": 16, "75": 16, "76": 16, "77": 16, "78": 19, "79": 20, "80": 21, "81": 21, "82": 21, "83": 24, "84": 25, "85": 26, "86": 27, "87": 28, "88": 28, "89": 28, "90": 28, "91": 28, "92": 31, "93": 33, "99": 93}, "uri": "tags.tmpl", "filename": "/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/tags.tmpl"}
__M_END_METADATA
"""
