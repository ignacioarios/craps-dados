import random

# Clase para el simulador de lanzamiento de dados
class DiceSimulator:
    def __init__(self):
        self.user_results = []  # Almacena los resultados del usuario
        self.team_results = []  # Almacena los resultados de N. Rivers Development

    def roll_dice(self):
        # Lanza dos dados para el usuario y dos para N. Rivers Development
        user_dice = random.randint(1, 6) + random.randint(1, 6)
        team_dice = random.randint(1, 6) + random.randint(1, 6)
        
        # Guarda los resultados
        self.user_results.append(user_dice)
        self.team_results.append(team_dice)

    def determine_winner(self, user_score, team_score):
        if user_score > team_score:
            return "¡Ganaste!"
        elif user_score < team_score:
            return "N. Rivers Development ganó."
        else:
            return "Empate."

    def display_results(self):
        user_wins = sum(1 for result in self.user_results if result > self.team_results[self.user_results.index(result)])
        team_wins = sum(1 for result in self.team_results if result > self.user_results[self.team_results.index(result)])
        
        print("\nResultados de las tiradas:")
        print("Tus resultados:", self.user_results)
        print("Resultados de N. Rivers Development:", self.team_results)
        print(f"\nDe las últimas 5 partidas, usted ganó {user_wins} veces.")
        print(f"N. Rivers Development ganó {team_wins} veces.")
        
        if user_wins > team_wins:
            print("Usted ganó el set. Por esta vez la casa ha perdido")
        elif user_wins < team_wins:
            print("N. Rivers Development ganó el set. La casa siempre gana")
        else:
            print("El set terminó en empate. Todos ganamos xd")

def main():
    simulator = DiceSimulator()
    for _ in range(5):
        input("Presiona Enter para lanzar los dados...")
        simulator.roll_dice()
        
        user_score = simulator.user_results[-1]
        team_score = simulator.team_results[-1]
        
        print(f"Tus dados: {user_score}, Dados de N. Rivers Development: {team_score}")
        print(simulator.determine_winner(user_score, team_score))

    # Mostrar resultados después de 5 tiradas
    simulator.display_results()

if __name__ == "__main__":
    main()
