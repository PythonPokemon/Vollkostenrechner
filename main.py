from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CostCalculator(App):
    def build(self):
        self.title = "Vollkostenrechner für Stuhlproduktion"

        root_layout = GridLayout(cols=2, spacing=10, padding=10)

        # Labels und Eingabefelder für die Kostenarten
        root_layout.add_widget(Label(text="Fixe Kosten (Miete der Produktionsstätte):"))
        self.fixed_cost_input = TextInput(hint_text="1000", input_filter="float")
        root_layout.add_widget(self.fixed_cost_input)

        root_layout.add_widget(Label(text="Fixe Kosten (Gehälter der Mitarbeiter):"))
        self.salary_cost_input = TextInput(hint_text="4000", input_filter="float")
        root_layout.add_widget(self.salary_cost_input)

        root_layout.add_widget(Label(text="Variable Kosten (Materialien pro Stuhl):"))
        self.material_cost_input = TextInput(hint_text="15", input_filter="float")
        root_layout.add_widget(self.material_cost_input)

        root_layout.add_widget(Label(text="Variable Kosten (Energiekosten pro Stuhl):"))
        self.energy_cost_input = TextInput(hint_text="5", input_filter="float")
        root_layout.add_widget(self.energy_cost_input)

        # Label und Eingabefeld für die Anzahl der produzierten Stühle
        root_layout.add_widget(Label(text="Anzahl der produzierten Stühle:"))
        self.unit_count_input = TextInput(hint_text="100", input_filter="int")
        root_layout.add_widget(self.unit_count_input)

        # Button zum Berechnen der Kosten
        calculate_button = Button(text="Kosten berechnen")
        calculate_button.bind(on_press=self.calculate_costs)
        root_layout.add_widget(calculate_button)

        # Ergebnisanzeige
        self.result_label = Label(text="", size_hint=(None, None))
        root_layout.add_widget(self.result_label)

        return root_layout

    def calculate_costs(self, instance):
        try:
            fixed_costs = float(self.fixed_cost_input.text)
            salary_costs = float(self.salary_cost_input.text)
            material_cost_per_unit = float(self.material_cost_input.text)
            energy_cost_per_unit = float(self.energy_cost_input.text)
            unit_count = int(self.unit_count_input.text)
        except ValueError:
            self.result_label.text = "Fehler: Bitte geben Sie gültige Zahlen ein."
            return

        # Kostenberechnung
        variable_costs = (material_cost_per_unit + energy_cost_per_unit) * unit_count
        production_department_costs = variable_costs
        administration_department_costs = (fixed_costs + salary_costs) * 0.8  # 80% für Verwaltungsabteilung

        total_costs = production_department_costs + administration_department_costs
        cost_per_unit = total_costs / unit_count

        result_text = f"Gesamtkosten: {total_costs:.2f} EUR\n"
        result_text += f"Kosten pro Einheit: {cost_per_unit:.2f} EUR/Stuhl"

        self.result_label.text = result_text

if __name__ == "__main__":
    CostCalculator().run()
