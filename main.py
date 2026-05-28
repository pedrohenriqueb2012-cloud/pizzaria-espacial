from flask import Flask, render_template, request
import os

app = Flask(__name__)

contador = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/opcao', methods=['POST'])
def opcao():

    nome = request.form["nome"]
    planeta = request.form["planeta"]

    imagem_planeta = planeta.lower()
    imagem_planeta = imagem_planeta.replace("ú", "u")
    imagem_planeta = imagem_planeta.replace("ê", "e")
    imagem_planeta = imagem_planeta.replace("ã", "a")
    imagem_planeta = imagem_planeta.replace("ô", "o")

    return render_template(
        'opcao.html',
        nome=nome,
        planeta=planeta,
        imagem_planeta=imagem_planeta
    )

@app.route('/pedido', methods=['POST'])
def pedido():
        global contador

        nome = request.form["nome"]
        planeta = request.form["planeta"]
        tamanho = request.form["tamanho"]
        bebida = request.form["bebida"]
        pizza = request.form["pizza"]
        borda = request.form["borda"]

        imagem_planeta = planeta.lower()
        imagem_planeta = imagem_planeta.replace("ú", "u")
        imagem_planeta = imagem_planeta.replace("ê", "e")
        imagem_planeta = imagem_planeta.replace("ã", "a")
        imagem_planeta = imagem_planeta.replace("ô", "o")

        #preço:

        #pizza:
        total = 0
        if pizza == "mussarela (R$9,99)":
            total += 9.99
        elif pizza == "calabresa (R$19,99)":
            total += 19.99
        elif pizza == "frango (R$24,99)":
            total += 24.99
        elif pizza == "portuguesa (R$99,99)":
            total += 99.99
        elif pizza == "bota-tudo (R$29,99)":
            total += 29.99
        elif pizza == "4 queijos (R$14,99)":
            total += 14.99
        elif pizza == "atum (R$0,99)":
            total += 0.99

        #borda:
        if borda == "nenhuma":
            total += 0
        elif borda == "catupiry (+R$5,00)":
            total += 5.00
        elif borda == "cheddar (+R$7,00)":
            total += 7.00
        elif borda == "gleaber (NOVO!!) (+R$7,00)":
            total += 7.00

        #tamanho:
        if tamanho == "Pequena (-10%)":
            total *= 0.9
        elif tamanho == "Grande (+10%)":
            total *= 1.1

        #bebida:
        if bebida == "nenhuma":
            total += 0
        elif bebida == "caco cola (+R$2,00)":
            total += 2.00
        elif bebida == "pepsuco (+R$1,50)":
            total += 1.50
        elif bebida == "guaramá (+R$2,00)":
            total += 2.00
        elif bebida == "elefanta (+R$1,00)":
            total += 1.00
        elif bebida == "uisqui (+R$2,50)":
            total += 2.50

        #fim
        total = round(total, 2)



        caminho_arquivo = os.path.join(
            os.path.dirname(__file__),
            "pedidos.txt"
        )
        with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:

            arquivo.write(f"Pedido {contador}\n")
            arquivo.write(f"Nome: {nome}\n")
            arquivo.write(f"Planeta: {planeta}\n")
            arquivo.write(f"Pizza: {pizza}\n")
            arquivo.write(f"Borda: {borda}\n")
            arquivo.write(f"Tamanho: {tamanho}\n")
            arquivo.write(f"Bebida: {bebida}\n")
            arquivo.write(f"Total: R$ {total}\n")
            arquivo.write("\n-------------------\n\n")
        contador +=1

        return render_template(
            'pedido.html', 
            nome=nome,
            planeta=planeta,
            imagem_planeta=imagem_planeta,
            pizza=pizza,
            borda=borda,
            tamanho=tamanho,
            bebida=bebida,
            total=total
        )

if __name__ == '__main__':
    app.run(debug=True)