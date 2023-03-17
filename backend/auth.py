from flask_restx import Resource, Namespace, fields
from models import User
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
from flask import request, jsonify, make_response


auth_ns = Namespace('auth', description="A namespace for Authentication")

signup_model = auth_ns.model(
    "SignUp",
    {
        "first_name": fields.String(),
        "last_name": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
        "profile_pic": fields.String(),
        "dob": fields.String(),
        "created_on": fields.DateTime()
    }
)

login_model = auth_ns.model(
    "Login",
    {
        "email": fields.String(),
        "password": fields.String()
    }
)


@auth_ns.route('/signup')
class SignUp(Resource):

    @auth_ns.expect(signup_model)
    def post(self):
        f_name = request.json['f_name']
        l_name = request.json['l_name']
        email =  request.json['email']
        profile_pic = request.json['profile_pic']
        dob = request.json['dob']

        db_user = User.query.filter_by(email=email).first()
        if db_user is not None:
            return jsonify({"message": f"Email with this {email} is alreadt exits"})
        email = request.json['email']
        password = generate_password_hash(request.json['password'])
        new_user = User(f_name=f_name, l_name=l_name, profile_pic=profile_pic, dob=dob, email=email, password=password)
        new_user.save()

        return make_response(jsonify({"message": "User Created Suceesfully"}), 201)



@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        email = request.json['email']
        password = request.json['password']

        db_user = User.query.filter_by(email=email).first()
        if db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity=db_user.id)
            refresh_token = create_refresh_token(identity=db_user.id)    

            return jsonify(
                {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                }
            )
        else:
            return jsonify({"message": "Incorrect Cradentials"})    


@auth_ns.route('/me')
class Me(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        return make_response(jsonify({"user": user.f_name+ ' ' + user.l_name, "email": user.email}))


@auth_ns.route('/refresh')
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_tokken=create_access_token(identity=current_user)

        return make_response(jsonify({"access_token": new_access_tokken}), 200)      