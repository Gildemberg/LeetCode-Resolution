# Você recebe dois não vazio listas vinculadas representando dois inteiros não negativos. 
# Os dígitos são armazenados em ordem inversa, e cada um dos seus nós contém um único dígito. 
# Adicione os dois números e retorne a soma como uma lista vinculada.Você pode assumir que os dois números não contêm nenhum zero à esquerda, exceto o próprio número 0.

# Entrada: l1 = [2,4,3], l2 = [5,6,4]
# Saída: [7,0,8]
# Explicação: 342 + 465 = 807.

# Exemplo 2:
# Entrada: l1 = [0], l2 = [0]
# Saída: [0]

# Exemplo 3:
# Entrada: l1 = [9,9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Saída: [8,9,9,9,0,0,0,1]


class ListNode:        
    class No:
        def __init__(self, valor, proximoV=None):
            self.valor=valor
            self.proximoV=proximoV

    def __init__(self):
        self.__cabeca=None
        self.__quantidade=0

    def __len__(self):
        return self.__quantidade

    def inserir(self, posicao, valor):
        novoElemento = self.No(valor) #criar um novo Elemento (No)
        self.__quantidade += 1

        #Se não houver nenhum elemento
        if self.__cabeca = is None:
            self.__cabeca = novoElemento
            return
        
        #Se a posição informada for 0 ou negativo, inserir no inicio da NodeList
        if posicao <=0:
            novoElemento.proximoV = self.__cabeca
            self.__cabeca = novoElemento
            return

        index = 0
        pointerAtual = self.__cabeca
        
        #Para inserir em qualquer posição (NodeList not null) 
        while ponterAtual = is not None and index < posicao-1:
            pointerAtual = pointerAtual.poximoV
            index+=1
        
        novoElemento.proximoV=pointerAtual.proximoV
        pointerAtual.proximoV=novoElemento





class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tamL1=len(l1)
        tamL2=len(l2)
        numero1=0
        numero2=0
        for num in l1[::-1]:
            numero1 += num*(10**tamL1)
            tamL1-=1
        for num2 in l2[::-1]:
            numero2 += num2*(10**tamL2)
            tamL2-=1

        numResultado = srt(numero1+numero2)
        
        resultado = []
        tamRes = len(numResultado)
        while tamRes>=0:
            resultado.append(int(numResultado[tamRes-1]))
            tamRes-=1


l1 = ListNode()
l1.inserir(0, 2)
l1.inserir(0, 4)
l1.inserir(0, 3)

l2 = ListNode()
l2.inserir(0, 5)
l2.inserir(0, 6)
l2.inserir(0, 4)
