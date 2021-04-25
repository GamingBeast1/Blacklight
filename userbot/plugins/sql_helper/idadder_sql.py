#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from sqlalchemy import Column, String

from . import BASE, SESSION


class users2(BASE):
    __tablename__ = "users2"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


users2.__table__.create(checkfirst=True)


def add_usersid_in_db(chat_id: int):
    id_user = users2(str(chat_id))
    SESSION.add(id_user)
    SESSION.commit()


def users():
    all_users = SESSION.query(users2).all()
    SESSION.close()
    return all_users

def already_added(chat_id):
    try:
        return SESSION.query(users2).filter(users2.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()
