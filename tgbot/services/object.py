"""Dataclasses for the translator."""
from dataclasses import dataclass


@dataclass
class Account(object):
    """Translation object."""

    id: int 
    username: str
    phone_number: str
    balance_usd: float





