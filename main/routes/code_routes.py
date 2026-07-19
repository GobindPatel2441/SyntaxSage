from flask import Blueprint,render_template,request

from main.services.code_generator import generate_code
from main.services.error_solver import solve_error
from main.services.logic_exp import explain_logic

code_bp = Blueprint('code',__name__)

@code_bp.route("/",methods=['GET','POST'])
def home():
    response =""

    if request.method =='POST':
        user_input = request.form['prompt']
        mode = request.form["mode"]

        if mode == "generate":
            response=generate_code(user_input)
        elif mode == "debug":
            response = solve_error(user_input)
        elif mode == "logic":
            response =explain_logic(user_input)
    return render_template("index.html",response = response)