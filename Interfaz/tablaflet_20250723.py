import flet as ft


def main(page: ft.Page):
    data=[
        ["Ana","23"],
        ["Maria","25"],
        ["Luis","22"],
        ["Pedro","21"],
        ["Luis","23"],
        ["Ana", "23"],
        ["Maria", "25"],
        ["Luis", "22"],
        ["Pedro", "21"],
        ["Luis", "23"] ]

    page.title = "Mi primera app en Flet"
    tabla=ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Nombre")),
            ft.DataColumn(label=ft.Text("Edad")),
            ft.DataColumn(label=ft.Text("Acciones")),
            ft.DataColumn(label=ft.Text("estado")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(nombre)),
                    ft.DataCell(ft.Text(edad)),
                    ft.DataCell(ft.Row(controls=[ft.IconButton(ft.Icons.EDIT,),ft.IconButton(ft.Icons.DELETE)])),
                    ft.DataCell(ft.Checkbox()),
                ]
            )
        for nombre, edad in data]
    , width=400, divider_thickness=5, border_radius=10,heading_row_color=ft.Colors.BLUE_50,
        border=ft.border.all(2, ft.Colors.BLUE_900),
        horizontal_margin=12,)

    page.add(tabla)

ft.app(target=main)