def allauth_login_context(request):
    return {
        "title": "Connexion",
        "no_accout": "Si vous n’avez pas encore créé de compte, veuillez",
        "sign_up": "vous inscrire.",
    }


def login_signup_items(request):
    menu_items = [
        {"name": "Login", "url": "account_login"},
        {"name": "Signup", "url": "account_signup"},
    ]
    return {"login_signup_items": menu_items}


def profile_items(request):
    menu_items = [
        {"name": "My profile", "url": "users:profile"},
        {"name": "Edit Profile", "url": "users:profile-edit"},
        {"name": "Settings", "url": "users:profile-settings"},
        {"name": "Log Out", "url": "account_logout"},
    ]
    return {"profile_items": menu_items}
