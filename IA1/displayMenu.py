import utils
import hill_climbing
import simulated_annealing
import tabu_search
import genetic_algorithm
import greedy
import classes
import antcolony

def display(solution): 
    print("---------------------------------------------------------------")    
    print(f"\nTotal Score: {solution.get_value(solution.current_day)[0]}")
    print("---------------------------------------------------------------")

def display_file(solution): 
    with open('output.txt', 'w') as f:
        f.write("---------------------------------------------------------------\n")
        f.write(f"Number of libraries explored: {len(solution.library_explored)}\n")
        
        for library in solution.library_explored:
            # Check if library id exists in the dictionary
            if library.id in solution.books_explored:
                f.write(f"\nLibrary {library.id} - Books Explored: {len(solution.books_explored[library.id])}\n")
                
                # Join all book ids into a string separated by space and write to file
                books = ' '.join(str(book) for book in solution.books_explored[library.id])
                f.write(books + '\n')
        
        f.write(f"\nTotal Score: {solution.get_value(solution.current_day)[0]}\n")
        f.write("---------------------------------------------------------------\n")

def run_initial_solution_first(libraries,book_scores,days,initial_solution):
    if initial_solution == 'random_solution':
        initial_solution_random = utils.random_solution(libraries, book_scores, days)
    elif initial_solution == 'random_solution_per_signup':
        initial_solution_random = utils.random_solution_per_signup(libraries, book_scores, days)
    elif initial_solution == 'greedy_solution':
        empty_solution = classes.State([], {}, book_scores, [], 0)
        initial_solution_random = greedy.greedy_solution(empty_solution,libraries, book_scores, days)
    return initial_solution_random

def choose_initial_solution_first():
    initial_solutions = ["random_solution", "random_solution_per_signup", "greedy_solution"]
    while True: 
        print("Choose an initial solution:")
        for i, solution in enumerate(initial_solutions, start=1):
            print(f"{i}. {solution}")
        solution_choice = input("Enter your choice: ")
        if not solution_choice.isdigit() or int(solution_choice) < 1 or int(solution_choice) > len(initial_solutions):
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue
        initial_solution = initial_solutions[int(solution_choice) - 1]
        return initial_solution
    
def run_initial_solution(libraries,book_scores,days,initial_solution):
    if initial_solution == 'random_solution':
        initial_solution_random = utils.random_solution(libraries, book_scores, days)
    elif initial_solution == 'random_solution_per_signup':
        initial_solution_random = utils.random_solution_per_signup(libraries, book_scores, days)
    elif initial_solution == 'greedy_solution':
        empty_solution = classes.State([], {}, book_scores, [], 0)
        initial_solution_random = greedy.greedy_solution(empty_solution,libraries, book_scores, days)
    return initial_solution_random

def choose_initial_solution():
    initial_solutions = ["random_solution", "random_solution_per_signup", "greedy_solution"]
    while True: 
        print("Choose an initial solution:")
        for i, solution in enumerate(initial_solutions, start=1):
            print(f"{i}. {solution}")
        solution_choice = input("Enter your choice: ")
        if not solution_choice.isdigit() or int(solution_choice) < 1 or int(solution_choice) > len(initial_solutions):
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue
        initial_solution = initial_solutions[int(solution_choice) - 1]
        return initial_solution


def run_another_algorithm_with_solution(libraries, book_scores, days, initial_solution):
    while True:
        print("Running another algorithm...")
        print("1. Hill Climbing")
        print("2. Hill Climbing First Accept")
        print("3. Simulated Annealing")
        print("4. Tabu Search")
        print("5. Genetic Algorithm")
        print("6. Ant Colony Optimization")
        print("7. Quit")
        choice = input("Enter your choice: ")
        if choice == "1": 
            best_solution_from_hill_climbing = hill_climbing.hill_climbing(initial_solution, days, libraries)
            return best_solution_from_hill_climbing
        elif choice == "2":
            best_solution_from_hill_climbing = hill_climbing.hill_climbing_first_accept(initial_solution, days, libraries)
            return best_solution_from_hill_climbing
        elif choice == "3":
            while True:
                try:
                    cooling_rate = float(input("Enter the cooling rate (between 0 and 1): "))
                    if cooling_rate <= 0 or cooling_rate >= 1:
                        raise ValueError("Cooling rate must be between 0 and 1.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

            while True:
                try:
                    max_iterations = int(input("Enter the maximum number of iterations: "))
                    if max_iterations < 0:
                        raise ValueError("Maximum iterations must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

            while True:
                try:
                    stop_temperature = float(input("Enter the stopping temperature: "))
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")
            best_solution_from_simulated_annealing = simulated_annealing.simulated_annealing(initial_solution, days, libraries, cooling_rate, max_iterations, stop_temperature)
            return best_solution_from_simulated_annealing
        elif choice == "4":
            while True:
                try:
                    tabu_size = int(input("Enter the tabu size: "))
                    if tabu_size <= 0:
                        raise ValueError("Tabu size must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

            while True:
                try:
                    limited = int(input("Enter 0 for unlimited neighbors or a number higher than 1 for limited neighbors: "))
                    if limited < 0:
                        raise ValueError("Limited neighbors must be 0 or a number higher than 1.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

            while True:
                try:
                    max_iterations = int(input("Enter the maximum number of iterations: "))
                    if max_iterations <= 0:
                        raise ValueError("Maximum iterations must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")
            best_solution_from_tabu_search = tabu_search.tabu_search(initial_solution, tabu_size, max_iterations, libraries,limited)
            return best_solution_from_tabu_search
        elif choice == "5":
            while True:
                try:
                    number_generations = int(input("Enter the number of generations: "))
                    if number_generations <= 0:
                        raise ValueError("Number of generations must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

            while True:
                try:
                    population_size = int(input("Enter the population size: "))
                    if population_size <= 0:
                        raise ValueError("Population size must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

            while True:
                try:
                    mutation_rate = float(input("Enter the mutation rate (between 0 and 1): "))
                    if mutation_rate < 0 or mutation_rate > 1:
                        raise ValueError("Mutation rate must be between 0 and 1.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

                tournament_size = 0
            while True:
                try:
                    selected = int(input("Enter 0 for roulette selection or 1 for tournament selection: "))
                    if selected not in [0, 1]:
                        raise ValueError("Selection must be either 0 or 1.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

                if selected == 1:
                    while True:
                        try:
                            tournament_size = int(input("Enter the tournament size: "))
                            if tournament_size <= 0:
                                raise ValueError("Tournament size must be a positive integer.")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}")
            population = [utils.random_solution(libraries, book_scores, days) for _ in range(population_size)]
            best_solution_from_genetic_algorithm = genetic_algorithm.genetic_algorithm(population, days, number_generations, tournament_size, mutation_rate,libraries,selected)
            return best_solution_from_genetic_algorithm
        elif choice == "6":
            while True:
                try:
                    num_iterations = int(input("Enter the number of iterations: "))
                    if num_iterations <= 0:
                        raise ValueError("Number of iterations must be a positive integer.") 
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

            while True:
                try:
                    num_ants = int(input("Enter the number of ants: "))
                    if num_ants <= 0:
                        raise ValueError("Number of ants must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

            while True:
                try:
                    evaporation_rate = float(input("Enter the evaporation rate: "))
                    if evaporation_rate < 0 or evaporation_rate > 1:
                        raise ValueError("Evaporation rate must be between 0 and 1.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

            while True:
                try:
                    initial_pheromone = float(input("Enter the initial pheromone: "))
                    if initial_pheromone < 0:
                        raise ValueError("Initial pheromone must be a positive number.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

            while True:
                try:
                    alpha = float(input("Enter the alpha value: "))
                    if alpha < 0:
                        raise ValueError("Alpha must be a positive number.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

            while True:
                try:
                    beta = float(input("Enter the beta value: "))
                    if beta < 0:
                        raise ValueError("Beta must be a positive number.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")
            best_solution_from_ant_colony = antcolony.ant_colony_optimization(libraries, book_scores, days, num_iterations, num_ants, evaporation_rate, initial_pheromone, alpha, beta)
            return best_solution_from_ant_colony
        elif choice == "7":
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def loop_back(libraries,book_scores,days,initial_solution):
    while True:
        print("Want to run again ?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == '1':
            best_solution = run_another_algorithm_with_solution(libraries,book_scores,days,initial_solution)
            display_file(best_solution)
            display(best_solution)
        elif choice == '2':
            break
        else:
            print("Invalid choice")


def main():
    files = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
    initial_solutions = ["random_solution", "random_solution_per_signup", "greedy_solution"]
    while True:
        print("Menu:")
        print("1. Hill Climbing")
        print("2. Hill Climbing First Accept")
        print("3. Simulated Annealing")
        print("4. Tabu Search")
        print("5. Genetic Algorithm")
        print("6. Ant Colony Optimization")
        print("7. Quit")
        choice = input("Enter your choice: ")

        if choice in ['1', '2', '3', '4','5','6']:
            print("Choose a file:")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")
            file_choice = input("Enter your choice: ")
            if not file_choice.isdigit() or int(file_choice) < 1 or int(file_choice) > len(files):
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue
            file_name = files[int(file_choice) - 1]
            if choice in ['1', '2', '3', '4','5']:
                initial_solution = choose_initial_solution_first()
                if choice == '1':
                    libraries, book_scores, days = utils.readFile(file_name)
                    initial_solution_random = run_initial_solution_first(libraries,book_scores,days,initial_solution)
                    best_solution_from_hill_climbing = hill_climbing.hill_climbing(initial_solution_random, days, libraries)
                    display_file(best_solution_from_hill_climbing)
                    display(best_solution_from_hill_climbing)
                    loop_back(libraries,book_scores,days,best_solution_from_hill_climbing)
                elif choice == '2':
                    # Run Hill Climbing
                    libraries, book_scores, days = utils.readFile(file_name)
                    initial_solution_random = run_initial_solution_first(libraries,book_scores,days,initial_solution)
                    best_solution_from_hill_climbing = hill_climbing.hill_climbing_first_accept(initial_solution_random, days, libraries)
                    total_score = utils.get_values_from_dict(best_solution_from_hill_climbing.books_explored, book_scores)
                    display_file(best_solution_from_hill_climbing)
                    loop_back(libraries,book_scores,days,best_solution_from_hill_climbing)
                elif choice == '3':
                    try:
                        # Run Simulated Annealing
                        libraries, book_scores, days = utils.readFile(file_name)
                        initial_solution_random = run_initial_solution_first(libraries,book_scores,days,initial_solution)
                        
                        while True:
                            try:
                                cooling_rate = float(input("Enter the cooling rate (between 0 and 1): "))
                                if cooling_rate <= 0 or cooling_rate >= 1:
                                    raise ValueError("Cooling rate must be between 0 and 1.")
                                break
                            except ValueError as e:
                                print(f"Invalid input: {e}")

                        while True:
                            try:
                                max_iterations = int(input("Enter the maximum number of iterations: "))
                                if max_iterations < 0:
                                    raise ValueError("Maximum iterations must be a positive integer.")
                                break
                            except ValueError as e:
                                print(f"Invalid input: {e}")

                        while True:
                            try:
                                stop_temperature = float(input("Enter the stopping temperature: "))
                                break
                            except ValueError as e:
                                print(f"Invalid input: {e}")
                        best_solution_from_simulated_annealing = simulated_annealing.simulated_annealing(initial_solution_random, days, libraries, cooling_rate, max_iterations, stop_temperature)
                        display_file(best_solution_from_simulated_annealing)
                        display(best_solution_from_simulated_annealing)
                        loop_back(libraries,book_scores,days,best_solution_from_simulated_annealing)
                    except ValueError as e:
                        print(f"Invalid input: {e}")
                elif choice == '4':
                    try:
                        # Run Tabu Search
                        libraries, book_scores, days = utils.readFile(file_name)
                        initial_solution_random = run_initial_solution_first(libraries,book_scores,days,initial_solution)
                        
                        while True:
                            try:
                                tabu_size = int(input("Enter the tabu size: "))
                                if tabu_size <= 0:
                                    raise ValueError("Tabu size must be a positive integer.")
                                break
                            except ValueError as e:
                                print(f"Invalid input: {e}")

                        while True:
                            try:
                                limited = int(input("Enter 0 for unlimited neighbors or a number higher than 1 for limited neighbors: "))
                                if limited < 0:
                                    raise ValueError("Limited neighbors must be 0 or a number higher than 1.")
                                break
                            except ValueError as e:
                                print(f"Invalid input: {e}")

                        while True:
                            try:
                                max_iterations = int(input("Enter the maximum number of iterations: "))
                                if max_iterations <= 0:
                                    raise ValueError("Maximum iterations must be a positive integer.")
                                break
                            except ValueError as e:
                                print(f"Invalid input: {e}")

                        best_solution_from_tabu_search = tabu_search.tabu_search(initial_solution_random, tabu_size, max_iterations, libraries,limited)
                        display_file(best_solution_from_tabu_search)
                        display(best_solution_from_tabu_search)
                        loop_back(libraries,book_scores,days,best_solution_from_tabu_search)
                    except ValueError as e:
                        print(f"Invalid input: {e}")

                elif choice == '5':
                    # Run Genetic Algorithm
                    libraries, book_scores, days = utils.readFile(file_name)
                    initial_solution_random = run_initial_solution_first(libraries,book_scores,days,initial_solution)
                    
                    while True:
                        try:
                            number_generations = int(input("Enter the number of generations: "))
                            if number_generations <= 0:
                                raise ValueError("Number of generations must be a positive integer.")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}")

                    while True:
                        try:
                            population_size = int(input("Enter the population size: "))
                            if population_size <= 0:
                                raise ValueError("Population size must be a positive integer.")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}")

                    while True:
                        try:
                            mutation_rate = float(input("Enter the mutation rate (between 0 and 1): "))
                            if mutation_rate < 0 or mutation_rate > 1:
                                raise ValueError("Mutation rate must be between 0 and 1.")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}")

                    tournament_size = 0
                    while True:
                        try:
                            selected = int(input("Enter 0 for roulette selection or 1 for tournament selection: "))
                            if selected not in [0, 1]:
                                raise ValueError("Selection must be either 0 or 1.")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}")

                    if selected == 1:
                        while True:
                            try:
                                tournament_size = int(input("Enter the tournament size: "))
                                if tournament_size <= 0:
                                    raise ValueError("Tournament size must be a positive integer.")
                                break
                            except ValueError as e:
                                print(f"Invalid input: {e}")

                    population = [utils.random_solution(libraries, book_scores, days) for _ in range(population_size)]
                    best_solution_from_genetic_algorithm = genetic_algorithm.genetic_algorithm(population, days, number_generations, tournament_size, mutation_rate,libraries,selected)
                    display_file(best_solution_from_genetic_algorithm)
                    display(best_solution_from_genetic_algorithm)
                    loop_back(libraries,book_scores,days,best_solution_from_genetic_algorithm)
            elif choice == '6':
                try:
                    # Run the Ant Colony Algorithm
                    libraries, book_scores, days = utils.readFile(file_name)
                    
                    while True:
                        try:
                            num_iterations = int(input("Enter the number of iterations: "))
                            if num_iterations <= 0:
                                raise ValueError("Number of iterations must be a positive integer.") 
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}")

                    while True:
                        try:
                            num_ants = int(input("Enter the number of ants: "))
                            if num_ants <= 0:
                                raise ValueError("Number of ants must be a positive integer.")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}")

                    while True:
                        try:
                            evaporation_rate = float(input("Enter the evaporation rate: "))
                            if evaporation_rate < 0 or evaporation_rate > 1:
                                raise ValueError("Evaporation rate must be between 0 and 1.")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}")

                    while True:
                        try:
                            initial_pheromone = float(input("Enter the initial pheromone: "))
                            if initial_pheromone < 0:
                                raise ValueError("Initial pheromone must be a positive number.")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}")

                    while True:
                        try:
                            alpha = float(input("Enter the alpha value: "))
                            if alpha < 0:
                                raise ValueError("Alpha must be a positive number.")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}")

                    while True:
                        try:
                            beta = float(input("Enter the beta value: "))
                            if beta < 0:
                                raise ValueError("Beta must be a positive number.")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}")

                    best_solution_from_ant_colony = antcolony.ant_colony_optimization(libraries, book_scores, days, num_iterations, num_ants, evaporation_rate, initial_pheromone, alpha, beta)
                    display_file(best_solution_from_ant_colony)
                    display(best_solution_from_ant_colony)
                    loop_back(libraries,book_scores,days,best_solution_from_ant_colony)
                except ValueError as e:
                    print(f"Invalid input: {e}")
        elif choice == '7':
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()