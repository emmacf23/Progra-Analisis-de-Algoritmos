start = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="X-UA-Compatible" content="ie=edge"><title>Test</title><style>table.display td {height: 30px;width: 30px;}table.display td.show {border: 1px solid black; box-shadow: brown 0 0 2px;}table.display td.ground {border: 1px solid green; height: 10px; box-shadow: green 0 0 4px;}table.display {border-collapse: collapse;}' + \
    '* {font-family: Helvetica, Arial, sans-serif;} table.output {border-collapse: collapse; margin-top: 30px;} table.output td{border: 1px solid black; text-align: center; padding: 3px;}table.output tr:nth-child(odd) {background-color: #ddd;} table.output th {border: 1px solid black; padding: 4px; text-align: center; background-color: #333; color: white;}' + \
    '</style></head><body><table class="display">'
end = '</table></body></html>'

def draw_to_html(trees):
    with open('index.html', 'w') as html:
        html.write(start)
        maxY = max(trees, key=lambda tree: tree.height).height + 1
        maxX = max(trees, key=lambda tree: tree.x).x
        matriz = [[None if y == maxY - 1 else False for x in range(0, maxX)] for y in range(0, maxY)]
        for t in trees:
            x = t.x - 1
            for y in range(1, t.height + 1):
                matriz[maxY - 1 - y][x] = True

        for fila in matriz:
            html.write("<tr>")
            for columna in fila:
                html.write("<td" + (" class=\"show\"" if columna == True else " class=\"ground\"" if columna == None else "") + "></td>")
            html.write("</tr>")

        html.write("<table class='output'><tr>")
        html.write("<th>Árbol</th>")
        html.write("<th>Posición X</th>")
        html.write("<th>Altura</th>")
        html.write("<th>Costo hasta camino de vuelta</th>")
        html.write("<th>Costo hasta hormiguero</th>")
        html.write("<th>Restricciones</th>")
        html.write("</tr>")
        for tree in trees:
            html.write("<tr>")
            html.write("<td>" + tree.name + "</td>")
            html.write("<td>" + str(tree.x) + "</td>")
            html.write("<td>" + str(tree.height) + "</td>")
            html.write("<td>" + str(tree.distance_to_road) + "</td>")
            html.write("<td>" + str(tree.total_distance) + "</td>")
            html.write("<td>")
            tree.other_trees_reference.sort(key=lambda ref: ref.to.name)
            for r in tree.other_trees_reference:
                html.write("<b>" + r.to.name + "</b>: ")
                html.write(str(r.weight) + "<br>")
            html.write("</td>")
            html.write("</tr>")

        html.write("</table>")

        
        html.write(end)