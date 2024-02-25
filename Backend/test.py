


import os
import shutil
import subprocess



def test1(input_script):
    try:
        # Execute the provided Python script
        result = subprocess.run(["python3", "-c", input_script], capture_output=True, text=True)
        return result.stdout.strip() == "Bonjour, le Monde !"
    except Exception as e:
        return False

def test2(input_script, user):
  
    
    
    
    code = ["Python", "hi lilo", "hello world", "hello", "hi", "bonjour", "bonjour le monde", "bonjour le monde !", "bonjour le monde !", "Bonjour le monde !", "Bonjour"]
    
    # make dir in teset folder, with user name
    if not os.path.exists(f'test/'):
        os.mkdir('test')  
    os.mkdir(f'test/{user}')
    
    # write code to file
    with open(f'test/{user}/main.py', '+w') as f:
        f.write(input_script)
    
    
    try:
        # Execute the provided Python script
        res = True
        for c in code:
          command = f"python3 test/{user}/main.py << EOF\n{c}\nEOF"
          result = subprocess.run(command, shell=True, text=True, capture_output=True)
          res = res and result.stdout == f'Entrez quelque chose : Vous avez saisi :  {c}\n'
        shutil.rmtree(f'test/{user}')
        return res
    except Exception as e:
        print(str(e))
        shutil.rmtree(f'test/{user}')
        return False


def test3(input_script, user):
  
    
    
    
    code = ["1", "+", "2"]
    
    # make dir in teset folder, with user name
    if not os.path.exists(f'test/'):
        os.mkdir('test')  
    os.mkdir(f'test/{user}')
    
    # write code to file
    with open(f'test/{user}/main.py', '+w') as f:
        f.write(input_script)
    
    
    try:
        # Execute the provided Python script
        res = False
        
        command = f"python3 test/{user}/main.py << EOF\n{code[0]}\n{code[1]}\n{code[2]}\nEOF"
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        res = result.stdout == f'Entrez le premier nombre : Entrez l\'opérateur (+, -, *, /) : Entrez le deuxième nombre : Résultat :  3\n'
        shutil.rmtree(f'test/{user}')
        return res
    except Exception as e:
        print(str(e))
        shutil.rmtree(f'test/{user}')
        return False
      
      
def test4(input_script, user):
  
    
    
    
    code = 37
    
    # make dir in teset folder, with user name
    if not os.path.exists(f'test/'):
        os.mkdir('test')  
    os.mkdir(f'test/{user}')
    
    # write code to file
    with open(f'test/{user}/main.py', '+w') as f:
        f.write(input_script)
    
    
    try:
        # Execute the provided Python script
        res = False
        
        command = f"python3 test/{user}/main.py << EOF\n{code}\nEOF"
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        res = result.stdout == f'Entrez la température en Celsius : Température en Fahrenheit : 98.60000000000001\n'
        shutil.rmtree(f'test/{user}')
        return res
    except Exception as e:
        print(str(e))
        shutil.rmtree(f'test/{user}')
        return False
      
      
def test6(input_script, user):
  
    
    
    
    code_rectangle = ["rectangle", "2", "3"] # 6.0
    code_cercle = ["cercle", "4", "5"] # 12.566370614359172
    
    
    # make dir in teset folder, with user name
    if not os.path.exists(f'test/'):
        os.mkdir('test')  
    os.mkdir(f'test/{user}')
    
    # write code to file
    with open(f'test/{user}/main.py', '+w') as f:
        f.write(input_script)
    
    
    try:
        # Execute the provided Python script
      res = False
      
      command1 = f"python3 test/{user}/main.py << EOF\n{code_rectangle[0]}\n{code_rectangle[1]}\n{code_rectangle[2]}\nEOF"
      result1 = subprocess.run(command1, shell=True, text=True, capture_output=True)
      
      
      command2 = f"python3 test/{user}/main.py << EOF\n{code_cercle[0]}\n{code_cercle[1]}\nEOF"
      result2 = subprocess.run(command2, shell=True, text=True, capture_output=True)
      
      
      res = result1.stdout == f'Entrez la forme (rectangle, cercle) : Entrez la longueur : Entrez la largeur : Surface : 6.0\n'
      res = res and result2.stdout == f'Entrez la forme (rectangle, cercle) : Entrez la longueur : Surface : 50.26548245743669\n'
      
      shutil.rmtree(f'test/{user}')
      return res
    except Exception as e:
        print(str(e))
        shutil.rmtree(f'test/{user}')
        return False
      
def test5(input_script, user):
  
    
    
    
    code = [50, 60, 1.45]
    
    result_test = [
      f'Entrez le montant (USD) : Montant converti : 501.50 MAD\n',
      f'Entrez le montant (USD) : Montant converti : 601.80 MAD\n',
      f'Entrez le montant (USD) : Montant converti : 14.54 MAD\n'
    ]
    
    
    # make dir in teset folder, with user name
    if not os.path.exists(f'test/'):
        os.mkdir('test')  
    os.mkdir(f'test/{user}')
    
    # write code to file
    with open(f'test/{user}/main.py', '+w') as f:
        f.write(input_script)
    
    
    try:
        # Execute the provided Python script
      res = True
      
      for index, c in enumerate(code):
        command = f"python3 test/{user}/main.py << EOF\n{c}\nEOF"
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        res = res and result.stdout == result_test[index]
      
      shutil.rmtree(f'test/{user}')
      return res
    except Exception as e:
        print(str(e))
        shutil.rmtree(f'test/{user}')
        return False
      
      
      
def test7(input_script, user):
  
    
    
    
    code = [3, 20, 50]
    
    const_input = 'Entrez la longueur du mot de passe : Votre mot de passe aléatoire : '
    
    
    # make dir in teset folder, with user name
    if not os.path.exists(f'test/'):
        os.mkdir('test')  
    os.mkdir(f'test/{user}')
    
    # write code to file
    with open(f'test/{user}/main.py', '+w') as f:
        f.write(input_script)
    
    
    
    try:
        # Execute the provided Python script
      res = True
      
      for index, c in enumerate(code):
        command = f"python3 test/{user}/main.py << EOF\n{c}\nEOF"
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        res = res and result.stdout[0:len(const_input)] == const_input
        res = res and len(result.stdout[len(const_input):]) - 1 == c
        
      
      shutil.rmtree(f'test/{user}')
      return res
    except Exception as e:
        print(str(e))
        shutil.rmtree(f'test/{user}')
        return False
      
      
def test8(input_script, user):
  
    
    code = ["www.google.com", "www.fb.com", "www.github.com"]
    
    const_input = 'Entrez la longueur du mot de passe : Votre mot de passe aléatoire : '
    
    
    # make dir in teset folder, with user name
    if not os.path.exists(f'test/'):
        os.mkdir('test')  
    os.mkdir(f'test/{user}')
    
    # write code to file
    with open(f'test/{user}/main.py', '+w') as f:
        f.write(input_script)
    
    
    try:
        # Execute the provided Python script
      res = True
      
      for c in code:
        command = f"python3 test/{user}/main.py {c}"
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        test_res = get_ip(c)
        print(result.stdout, test_res)
        res = res and result.stdout.strip() == test_res
        # res = res and result.stdout[0:len(const_input)] == const_input
        # res = res and len(result.stdout[len(const_input):]) - 1 == c
        
      
      shutil.rmtree(f'test/{user}')
      return res
    except Exception as e:
        print(str(e))
        shutil.rmtree(f'test/{user}')
        return False
      
      
import socket
      
def get_ip(url):

    try:
        ip_address = socket.gethostbyname(url)
        return(f"Adresse IP de \"{url}\" : {ip_address}")
    except socket.gaierror:
        return(f"Adresse IP de \"{url}\" : Not Found")
