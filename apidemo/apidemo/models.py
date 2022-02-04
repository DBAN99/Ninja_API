from django.contrib.auth.models import User
from ninja import ModelSchema


# 특정 스키마 생성
class A_UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username', 'first_name', 'last_name']

# Will create schema like this:
#
# class UserSchema(Schema):
#     id: int
#     username: str
#     first_name: str
#     last_name: str

# model_fields를 이용해 모든 column을 사용하는 방법 - 비추
class B_UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = "__all__"

# model_exclude를 이용해서 사용하면 exclude에 해당하는 column을 제외하고 나머지 모두를 사용할 수 있음
class C_UserSchema(ModelSchema):
    class Config:
        model = User
        model_exclude = ['password', 'last_login', 'user_permissions']