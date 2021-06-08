from flask import request, render_template, make_response
from flask_restplus import Namespace, Resource, reqparse

namespace = Namespace(
    'jinja_template',
    'Jinja Template page. Note that this is a html page and not a REST API endpoint')

parser = reqparse.RequestParser()
parser.add_argument('top', type=str, help='Top text')
parser.add_argument('bottom', type=str, help='Bottom text')


@namespace.route('')
class JinjaTemplate(Resource):

    @namespace.response(200, 'Render jinja template')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(parser)
    def get(self):
        '''Render jinja template page'''

        top = request.args.get('top') if 'top' in request.args else ''
        bottom = request.args.get('bottom') if 'bottom' in request.args else ''

        return make_response(render_template('example.html', top=top, bottom=bottom), 200)
