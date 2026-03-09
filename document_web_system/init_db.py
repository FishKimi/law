from app import app
from models import db, User, Document, Question

with app.app_context():

    db.create_all()

    if not User.query.filter_by(username="admin").first():

        admin = User(username="admin", role="admin")

        db.session.add(admin)

    if not Document.query.first():

        doc = Document(
            title="人工智能法律应用",
            content="""
人工智能在法律领域的应用包括：

1. 案例检索
2. 合同审查
3. 法律预测
"""
        )

        db.session.add(doc)

        db.session.commit()

        q1 = Question(
            document_id=doc.id,
            question="文档结构是否清晰？",
            description="根据逻辑结构和条理性评分"
        )

        q2 = Question(
            document_id=doc.id,
            question="文档内容是否具有价值？",
            description="根据内容质量评分"
        )

        db.session.add(q1)
        db.session.add(q2)

    db.session.commit()

    print("数据库初始化完成")