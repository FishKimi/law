from flask import Flask, render_template, request, redirect, session
from models import db, User, Setting, Document, Question, Score

app = Flask(__name__)

app.secret_key = "secret"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        user = User.query.filter_by(username=username).first()

        if user:

            session["user"] = user.username
            session["role"] = user.role

            if user.role == "admin":
                return redirect("/admin")

            return redirect("/read")

    return render_template("login.html")


@app.route("/admin")
def admin():

    if session.get("role") != "admin":
        return "无权限"

    setting = Setting.query.first()

    questions = Question.query.all()

    return render_template(
        "admin.html",
        max_documents=setting.max_documents,
        questions=questions
    )


@app.route("/set_limit", methods=["POST"])
def set_limit():

    if session.get("role") != "admin":
        return "无权限"

    value = int(request.form["limit"])

    setting = Setting.query.first()

    setting.max_documents = value

    db.session.commit()

    return redirect("/admin")


@app.route("/add_question", methods=["POST"])
def add_question():

    if session.get("role") != "admin":
        return "无权限"

    q = Question(

        document_id=1,

        question=request.form["question"],

        description=request.form["description"]

    )

    db.session.add(q)

    db.session.commit()

    return redirect("/admin")


@app.route("/read")
def read():

    user = User.query.filter_by(username=session["user"]).first()

    setting = Setting.query.first()

    count = Score.query.filter_by(user_id=user.id).count()

    if count >= setting.max_documents:
        return "已达到评分上限"

    doc = Document.query.first()

    return render_template("read.html", doc=doc)


@app.route("/score", methods=["GET", "POST"])
def score():

    user = User.query.filter_by(username=session["user"]).first()

    questions = Question.query.all()

    if request.method == "POST":

        for q in questions:

            value = int(request.form[f"score_{q.id}"])

            s = Score(

                user_id=user.id,

                question_id=q.id,

                score=value

            )

            db.session.add(s)

        db.session.commit()

        return "评分提交成功"

    return render_template("score.html", questions=questions)


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)