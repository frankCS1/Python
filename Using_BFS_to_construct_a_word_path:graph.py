from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjlist = defaultdict(list)

    def add_edge(self, word1, word2):
        self.adjlist[word1].append(word2)

    def bfs(self, start_word, end_word):
        #Checks if word is in graph return None
        if start_word not in self.adjlist or end_word not in self.adjlist:
            return None

        visited = set()  #Tracking visted words
        queue = deque([(start_word, [start_word])])  #Starting word

        while queue:
            currentword, path = queue.popleft()  #Amends list, adds the word
            if currentword == end_word:
                return path  #Returns the list 

            if currentword not in visited:
                visited.add(currentword)  #Marks visited words
                for neighbor in self.adjlist[currentword]:
                    queue.append((neighbor, path + [neighbor]))  #Add neighboring words to the queue

        return None  #If no path is found

def graphword(sentence):
    words = sentence.split()  #Splits sentence to words
    graph = Graph()  #Create a graph
    for i in range(len(words) - 1):  #Loops through all words except the last one
        graph.add_edge(words[i], words[i + 1])  #Adds an edge from current word to next word
    return graph  #Returns the constructed graph

#User input
sentence = input("Input the sentence: ")
start_word = input("Input the starting word: ")
end_word = input("Input the ending word: ")

#Contructs the graph using BFS
word_graph = graphword(sentence)
path = word_graph.bfs(start_word, end_word)

#Result
if path:
    if len(path) > 30:
        y_n = input("Do you want to print the whole path?: ")
        if y_n.lower() == "yes":
            print("The path is:", path)
        else:
            print("The length of the path is:", len(path))
    else:
        print("The path is:", path)
else:
    print("No path found")
