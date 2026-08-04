import flet as ft

def saludar(e):
    print("hola mundo!")




def main(page: ft.Page):
    page.title = "mi primera app con flet"

    mensaje = ft.Text("aqui va un mensaje!")
    nombre = ft.TextField(label="Nombre", autofocus=True)


    def mostrar_mensaje(e):
        dialogo = ft.AlertDialog(
            title=ft.Text("Hola!"),
            content=ft.Text(txt_mensaje)
        )
        page.show_dialog(dialogo)

    def saludar(e):
        if nombre.value == "":
            mensaje.value = "Por favor ingresa tu nombre"

        else:
            mensaje.value = "hola, " + nombre.value
            #page.update()
            mostrar_mensaje(mensaje.value) #pin seletor to cur

    page.add(
        ft.Text("Escribe tu nombre: "),
        ft.Button("click aqui!", on_click = saludar),
        mensaje,
        nombre
    )


ft.run(main)