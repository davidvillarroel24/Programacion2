import flet as ft

def main(page: ft.Page):
    page.title = "Ejemplo de DataTable"
    data=[["Ana","19"],
          ["Pedro","23"],
          ["juan","25"],
          ["Eddy","19"],
          ["Ivan","20"]
          ]
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Nombre")),
            ft.DataColumn(label=ft.Text("Edad")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Ana")),
                    ft.DataCell(ft.Text("23")),
                ]
            )
        ],
        border_radius=10, 
        #bgcolor=ft.Colors.BLUE_50,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(2,ft.Colors.BLACK),
        divider_thickness=10
    )

    page.add(tabla)

ft.app(target=main)


    

