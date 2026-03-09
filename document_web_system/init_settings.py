from server import app, db
from models import Setting

with app.app_context():

    setting = Setting.query.first()

    if not setting:
        setting = Setting(max_documents=5)
        db.session.add(setting)
        db.session.commit()
        print("系统阅读数量初始化成功")

    else:
        print("系统设置已存在")