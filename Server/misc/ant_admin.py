from misc.list_node import ListNode
from misc.tree import Tree


class AntAdmin:

    def __init__(self, trees, speed=1):
        '''
        E: Array de árboles y la velocidad (segundos por cuadro) de las hormigas (sólo números enteros)
        S: N/A
        F: Instancia un administrador de hormiguero
        '''

        self.trees = trees.copy()  # Se copia el array de árboles para no alterar los originales
        self.trees_dict = {}  # Diccionario que va a guardar el nombre de cada árbol y su posición en el array

        for pos in range(0, len(trees)):
            tree = trees[pos]
            tree.set_speed(speed)
            self.trees_dict[tree.name] = pos

        self.speed = speed

        #  Lista de los últimos índices usados por cada árbol
        self.first_available_indexes = {}
        self.queue = [ListNode()]  #  Cola de salida de las hormigas
        # Diccionario que guarda las restricciones por agregar pendientes
        self.restrictions_list = {}

    def send_ants(self, ant_list):
        '''
        E: Recibe una lista de hormigas (índices a árboles)
        S: N/A
        F: Agrega en bloque un conjunto de hormigas a la cola
        '''
        for ant in ant_list:
            self.send_ant_to_tree(ant)

    def _irrespected_restrictions(self, tree_index, index):
        '''
        E: Índice del árbol, índice del nodo a ocupar
        S: True si hay alguna violación a las restricciones, si no False
        F: Antes de ocupar un nodo busca si habría algún conflicto con sus restricciones
        '''
        tree = self.trees[tree_index]
        for restriction in tree.other_trees_reference:
            target_index = index + restriction.weight

            if target_index < len(self.queue) and tree_index in self.queue[target_index].restrictions:
                return True

        return False

    def _add_node(self):
        '''
        E: N/A
        S: Restricciones del nuevo nodo
        F: Agrega un nuevo nodo en la cola y agrega sus restricciones si estaban pendientes
        '''
        restrictions = []
        new_index = len(self.queue)

        if new_index in self.restrictions_list.keys():
            restrictions = self.restrictions_list[new_index]
            del self.restrictions_list[new_index]

        self.queue.append(ListNode())
        self.queue[new_index].restrictions = restrictions
        return restrictions

    def _update_index(self, tree_index):
        '''
        E: Índice de un árbol
        S: Primer índice utilizable para ese árbol
        F: Recorre desde la última posición buscando cuál es el primer spot libre para el árbol
        '''
        index = self.first_available_indexes[tree_index]
        node = self.queue[index]

        while index < len(self.queue) - 1 and (
                node.busy or tree_index in node.restrictions or self._irrespected_restrictions(tree_index, index)):
            index += 1
            node = self.queue[index]

        if index == len(self.queue) - 1 and (
                node.busy or tree_index in node.restrictions or self._irrespected_restrictions(tree_index, index)):
            restrictions = self._add_node()
            index += 1

            while tree_index in restrictions:
                restrictions = self._add_node()
                index += 1

        self.first_available_indexes[tree_index] = index
        return index

    def _add_restrictions(self, tree_index, index):
        '''
        E: tree_index -> Índice de un árbol, index -> Índice del nuevo nodo que se está agregando
        S: N/A
        F: Actualiza las restricciones de los campos libres del queue. Deja pendientes si es necesario
        '''
        restrictions = self.trees[tree_index].other_trees_reference

        for restriction in restrictions:
            target_index = index + restriction.weight
            if target_index > len(self.queue):
                if target_index not in self.restrictions_list.keys():
                    self.restrictions_list[target_index] = []

                # TODO: Estoy agregando mal el índice, no puede ser el tree_index sino el índice del árbol en el restriction
                restriction_index = self.trees_dict[restriction.to.name]

                if not restriction_index in self.restrictions_list[target_index]:
                    self.restrictions_list[target_index].append(restriction_index)

    def send_ant_to_tree(self, tree_index):
        '''
        E: Índice de un árbol
        S: N/A
        F: Agrega una hormiga a la cola del hormiguero
        '''
        if not tree_index in self.first_available_indexes.keys():
            self.first_available_indexes[tree_index] = 0

        index = self._update_index(tree_index)

        self.queue[index].set_target(tree_index)
        self._add_restrictions(tree_index, index)

    def close_loop(self):
        '''
        E: N/A
        S: La cantidad de veces que se repiten las hormigas para no perder tiempo dentro del hormiguero
        F: Define cuántos espacios hay que dejar detrás de la última hormiga para poder volver a ejecutar el ciclo
        '''
        finished = False
        while not finished:
            finished = True
            length = len(self.queue)
            for key, restrictions in self.restrictions_list.items():
                key = key % length
                for restriction in restrictions:
                    if self.queue[key].target == restriction:
                        self._add_node()
                        finished = False
                        break
                if not finished:
                    break
        # print("While closing loop:", len(self.queue))

        max_back_time = 0
        max_back_time_index = 0
        for index in range(0, len(self.queue)):
            node = self.queue[index]
            if node.target != None:
                back_time = node.set_back_time(self.trees[node.target], index)
                if back_time > max_back_time:
                    max_back_time = back_time
                    max_back_time_index = index

        # print("Max back time:", max_back_time)
        # print("Max back time index:", max_back_time_index)
        # print("Tree wait time:",
        #      self.trees[self.queue[max_back_time_index].target].total_distance)
        wait_time = max_back_time - (len(self.queue) - 1 - max_back_time_index)
        # print("Wait time:", wait_time)
        if wait_time <= 0:
            return 0

        times = int(wait_time / len(self.queue))
        target_index = wait_time % len(self.queue)

        if target_index > max_back_time_index:  # En caso de que del todo no le de tiempo de llegar a su posición, se aumenta en uno el multiplicador
            times += 1

        self.queue += times * self.queue

        return times

    def analysis_count(self, pTime):
        '''
        E: Tiempo en segundos
        S: Tupla (cant hormigas, cant hojas)
        F: Cuenta la cantidad de hormigas y la cantidad de hojas que se obtendrán al final de la simulación
        '''
        for tree in self.trees:
            tree.restart_temp_leaves_count()

        complete_iterations = int(pTime / len(self.queue))
        # print("Complete iterations:", complete_iterations)

        last_index = pTime % len(self.queue)
        # print("Last index:", last_index)

        ant_count = 0
        leaf_count = 0
        for index in range(0, len(self.queue) if len(self.queue) < pTime else pTime):
            node = self.queue[index]
            if node.busy:
                ant_count += 1
                temp_leaf_count = complete_iterations + (1 if index < last_index else 0)
                tree_leaf_count = self.trees[node.target].temp_leaves_count

                if tree_leaf_count < temp_leaf_count:
                    temp_leaf_count = tree_leaf_count

                self.trees[node.target].temp_leaves_count -= temp_leaf_count
                leaf_count += temp_leaf_count

        return ant_count, leaf_count

    @staticmethod
    def evaluate(trees, ants, speed, pTime):
        '''
        Esta es la función que se usaría en los algoritmos
        E: Lista de árboles, lista de hormigas, velocidad en segundos por cuadro (cuántos segundos dura una hormiga en recorrer un cuadro), tiempo en segundos para ver cuántas hojas se logran recolectar en ese intervalo
        S: Objeto con los resultados del análisis y el loop que se debe utilizar en la simulación
        '''
        Tree.add_trees_dependencies(trees)
        ant_admin = AntAdmin(trees, speed)

        ant_admin.send_ants(ants)

        # print("Before loop closed: ", len(ant_admin.queue))
        times = ant_admin.close_loop()

        # print("Times:", times)
        # print("After loop closed: ", len(ant_admin.queue))
        # print("Loop: ")

        loop = []
        for node in ant_admin.queue:
            loop.append(node.target if node.target != None else "_")

        # print("\n")
        results = ant_admin.analysis_count(pTime)
        # print("Results" ,results)

        return {"ant_count": results[0], "leaf_count": results[1], "loop": loop}
