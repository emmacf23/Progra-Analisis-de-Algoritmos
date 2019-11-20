from misc.tree_reference import TreeReference
class Tree():
    
    def __init__(self, name, x, levels, base_size = 1, percentage = 1):
        '''
        E: Nombre para el HTML, el X con respecto al hormiguero, cantidad de niveles, el tamaño base del árbol y el porcentaje de crecimiento
        S: N/A
        F: Instancia el objeto árbol
        '''

        self.name = name
        self.x = x
        
        self.levels = levels
        self.base_size = base_size
        self.precentage = percentage

        height = base_size
        lastHeight = base_size
        for level in range(1, levels):
            lastHeight = lastHeight * percentage
            height += lastHeight

        height = round(height) # Obtiene la altura redondeada para que sea de formato entero
        self.height = height
        self.distance_to_road = x + 2 * height + 1
        self.total_distance = self.distance_to_road + x - 1
        self.other_trees_reference = [] # Las referencias tienen la relación entre árboles y restricciones
        self.leaves_count = pow(2, levels - 1)
        self.temp_leaves_count = self.leaves_count

    def __repr__(self):
        return '{}: {} {} {} {} {}'.format(self.__class__.__name__,
                                           self.name,
                                           self.x,
                                           self.levels,
                                           self.base_size,
                                           self.precentage)
    
    def set_speed(self, speed):
        '''
        E: Velocidad en segundos por cuadro de las hormigas
        S: N/A
        F: Actualiza los valores del árbol para simular que la hormiga se mueve a la velocidad dada
        '''
        self.total_distance *= speed
        self.height *= speed
        self.distance_to_road *= speed
    
    def restart_temp_leaves_count(self):
        '''
        E: N/A
        S: N/A
        F: Reestablece el conteo temporal de hojas
        '''
        self.temp_leaves_count = self.leaves_count
    
    def add_reference(self, other_tree):
        '''
        E: Objeto Tree
        S: N/A
        F: Establece una restricción entre árboles
        '''
        reference = TreeReference(self, other_tree)
        
        if reference.weight > 0:
            self.other_trees_reference.append(reference)

    @staticmethod
    def add_dependencies(trees_array):
        '''
        E: Array de árboles
        S: N/A
        F: Calcula todas las dependencias entre los árboles y agrega sus referencias
        '''
        for tree_index in range(1, len(trees_array)):
            tree = trees_array[tree_index]
            for child_index in range(0, tree_index):
                tree.add_reference(trees_array[child_index])
    
    @staticmethod
    def add_trees_dependencies(trees):
        '''
        E: Lista de árboles
        S: N/A
        F: Agrega las dependencias de todos los árboles sin desordenar la lista
        '''
        trees_copy = trees.copy()
        trees_copy.sort(key=lambda tree: tree.total_distance)
        Tree.add_dependencies(trees_copy)
