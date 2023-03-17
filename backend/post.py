from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_current_user
from models import Post, User, db
from flask import request,jsonify
import os
import urllib.request
from werkzeug.utils import secure_filename


post_ns = Namespace('post', description="A namespace for Posts")


# Schema
post_model = post_ns.model(
    "Post",
    {
        "id": fields.Integer(),
        "user_id": fields.Integer(),
        "title": fields.String(),
        "description": fields.String(),
        "media": fields.String(),
        "created_date": fields.DateTime()
    }
)



@post_ns.route('/posts')
class PostResources(Resource):
    @post_ns.marshal_list_with(post_model)
    @jwt_required()
    def get(self):
        posts = Post.query.all()

        return posts

    @post_ns.marshal_with(post_model)
    @post_ns.expect(post_model)
    @jwt_required()
    def post(self):
       current_users = get_jwt_identity()
       title = request.json['title']
       description = request.json['description']
       media = request.json['media']
       new_post = Post(title=title, description=description, media= media, user_id = current_users)
       new_post.save()
       return new_post, 201


@post_ns.route('/posts/<int:id>')
class PostResources(Resource):
    @post_ns.marshal_with(post_model)
    @jwt_required()
    def get(self, id):
        posts = Post.query.get_or_404(id)

        return posts

    

    @jwt_required()
    def delete(self, id):
        delete_post = Post.query.get(id)
        user = Post.query.filter_by(user_id = get_jwt_identity()).first()
        if not user:
            return jsonify({"message": "You can't delete"})
        else:
            delete_post.delete()
            return jsonify({"message": "user deleted"})    
            