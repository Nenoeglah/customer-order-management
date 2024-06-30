

# # from flask_sqlalchemy import SQLAlchemy

# # db = SQLAlchemy()

# # class Config:
# #     SQLALCHEMY_DATABASE_URI = 'sqlite:///customers_orders.db'
# #     SQLALCHEMY_TRACK_MODIFICATIONS = False
# #     OIDC_CLIENT_SECRETS = 'client_secrets.json'
# #     OIDC_COOKIE_SECURE = False
# #     AFRICASTALKING_API_KEY = 'atsk_93f6b495ec5942eface502ae9c4f2b4db98cc4087765415fdf9898582333daf803d81785'
# #     AFRICASTALKING_USERNAME = 'Eglah Chepngeno'
# #     # SECRET_KEY = 'Tsltg7cmLvxCaqrJms9jhs4bC2t1wyUERNdj_hoO54okF-TrYHcFZLPaOgOod3mz'



# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Config:
#     SECRET_KEY = '1234'  
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///customers_orders.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     OIDC_CLIENT_SECRETS = 'client_secrets.json'
#     OIDC_COOKIE_SECURE = False
#     AFRICASTALKING_API_KEY = 'atsk_93f6b495ec5942eface502ae9c4f2b4db98cc4087765415fdf9898582333daf803d81785'
#     AFRICASTALKING_USERNAME = 'Eglah Chepngeno'




import os

class Config:
    SECRET_KEY = '1234'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///customer_order.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OIDC_CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')
    OIDC_SCOPES = ['openid', 'email', 'profile']
    OIDC_REDIRECT_URI = 'http://localhost:5000/authorization-code/callback'
    # OIDC_ID_TOKEN_COOKIE_SECURE = False
    # OIDC_REQUIRE_VERIFIED_EMAIL = False
    # OIDC_VALID_ISSUERS = ['https://dev-13632230.okta.com/oauth2/default']
    AFRICASTALKING_USERNAME = 'Eglah Chepngeno'
    AFRICASTALKING_API_KEY = 'atsk_93f6b495ec5942eface502ae9c4f2b4db98cc4087765415fdf9898582333daf803d81785'
