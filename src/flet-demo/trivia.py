import flet as ft 

def main(page: ft.Page):
    challenge = ft.Text("Dating back to a 1974 Bell Labs memo, what two-word greeting is universally known as the classic first program written in almost every language?", size=30)
    
    def hint():
        page.add(
            ft.SafeArea(
                content=ft.AlertDialog(
                    title=ft.Text("Hint:"),
                    content=ft.Text("Try a quick google search. 😉\n\n(Click off to close)"),
                    open=True,
                )
            )
        )

    def evaluate(e):  
        if e == 'Hello, world!':
            page.add(
                ft.SafeArea(
                    content=ft.AlertDialog(
                        title=ft.Text("Congratulations!"),
                        content=ft.Text("You guessed correctly! \n\n(Click off to close)"),
                        open=True,
                    )
                )
            )
                
        else:
            page.add(
                ft.SafeArea(
                    content=ft.AlertDialog(
                        title=ft.Text("Incorrect."),
                        content=ft.Text("Please try again.\n\n(Click off to close)"),
                        open=True,
                    )
                )
            )
    



    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=challenge,
                alignment=ft.Alignment.CENTER,
                padding=25,
            )
        )
    )

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content = ft.TextField(label="Response", hint_text="Enter your response.", autocorrect=False, show_cursor=True, on_submit=evaluate),
                
                alignment=ft.Alignment.CENTER,
                
            )
        )
    )

    page.add(
        ft.SafeArea(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.FilledButton(content="Hint", on_click=hint),
                    ft.FloatingActionButton(icon=ft.Icons.POST_ADD, on_click=evaluate)

                ]
            )
            
        )
    )

if __name__ == '__main__': # __name__ is a built in variable. when you run a file directly, python sets this variable to the text __main__. When another file imports this file, Python sets it to the file name instead. This checks to make sure you are calling the file directly.
    ft.run(main)