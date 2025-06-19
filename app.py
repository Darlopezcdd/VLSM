from flask import Flask, render_template, request, make_response
from weasyprint import HTML
from logic.vlcm import vlcm
from logic.ip import Ip
from logic.redes import Red

app = Flask(__name__)


resultado = None
redes_resultado = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global resultado, redes_resultado

    if request.method == 'POST':
        ip_base = request.form.get('ip_base')
        mascara = int(request.form.get('mascara'))
        redes_raw = request.form.get('redes')

        ip_obj = Ip(*map(int, ip_base.split(".")), mascara)

        redes_info = []
        for linea in redes_raw.strip().splitlines():
            if ',' in linea:
                nombre, hosts = linea.strip().split(",")
                redes_info.append(Red(nombre.strip(), int(hosts.strip())))

        v = vlcm(ip_obj, redes_info)
        resultado = v.vlcm()

        redes_resultado = v.redes_info
        resultado = resultado.replace("\t", " ")

    return render_template("index.html", resultado=resultado, redes=redes_resultado)


@app.route('/generate_pdf_report')
def generate_pdf_report():

    html_content = render_template("resultado.html", resultado=resultado, redes=redes_resultado)

    pdf = HTML(string=html_content).write_pdf()

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=detalle_subredes.pdf'
    return response


@app.route('/generate_pdf_process')
def generate_pdf_process():

    html_content = render_template("proceso.html", resultado=resultado)

    pdf = HTML(string=html_content).write_pdf()

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=proceso_vlcm.pdf'
    return response


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)