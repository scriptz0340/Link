import flet as ft 

def main(page: ft.Page):
    challenge = ft.Text("Dating back to a 1974 Bell Labs memo, what two-word greeting is universally known as the classic first program written in almost every language?", size=30)
    
    def hint_button_click():
        page.add(
            ft.SafeArea(
                content=ft.AlertDialog(
                    title=ft.Text("Hint:"),
                    content=ft.Text("Try a quick google search. 😉\n\n(Click off to close)"),
                    open=True,
                )
            )
        )

    def submit_button_click(e: ft.Event[ft.Button]):
        evaluate(response_field.value)
        
        

    def evaluate(e):  
        if e == 'Hello, world!':
            page.add(
                ft.SafeArea(
                    content=ft.AlertDialog(
                        title=ft.Text("Congratulations! 🎉"),
                        content=ft.Text("You guessed correctly! 🥳 \n\n While most people associate it with the C programming language, it was actually first written in B (C's predecessor) in a 1972 internal memo titled A Tutorial Introduction to the Language B.\n\nIt became a global tradition after it was featured as the opening example in the seminal 1978 book, The C Programming Language, co-authored by Kernighan and Dennis Ritchie. \n\n(Click off to close)"),
                        open=True,
                    )
                )
            )
                
        else:
            page.add(
                ft.SafeArea(
                    content=ft.AlertDialog(
                        title=ft.Text("Incorrect. 😢"),
                        content=ft.Text("Please try again. 🔄\n\n(Click off to close)"),
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
            content=ft.Row(
                controls=[
                    response_field := ft.TextField(
                        key="response_field",
                        label="Response",
                        on_submit=submit_button_click,
                    ),
                    ft.Button(key="submit_button", content="Submit", on_click=submit_button_click),
                    ft.Button(key="hint_button", content="Hint", on_click=hint_button_click),
                    message := ft.Text()

                ]
    
            )
        )
    )


if __name__ == '__main__': # __name__ is a built in variable. when you run a file directly, python sets this variable to the text __main__. When another file imports this file, Python sets it to the file name instead. This checks to make sure you are calling the file directly.
    ft.run(main)