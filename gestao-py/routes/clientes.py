from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

'''
Rota de clientes;

    -/clientes/ (GET) - listar clientes;
    -/clientes/ (POST) - inserir um cliente no servidor;
    -/clientes/new (GET) - renderizar um formulário para criar o cliente;
    -/clientes/<id> (GET) - obter os dados do cliente;
    -/clientes/<id>/edit (GET) - renderizar um formulário para editar um cliente;
    -/clientes/<id>/update (PUT) - atualizar dos dados do cliente;
    -/clientes/<id>/delete (DELETE) - deleta o registro do usuário;
'''

@cliente_route.route('/')
def lista_clientes() :
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes = clientes)
    
@cliente_route.route('/', methods=['POST']) 
def inserir_clientes() :
    data = request.json

    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['Email'],
        endereco = data['endereco'],
        cpf = data['cpf'],


    )  

    return render_template('item_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente() :
    return render_template('form_cliente.html')
    
@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id) :
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente = cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id) :
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html', cliente = cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id) :
    
    data = request.json  

    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['Email']
    cliente_editado.endereco = data['endereco']
    cliente_editado.save()
    
    #editar usuário
    return render_template('item_cliente.html', cliente = cliente_editado)

    
@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id) :
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return{'deleted': 'ok'}



    