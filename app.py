from flask import Flask, render_template, request
import speedtest
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        download = round(res["download"]/1000, 2)
        upload = round(res["upload"]/1000, 2)
        print("-->Download Speed: {:.2f} kb/s\n-->Upload Speed: {:.2f} Kb/s".format(download, upload))
        return render_template('index.html', download=download, upload=upload)
    else:
        return render_template('index.html', download=0, upload=0)


if __name__=='__main__':
    app.run()



