from flask_assets import Environment, Bundle


#: application css bundle
css_main = Bundle("css/kgraph.css",
                 "js/graph/css/graph.css")



#: consolidated css bundle
css_lib = Bundle("bower_components/bootstrap/dist/css/bootstrap.min.css")

#: vendor js bundle
js_vendor = Bundle("bower_components/jquery/dist/jquery.js",
                   "bower_components/bootstrap/dist/js/bootstrap.js",
                   "bower_components/angular/angular.js",
                   "bower_components/angular-route/angular-route.js",
                   "bower_components/angular-resource/angular-resource.js",
                   "bower_components/lodash/dist/lodash.js",
                   "bower_components/graphlib/dist/graphlib.core.js",
                   "bower_components/d3/d3.js",
                   "bower_components/dagre/dist/dagre.core.js",
                   "bower_components/dagre-d3/dist/dagre-d3.core.js",
                   )

#: application js bundle
js_main = Bundle("js/**/*.js",
                "js/*.js")


def init_app(app):
    webassets = Environment(app)
    webassets.register('css_all', css_lib)
    webassets.register('css_main', css_main)
    webassets.register('js_vendor', js_vendor)
    webassets.register('js_main', js_main)
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug