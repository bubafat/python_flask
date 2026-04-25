# Lista de Comando

- Cria o ambiente visual na pasta venv
```python
python -m venv venv
```
- Ativar o  ambiente virtual
```python
venv\Scripts\activate
```
- instalar todos os pacotes necessários
```python
pip install flask
pip install flask-wtf
pip install requests
pip install pytest
pip install pytest-flask 
``` 
ou se houver o arquivo requeriments.txt
```
pip install -r requeriments.txt
```
- Salva a lista de pacotes instalados no arquivo requirements.txt
- Isso permite que outars pessoas isntalem as mesmas versões 
```python
pip freeze > requirements.txt
```

## Criar o arquivo .gitignore
- Diz ao git quais arquivos e pastas **NÂO devem ser versionados**  