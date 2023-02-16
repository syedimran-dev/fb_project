from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Post, User, db, React, Comment
from flask import request, jsonify



comment_ns = Namespace('comment', description= "A namespace for Comment")

# Schema
comment_model = comment_ns.model(
    "Comment",
    {
        "id": fields.Integer(),
        "user_id": fields.Integer(),
        "psot_id": fields.Integer(),
        "comment": fields.String(),
        "creted_on": fields.DateTime()
    }
)


@comment_ns.route('/comment/<int:id>')
class ReactResources(Resource):
    @comment_ns.marshal_list_with(comment_model)
    @jwt_required()
    def get(self, id):
        comment = Comment.query.get_or_404(id)

        return comment

    @comment_ns.marshal_with(comment_model)
    @comment_ns.expect(comment_model)
    @jwt_required()
    def post(self, id):
       current_user = get_jwt_identity()
       comment = request.json['comment']
       post = Post.query.get(id)
       new_react= Comment(user_id = current_user, post=post, comment=comment)
       new_react.save()    
       return new_react, 201
    
        
