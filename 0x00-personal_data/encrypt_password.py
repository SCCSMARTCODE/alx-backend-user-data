#!/usr/bin/env python3
"""
Defines a hash_password function to return a hashed password
"""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """
    :param password:
    :return:
    """
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    :param hashed_password:
    :param password:
    :return:
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
