from antlr4 import *
from Grammar.gramaticaParser import gramaticaParser
from Grammar.gramaticaVisitor import gramaticaVisitor
from scipy import stats
import math
import matplotlib.pyplot as plt
import numpy as np


class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class VisitorCompiler(gramaticaVisitor):
    def __init__(self):
        self.variables = {}
        self.funciones = {}
        self.call_stack = []


    def visitAsignacion(self, ctx: gramaticaParser.AsignacionContext):
        var_name = ctx.getChild(0).getText()
        if(ctx.expresion()):
            value = self.visit(ctx.expresion())
            self.variables[var_name] = value
        elif(ctx.matriz_operaciones()):
            value = self.visit(ctx.matriz_operaciones())
            self.variables[var_name] = value
        elif(ctx.arange()):
            value = self.visit(ctx.arange())
            self.variables[var_name] = value
        elif(ctx.v_input()):
            value = self.visit(ctx.v_input())
            self.variables[var_name] = value

    def visitV_input(self, ctx: gramaticaParser.V_inputContext):        
        value = input(self.visit(ctx.cadena()) + "\n" if ctx.cadena() else "")        
        return value

    def visitPrintf(self, ctx: gramaticaParser.PrintfContext): 
        value = self.visit(ctx.concatenacion())
        print(value)
        return value

    def visitConcatenacion(self, ctx: gramaticaParser.ConcatenacionContext):
        # Visit the first expression
        result = self.visit(ctx.expresion(0))
        # Iterate through the rest of the expressions
        for i in range(1, len(ctx.expresion())):
            result += str(self.visit(ctx.expresion(i)))
        return result
    
    def visitParametro(self, ctx):
        if ctx:
            ids = ctx.ID()
            if not isinstance(ids, list):
                ids = [ids]
            return [id.getText() for id in ids]
        return []
    
    def visitArgs(self, ctx):
        return [self.visit(exp) for exp in ctx.expresion()]

        
    def visitFuncion(self, ctx):
        func_name = ctx.ID().getText()
        params = self.visit(ctx.parametro()) if ctx.parametro() else []
        body = ctx.stmt_func()
        self.funciones[func_name] = (params, body) 

    def visitLlamafuncion(self, ctx):
        func_name = ctx.ID().getText()
        if func_name not in self.funciones:
            raise Exception(f"Function '{func_name}' not defined")

        parametros_func, cuerpo_funcion = self.funciones[func_name]
        parametros_llamada = self.visit(ctx.args()) if ctx.args() else []

        # Guardar las variables actuales
        variables_actuales = self.variables.copy()

        # Asignar nuevos valores a los parámetros
        for param, value in zip(parametros_func, parametros_llamada):
            self.variables[param] = value

        try:
            # Ejecutar la función y capturar el retorno
            resultado = self.visit(cuerpo_funcion)
        except ReturnValue as e:
            resultado = e.value

        # Restaurar las variables originales
        self.variables = variables_actuales

        return resultado


    def visitStmt_func(self, ctx):
        for sentencia in ctx.sentencias():
            resultado = self.visit(sentencia)
            if isinstance(resultado, ReturnValue):
                return resultado.value
            
    def executeSentencia(self, ctx):
        for sentencia in ctx.sentencias():
            self.visit(sentencia)
        if ctx.v_return():
            return self.visit(ctx.v_return())

    def visitV_return(self, ctx):
        if ctx.expresion():
            resultado = self.visit(ctx.expresion()) 
            raise ReturnValue(resultado)
        raise ReturnValue(None)

    def visitCondicional(self, ctx: gramaticaParser.CondicionalContext):
        condition = self.visit(ctx.expresion())
        condition_met = False

        if condition:
            for statement in ctx.sentencias():
                        self.visit(statement)
            condition_met = True

        if not condition_met and ctx.elifBlock():
            for elif_ctx in ctx.elifBlock().condicional_elif():
                elif_condition = self.visit(elif_ctx)
                if elif_condition:
                    condition_met = True
                    break

        if not condition_met and ctx.condicional_else():
            self.visit(ctx.condicional_else())

    def visitCondicional_else(self, ctx: gramaticaParser.Condicional_elseContext):
        for statement in ctx.sentencias():
                        self.visit(statement)

    def visitCondicional_elif(self, ctx: gramaticaParser.Condicional_elifContext):
        condition = self.visit(ctx.expresion())
        if condition:
            for statement in ctx.sentencias():
                self.visit(statement)
            return True
        else: return False


    def visitCiclo_for(self, ctx: gramaticaParser.Ciclo_forContext):
        # Obtener el nombre de la variable iteradora
        variable = ctx.ID().getText()

        # Determinar el tipo de ciclo for
        if ctx.RANGE():  # Ciclo for con range()
            # Obtener los límites del rango
            start = ctx.expresion(0).getText() # Obtener el valor inicial
            if(start.isalpha()):
                start = int(self.variables[start])
            end = ctx.expresion(1).getText()  # Obtener el valor final
            if(end.isalpha()):
                end = int(self.variables[end])
 
            # Verificar si se proporciona un valor para el incremento
            if len(ctx.expresion()) == 3:
                step = int(ctx.expresion(2).getText())
            else:
                step = 1

            # Ejecutar el ciclo for utilizando range()
            for valor in range(int(start), int(end), step):
                # Asignar el valor de la iteración a la variable
                self.variables[variable] = valor
                # Visitar las sentencias dentro del ciclo
                for sentencia in ctx.sentencias():
                    self.visit(sentencia)

        else:  # Ciclo for con una expresión iterable
            # Obtener la expresión iterable
            iterable = self.visit(ctx.expresion(0))

            # Ejecutar el ciclo for sobre el iterable
            for valor in iterable:
                # Asignar el valor de la iteración a la variable
                self.variables[variable] = valor
                # Visitar las sentencias dentro del ciclo
                for sentencia in ctx.sentencias():
                    self.visit(sentencia)

        # Verificar si hay un return al final del ciclo
        if ctx.v_return():
            return self.visit(ctx.v_return())

    def visitCiclo_while(self, ctx: gramaticaParser.Ciclo_whileContext):
        while self.visit(ctx.expresion()):
            for sentencia in ctx.sentencias():
                self.visit(sentencia)
            
 
    
    def visitMatriz_operaciones(self, ctx:gramaticaParser.Matriz_operacionesContext):
        if (ctx.getChild(2)==None):
            result = self.visit(ctx.matriz(0))
        else:
            if(ctx.getChild(0).getText()=="trans" or ctx.getChild(0).getText()=="inv"):
                matrix1 = self.visit(ctx.matriz(0)) if ctx.matriz(0) else self.variables[ctx.ID().getText()]
                matrix1 = np.array(matrix1)
                if ctx.getChild(0).getText()== 'trans':
                    result = np.transpose(matrix1)
                elif ctx.getChild(0).getText()== 'inv':
                    result = np.linalg.inv(matrix1)
            else:
                matrix1 = self.visit(ctx.matriz(0))
                matrix2 = self.visit(ctx.matriz(1))
                matrix1 = np.array(matrix1)
                matrix2 = np.array(matrix2)
                operator = ctx.getChild(1).getText()
                
                if operator == '+':
                    result = np.add(matrix1, matrix2)
                elif operator == '-':
                    result = np.subtract(matrix1, matrix2)
                elif operator == '*':
                    result = np.multiply(matrix1, matrix2)
        return result

    def visitMatriz(self, ctx: gramaticaParser.MatrizContext):
        rows = len(ctx.fila_matriz())
        cols = len(ctx.fila_matriz(0).expresion())

        matrix = np.zeros((rows, cols))
        
        for i, fila in enumerate(ctx.fila_matriz()):
            for j, exp in enumerate(fila.expresion()):
                matrix[i][j] = self.visit(exp)
        return matrix
        
    def visitExpresion(self, ctx: gramaticaParser.ExpresionContext):
        if ctx.SUMA() or ctx.RESTA() or ctx.MULTIPLICACION() or ctx.DIVISION() or ctx.POTENCIA() or ctx.MODULO():
            left = self.visit(ctx.expresion())
            right = self.visit(ctx.termino())
            
            op = ctx.getChild(1).getText()
            if isinstance(left, np.ndarray) or isinstance(right, np.ndarray):
                # Si alguno de los operandos es una matriz, realizar operación matricial
                if op == '+':
                    return np.add(left, right)
                elif op == '-':
                    return np.subtract(left, right)
                elif op == '*':
                    return np.matmul(left, right)  # Multiplicación de matrices
            else: 
                if op == '+':
                    return float(left) + float(right)
                elif op == '-':
                    return float(left) - float(right)
                elif op == '*':
                    return float(left) * float(right) 
                elif op == '/':
                    return float(left) / float(right)
                elif op == '^':
                    return float(left) ** float(right)
                elif op == '%':
                    return float(left) % float(right)
        elif ctx.MAYORQUE() or ctx.MENORQUE() or ctx.MENORIGUAL() or ctx.MAYORIGUAL() or ctx.DIFERENTE() or ctx.IGUAL():
            left = self.visit(ctx.expresion())
            right = self.visit(ctx.termino())
            op = ctx.getChild(1).getText()
            if op == '>':
                return float(left) > float(right)
            elif op == '<':
                return float(left) < float(right)
            elif op == '>=':
                return float(left) >= float(right)
            elif op == '<=':
                return float(left) <= float(right)
            elif op == '!=':
                return float(left) != float(right)
            elif op == '==':
                return float(left) == float(right)
                
        elif ctx.ASIGNACION():
            var_name = ctx.ID().getText()
            value = self.visit(ctx.termino())
            self.variables[var_name] = self.variables.get(value)
            return self.variables.get(var_name)
        elif ctx.OR():
            left = self.visit(ctx.expresion())
            right = self.visit(ctx.termino())
            return left or right
        elif ctx.AND():
            left = self.visit(ctx.expresion())
            right = self.visit(ctx.termino())
            return left and right
        elif ctx.func():
            return self.visit(ctx.func())
        elif ctx.llamafuncion():
            return self.visit(ctx.llamafuncion())
        else:
            return self.visit(ctx.termino())


    def visitTermino(self, ctx: gramaticaParser.TerminoContext):
        if ctx.ID():
            var_name = ctx.getChild(0).getText()
            return self.variables.get(var_name)
        elif ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        elif ctx.BOOLEAN():
            bool_value = ctx.BOOLEAN().getText()
            return bool_value == 'True'
        elif ctx.cadena():
            return self.visit(ctx.cadena())
        elif ctx.lista():
            return self.visit(ctx.lista())
        elif ctx.arreglo():
            return self.visit(ctx.arreglo())

    def visitCadena(self, ctx: gramaticaParser.CadenaContext):
        return ctx.getText()[1:-1]
    
    def visitLista(self, ctx: gramaticaParser.ListaContext):
        text = ctx.getText()[1:-1]  # Obtener el texto sin los corchetes
        elements = text.split(',')  # Dividir el texto en función del separador (coma en este caso)
        return [element.strip() for element in elements]  # Crear una lista resultante, eliminando los espacios en blanco alrededor de cada elemento

    def visitArreglo(self, ctx: gramaticaParser.ArregloContext):
        text = ctx.getText().strip()[1:-1]  # Obtener el texto sin los corchetes y eliminar espacios en blanco
        if not text:  # Si el texto está vacío, retornar una lista vacía
            return []
        elements = text.split(',')
        elements = [float(x) for x in elements]  # Convertir cada elemento a flotante
        return elements

    def visitMetodo(self, ctx):
        variable = ctx.ID().getText()  # Nombre de la variable
        metodo = ctx.getChild(2).getText()
        args = [self.visit(ctx.expresion())]  # Argumentos del método

        # Verificar qué método se está llamando y realizar la acción correspondiente
        if metodo == 'append':
            if isinstance(self.variables[variable], list):  # Si es una lista
                self.variables[variable].append(args[0])  # Agregar el argumento a la lista
            elif isinstance(self.variables[variable], np.ndarray):  # Si es una matriz
                self.variables[variable] = np.vstack([self.variables[variable], args])
            else:
                raise Exception("Append operation not supported for this type")
        elif metodo == 'remove':
            if isinstance(self.variables[variable], list):  # Si es una lista
                del self.variables[variable][args[0]]
            elif isinstance(self.variables[variable], np.ndarray):  # Si es una matriz
                if isinstance(args[0], int):  # Si se pasó un índice
                    self.variables[variable] = np.delete(self.variables[variable], args[0], axis=0)
                else:  # Si se pasó el valor del elemento
                    for i, fila in enumerate(self.variables[variable]):
                        if args[0] in fila:
                            self.variables[variable] = np.delete(self.variables[variable], i, axis=0)
                            break
                    else:
                        raise ValueError(f"{args[0]} not in array")
            else:
                raise Exception("Remove operation not supported for this type")
        else:
            raise Exception(f"Method '{metodo}' not recognized")

    def append(self, variable, value):
        if isinstance(variable, list):
            variable.append(value)
        elif isinstance(variable, np.ndarray):
            value = np.array([value], dtype=object)
            variable = np.vstack([variable, value])
        else:
            raise Exception("Append operation not supported for this type")
        return variable

    def remove(self, variable, index_or_value):
        if isinstance(variable, list):
            if isinstance(index_or_value, int):
                del variable[index_or_value]
            else:
                variable.remove(index_or_value)
        elif isinstance(variable, np.ndarray):
            if isinstance(index_or_value, int):
                variable = np.delete(variable, index_or_value, axis=0)
            else:
                for row in variable:
                    if index_or_value in row:
                        variable = np.delete(variable, np.where(variable == index_or_value)[0][0], axis=0)
                        break
                else:
                    raise ValueError(f"{index_or_value} not in array")
        else:
            raise Exception("Remove operation not supported for this type")
        return variable

    def parse_element(self, element):
        try:
            return float(element) if '.' in element else int(element)
        except ValueError:
            return element

    def visitGraficas(self, ctx: gramaticaParser.GraficasContext):
        if ctx.getChild(0).getText() == "scatter":
            x = self.visit(ctx.getChild(2))
            y = self.visit(ctx.getChild(4))

            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.scatter(x, y)

            x= np.array(x)

            # Calcular la regresión lineal
            slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
            line = slope * x + intercept
            ax.plot(x, line, color='red', label='Regresión lineal')

            plt.show()
        elif(ctx.getChild(0).getText()=="plot"):
            x = self.visit(ctx.getChild(2))
            y = self.visit(ctx.getChild(4))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.plot(x, y)
            plt.show()
        elif(ctx.getChild(0).getText()=="fill_between"):
            x = self.visit(ctx.getChild(2))
            y = self.visit(ctx.getChild(4))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.fill_between(x, y)
            plt.show()
        elif(ctx.getChild(0).getText()=="barh"):
            x = self.visit(ctx.getChild(2))
            y = self.visit(ctx.getChild(4))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.barh(x, y)
            plt.show()
        elif(ctx.getChild(0).getText()=="bar"):
            x = self.visit(ctx.getChild(2))
            y = self.visit(ctx.getChild(4))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.bar(x, y)
            plt.show()
        elif(ctx.getChild(0).getText()=="hist"):
            x = self.visit(ctx.getChild(2))
            y = self.visit(ctx.getChild(4))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.hist(x, y)
            plt.show()
        elif(ctx.getChild(0).getText()=="boxplot"):
            x = self.visit(ctx.getChild(2))
            fig, ax = plt.subplots()
            ax.boxplot(x)
            plt.show()
        elif(ctx.getChild(0).getText()=="pie"):
            x = self.visit(ctx.getChild(2))
            fig, ax = plt.subplots()  # Obtener la figura y los ejes
            ax.pie(x)
            plt.show()
        elif(ctx.getChild(0).getText()=="grafsen" or ctx.getChild(0).getText()=="grafcos" or ctx.getChild(0).getText()=="graftan"):
            if(ctx.ID()):
                var_name = ctx.getChild(2).getText()
                print(var_name)
                x = self.variables.get(var_name)
            else:
                print(self.visit(ctx.arange()))
                x = self.visit(ctx.arange())
            y = self.visit(ctx.func())
            fig, ax = plt.subplots()
            ax.set_title(ctx.func().getText()[3:])
            ax.plot(x, y)
            plt.show()

    def visitArange(self, ctx: gramaticaParser.ArangeContext): 
        #print(ctx.expresion(0).getText())
        x = int(ctx.expresion(0).getText())
        y = int(ctx.expresion(1).getText())*np.pi
        #print(ctx.expresion(1).getText())
        z = int(ctx.expresion(2).getText())
        #print(ctx.expresion(2).getText())
        arr = np.linspace(x,y,z)
        return arr
    
    def visitLectura_archivo(self, ctx: gramaticaParser.Lectura_archivoContext):
        nombre_archivo = ctx.getChild(2).getText().replace('"','').replace("'","")
        with open(nombre_archivo, 'r') as file:
            lineas = file.readlines()
        for i in range(len(lineas)):
            if(lineas[i]=="\n"):
                print("\n")
            else:
                print(lineas[i])

        # Realizar acciones con las líneas del archivo leído, si es necesario

    def visitEscritura_archivo(self, ctx: gramaticaParser.Escritura_archivoContext):
        nombre_archivo = ctx.getChild(2).getText().replace('"','').replace("'","")
        cadena = ctx.getChild(4).getText().replace('"','').replace("'","")
        with open(nombre_archivo, 'w') as file:
            cadena = cadena.replace('~',' ')
            file.write(cadena.replace('¬','\n'))

    def visitFunc(self, ctx: gramaticaParser.FuncContext):
        value = self.visit(ctx.expresion())
        function_name = ctx.getChild(2).getText()
        #Para radianes math
        if(ctx.getChild(0).getText()=="math"):

            if function_name=="factorial":
                a = math.factorial(int(value))
            elif function_name=="sqrt":
                a = math.sqrt(float(value))
            if isinstance(self.visit(ctx.expresion()), str):
                value = math.radians(int(value))
            else:
                value = math.radians(value)
            if function_name=="sin":
                a = math.sin(value)
            elif function_name=="cos":
                a = math.cos(value)
            elif function_name== "tan":
                a = math.tan(value)
            elif function_name=="arcsin":
                a = math.asin(value)
            elif function_name=="arccos":
                a = math.acos(value)
            elif function_name== "arctan":
                a = math.atan(value)
            #print(a)
            return a 
        #Sin radianes
        elif(ctx.getChild(0).getText()=="np"):

            if isinstance(self.visit(ctx.expresion()), str):
                value = int(value)

            if function_name=="sin":
                a = np.sin(value)
            elif function_name=="cos":
                 a = np.cos(value)
            elif function_name== "tan":
                 a = np.tan(value)
            elif function_name=="arcsin":
                a = np.arcsin(value)
            elif function_name=="arccos":
                a = np.arccos(value)
            elif function_name== "arctan":
                a = np.arctan(value)
            return a       

