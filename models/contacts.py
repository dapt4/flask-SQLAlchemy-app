from sqlalchemy.orm import Mapped, mapped_column

from utils.db import db


class Contact(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column()
    phone: Mapped[str]

    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone
