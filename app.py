from flask import Flask, render_template, request

app = Flask(__name__)

MESSAGE = """Dear pyari larki:

You are genuinely one of the most special people in my life. Your presence brings a kind of happiness and comfort that is hard to put into words. I truly appreciate every conversation, every laugh, and every little moment we share.

No matter where life takes us, I hope you always remember how much you are valued and appreciated. You have a beautiful place in my heart, and I’m grateful to have someone like you in my life.

Thank you for being you, for making ordinary moments feel meaningful, and for always being someone I can appreciate and care about. I hope life gives you countless reasons to smile, and I’ll always wish the very best for you. ❤️

یہ مجھے چین کیوں نہیں پڑتا

ایک ہی شخص ہے جہان میں کیا
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        name = request.form.get("name", "")
        f_name = request.form.get("f_name", "")
        cast = request.form.get("cast", "")

        # Same logic as your Python program:
        if cast.lower() == "gill":
            message = MESSAGE
        else:
            message = MESSAGE

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
