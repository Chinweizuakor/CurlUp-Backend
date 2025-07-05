"""Curlup Backend System Model Utility Functions."""

import secrets
import uuid


def generate_uuid() -> str:
    return str(uuid.uuid4())


def generate_client_id() -> str:
    return "CLI" + "".join(secrets.choice("0123456789") for _ in range(10))


def generate_admin_id() -> str:
    return "ADM" + "".join(secrets.choice("0123456789") for _ in range(10))


def generate_vendor_id() -> str:
    return "VEN" + "".join(secrets.choice("0123456789") for _ in range(10))
