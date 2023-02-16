# from flask_restx import Namespace, Resource, fields
# from flask_jwt_extended import jwt_required, get_jwt_identity
# from models import Post, User, db, React, friendship
# from flask import request, jsonify



# friend_ns = Namespace('friend', description= "A namespace for Friend")

# # Schema
# friend_model = friend_ns.model(
#     "Friend",
#     {
#         "id": fields.Integer(),
#         "from_id": fields.Integer(),
#         "to_id": fields.Integer(),
#         "creted_on": fields.DateTime()
#     }
# )


# @friend_ns.route('/friend')
# class FriendResource(Resource):
#     @friend_ns.marshal_list_with(friend_model)
#     @jwt_required
#     def get(self):
#         friend = User.query.all()

#         return friend


# @friend_ns.route('/react/<int:id>')
# class FriendResources(Resource):
#     @friend_ns.marshal_with(friend_model)
#     @jwt_required()
#     def get(self, id):
#         friend = User.query.get(id)

#         return friend

#     @friend_ns.marshal_with(friend_model)
#     @friend_ns.expect(friend_model)
#     @jwt_required()
#     def post(self, id):
#        pass
       
       