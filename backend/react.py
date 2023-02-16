from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Post, User, db, React
from flask import request, jsonify



react_ns = Namespace('react', description= "A namespace for React")

# Schema
react_model = react_ns.model(
    "React",
    {
        "id": fields.Integer(),
        "user_id": fields.Integer(),
        "psot_id": fields.Integer(),
        "creted_on": fields.DateTime()
    }
)


@react_ns.route('/react/<int:id>')
class ReactResources(Resource):
    @react_ns.marshal_list_with(react_model)
    @jwt_required()
    def get(self, id):
        react = React.query.get_or_404(id)

        return react

    @react_ns.marshal_with(react_model)
    @react_ns.expect(react_model)
    @jwt_required()
    def post(self, id):
       current_user = get_jwt_identity()
       post = Post.query.get(id)
       new_react= React(user_id = current_user, post=post)
       user = React.query.filter_by(user_id=get_jwt_identity()).first()
       if user:
           user.delete()
       else:
        new_react.save()
        new_react, 201
