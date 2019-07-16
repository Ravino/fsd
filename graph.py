  
f = open("./input.graph","r+")

#Список смежности - Adjacency list
AdjVertices = {} 
 
vertxsNum = f.readline() 
for i in range (1, int(vertxsNum)+1):
    k = f.readline().split(': ')  
    edg = k[1].rstrip().split(', ')
    edges = {} 
    AdjVertices[k[0]] = edg
 

def giveHelp():
    print("\t1 Вывести на экран список смежности")
    print("\n\t3 Добавить вершину")
    print("\n\t3- Удалить вершину")
    print("\t4 Добавить дугу")
    print("\t4- Удалить дугу")
    print("\n\t6 Поиск в ширину")
    print("\t7 Рассчитать матрицу достижимости") 
    print("\n\t0 - Выход")

def addVertex(): 
    key = input("\n\tВведите название новой вершины \n")
    AdjVertices[key] = []
    print("Готово")

def removeVertex(): 
    key = input("\n\tВведите вершину которую надо убрать\n")
    AdjVertices.pop(key, None)  
    print("Готово")

def addEdge(  ):
        vert1 = input("\n\tВведите исходную вершину\n")
        vert2 = input("\n\tВведите вторую вершину  \n")
        weight = input("\n\tВведите вес ребра\n") 
        AdjVertices[vert1].append(str(vert2 + "-" + weight))

def removeEdge():
        vert1 = input("\n\tВведите исходную вершину\n")
        vert2 = input("\n\tВведите вторую вершину  \n")
        weight = input("\n\tВведите вес ребра\n") 
        AdjVertices[vert1] = AdjVertices[vert1].remove(str(vert2 + "-" + weight)) 
        

def printAdjList(): 
    print("\nКлюч отображает вершину, списки - смежные с ней вершины")
    print("Через дефис обозначается вес ребра") 
    print(AdjVertices) 

def BF_withInp():
    # Запуск поиска в ширину из консоли
    vert1 = input("\n\tВведите исходную вершину\n")
    vert2 = input("\n\tВведите вершину для поиска \n")
    BreadthFirst(vert1, vert2)  

def BreadthFirst(vert1, vert2):  
        steps = 0
        lvldeep = 0

        queue = []
        visited = []
        ans = False 

        if vert1 == vert2:
            ans = True
            print("Поиск в ширину завершён, искомое идентично первой данной вершине")
            return ans
        else: 
            visited.append(vert1)
            for v in AdjVertices[vert1]:
                queue.append(str(v.split('-')[0]))

        steps += 1 

        while queue.__len__() >  0 or ans is not True: 
             
            if not queue[0]:
                print("Поиск в ширину завершился провалом, вершин проверено: ") 
                print(steps) 
                return ans 
            if not queue:
                print("Поиск в ширину завершился провалом, вершин проверено: ") 
                print(steps) 
                return
            if queue[0] == vert2 and not visited.__contains__(queue[0]):
                ans = True
                print("Поиск в ширину завершён, вершин проверено: ") 
                print(steps) 
                return ans
            else:
                visited.append(queue[0])
                for v in AdjVertices[queue[0]]:
                    queue.append(str(v.split('-')[0]))
                queue.pop(0)
                steps += 1 


        print("Поиск в ширину завершился провалом, вершин проверено: ") 
        print(steps) 
        return ans



def Reachability():

    matrixR = []
    for v in range(0, list(AdjVertices.keys()).__len__()):
        zeros = []
        for vv in range(0, list(AdjVertices.keys()).__len__()):
            zeros.append(0)
        matrixR.append(zeros)

    print(AdjVertices.keys())
    print(matrixR[0][0])
    matrixR[0][0] = 7732
    print(matrixR[6][6])

    matrixR
    row = 0
    col = 0 
    for v in  list(AdjVertices.keys()) :
        for vv in  list(AdjVertices.keys()) : 
            matrixR[row][col] = int(BreadthFirst(v, vv))
            col +=1 
        col = 0
        row +=1   
    
    for i in range(0, list(AdjVertices.keys()).__len__()):
        print(matrixR[i])


giveHelp()
while True:
        n = input("\n\tPress 'H' for help\n")
        if n.strip() == "0":
            break
        if n.strip() == "1":
            printAdjList()
        if n.strip() == "6":
            BreadthFirst()
        if n.strip() == "7":
            Reachability()
        if n.strip() == "H":
            giveHelp()
        if n.strip() == "3":
            addVertex()
        if n.strip() == "3-":
            removeVertex()
        if n.strip() == "4":
            addEdge()
        if n.strip() == "4-":
            removeEdge() 
        if n.strip() == "0": 
            break 
 