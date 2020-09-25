from app import create_app
from flask import Flask

def test_create_app_deve_retornar_um_app_flask():
	assert isinstance(create_app(), Flask)

def test_login_deve_retornar_sucesso(client):
	response = client.get('/login') # 1

	assert response.status_code == 200 # 2

def teste_endpoint_de_login_deve_retornar_o_template_de_login(client, templates):
	client.get('/login')

	assert templates[0].name == 'login.html'