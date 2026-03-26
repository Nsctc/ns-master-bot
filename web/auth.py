from flask import request, redirect, session
from config import ADMIN_USER, ADMIN_PASS

def login_required(func):
    def wrapper(*args, **kwargs):
        if session.get("user") != ADMIN_USER:
            return redirect("/login")
        return func(*args, **kwargs)
    return wrapper
