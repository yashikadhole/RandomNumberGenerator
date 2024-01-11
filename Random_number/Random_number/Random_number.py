import nextpy as xt
import random

class RandomNumber(xt.State):
    min_value: int = 0
    max_value: int = 100
    random_number: int = 0
    def generate_random_number(self):
        self.random_number = random.randint(self.min_value, self.max_value)

# Construct the filename to display 
from xtconfig import config
filename = f"{config.app_name}/{config.app_name}.py"


randum_gen=RandomNumber()
# define index page. Frontend Pages are just functions that return a frontend components
def index() -> xt.Component:
    return xt.fragment(
        xt.vstack(
            xt.text(
                "Random Number Generator".upper(),
                color="#F3F5F7",
                font_size="28px",
                padding="12px",
                max_width="620px",
                class_name="mx-auto mt-5",  # Center the text and add top margin
            ),
            xt.text(
                "Minmum Number",
                color="#F3F5F7",
                font_size="20px",
                padding="12px",
                max_width="300px",
                class_name="mx-auto mt-5",
            ),
            xt.form(
                xt.form_control(
                    
                    xt.number_input(
                        placeholder="Enter Minimum Value",
                        id="min_value",
                        value=RandomNumber.min_value,
                        on_change=RandomNumber.set_min_value,
                        variant="unstyled",
                        background_color="white",
                        border_style="solid",
                        border_color="#23262f",
                        p="0.75rem",
                        border_width="2px",
                        border_radius="0.5rem",
                        class_name="mb-3",  # Add bottom margin
                    )
                ),
                xt.text(
                    "Maximum Number",
                    color="#F3F5F7",
                    font_size="20px",
                    padding="12px",
                    max_width="300px",
                    class_name="mx-auto mt-5",
                ),
                xt.form_control(
                    xt.number_input(
                        placeholder="Enter Maximum Value",
                        value=RandomNumber.max_value,
                        on_change=RandomNumber.set_max_value,
                        id="max_value",
                        variant="unstyled",
                        background_color="white",
                        border_style="solid",
                        border_color="#23262f",
                        p="0.75rem",
                        border_width="2px",
                        border_radius="0.5rem",
                        class_name="mb-3",  # Add bottom margin
                    )
                ),
                xt.button(
                    "Generate Random Number",
                    on_click=RandomNumber.generate_random_number,
                    variant="unstyled",
                    background_color= "#f44336",
                    py="0.5rem",
                    px="1.5rem",
                    border_radius="9999px",
                    width="100%",
                    class_name="mb-3",  # Add bottom margin
                ),
            ),
            xt.text(
                f"Random Number: {RandomNumber.random_number}",
                font_size="18px",
                color="#3b71fe",
                py="1rem",
            ),

            height="100vh",  # Full viewport height
            background="#04090B",  # Background color
            padding_top="10%",  # Top padding percentage for responsive design
        ),
    )

# Global styles defined as a Python dictionary
style = {
    "text_align": "center", 
    "margin": "0",
    "padding": "0",
    "box-sizing": "border-box",
}

app = xt.App(style=style)
app.add_page(index)