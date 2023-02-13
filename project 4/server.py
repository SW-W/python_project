from flask import Flask, render_template, url_for, request
import datetime


app = Flask(__name__)
tasks = []

@app.route('/', methods= ['GET','POST'])
def home():
    today=datetime.datetime.now().date()
    pth =str(request.url)
    if "=" in pth:
        ind = int(pth.index("="))
        task = pth[ind+1:int(len(pth))]
        tasks.append(task)
    print(tasks)

    if request.method == 'POST':
        done_item = request.form.get("task")
        for item in tasks:
            if item == done_item:
                tasks.remove(item)
    return render_template("index.html", tasks=tasks, len=len, date=today)

if __name__ == "__main__":
    app.run(debug=True)
