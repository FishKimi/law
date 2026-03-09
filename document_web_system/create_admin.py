from server import app, db
from models import User

with app.app_context():

    admin = User(
        username="admin",
        role="admin",
        max_documents=100
    )

    db.session.add(admin)
    db.session.commit()

    print("管理员创建成功")