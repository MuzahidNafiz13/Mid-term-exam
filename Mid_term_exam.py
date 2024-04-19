class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

        Star_Cinema().entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)

        # Initialize the seats for the new show
        self._seats[show_id] = [[False for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, show_id, seats):
        # Check if the show ID is valid
        if show_id not in self._seats:
            raise ValueError(f"Invalid show ID: {show_id}")

        # Check if the seats are available
        for row, col in seats:
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                raise ValueError(f"Invalid seat: ({row}, {col})")
            if self._seats[show_id][row][col]:
                raise ValueError(f"Seat ({row}, {col}) is already booked.")

        for row, col in seats:
            self._seats[show_id][row][col] = True

    def view_show_list(self):
        return self._show_list

    def view_available_seats(self, show_id):
        # Check if the show ID is valid
        if show_id not in self._seats:
            raise ValueError(f"Invalid show ID: {show_id}")

        available_seats = []
        for row in range(self._rows):
            for col in range(self._cols):
                if not self._seats[show_id][row][col]:
                    available_seats.append((row, col))
        return available_seats


class ReplicaSystem:
    def __init__(self, star_cinema):
        self._star_cinema = star_cinema

    def view_all_shows(self):
        print("1. VIEW ALL SHOW TODAY")
        for hall in self._star_cinema.hall_list:
            print(f"Hall {hall._hall_no}:")
            for show in hall.view_show_list():
                print(f"- {show[1]}, SHOW_ID: {show[0]}, TIME: {show[2]} ")

    def view_available_seats(self, show_id, hall_no):
        print("2. VIEW AVAILABLE SEATS")
        try:
            print(f"ENTER SHOW_ID: {show_id}")
            available_seats = []
            for hall in self._star_cinema.hall_list:
                if hall._hall_no == hall_no:
                    available_seats = hall.view_available_seats(show_id)
                    break
            if not available_seats:
                print("No seats available for this show.")
            else:
                print("ALL THE SEATS AVAILABLE FOR", show_id)
                print(available_seats)
                print("AND IN A 2D MATRIX FORM")
                seat_matrix = [[False for _ in range(hall._cols)] for _ in range(hall._rows)]
                for row, col in available_seats:
                    seat_matrix[row][col] = 0
                for row in seat_matrix:
                    print(row)
        except ValueError as e:
            print(e)

    def book_seats(self, show_id, hall_no, num_tickets, seats):
        print("3. BOOK TICKET")
        try:
            print(f"ENTER SHOW_ID: {show_id}")
            print(f"ENTER NUMBER OF TICKETS: {num_tickets}")
            for hall in self._star_cinema.hall_list:
                if hall._hall_no == hall_no:
                    for row, col in seats:
                        hall.book_seats(show_id, [(row, col)])
                        print(f"THE SEAT ({row}, {col}) IS BOOKED FOR SHOW {show_id}")
                    return
            raise ValueError(f"Invalid hall number: {hall_no}")
        except ValueError as e:
            print(e)

    def run(self):
        while True:
            print("\n1. VIEW ALL SHOW TODAY")
            print("2. VIEW AVAILABLE SEATS")
            print("3. BOOK TICKET")
            print("4. EXIT")
            option = input("ENTER OPTION: ")

            if option == "1":
                self.view_all_shows()
            elif option == "2":
                show_id = input("ENTER SHOW_ID: ")
                self.view_available_seats(show_id, 1)  # Assuming hall 1 for now
            elif option == "3":
                show_id = input("ENTER SHOW_ID: ")
                num_tickets = int(input("ENTER NUMBER OF TICKETS: "))
                seats = []
                for _ in range(num_tickets):
                    row = int(input("ENTER SEAT ROW: "))
                    col = int(input("ENTER SEAT COLUMN: "))
                    seats.append((row, col))
                self.book_seats(show_id, 1, num_tickets, seats)  # Assuming hall 1 for now
            elif option == "4":
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")


# Example usage
star_cinema = Star_Cinema()
hall1 = Hall(10, 10, 1)
hall2 = Hall(15, 12, 2)

hall1.entry_show("show1", "Movie A", "7:00 PM")
hall2.entry_show("show2", "Movie B", "9:00 PM")

replica_system = ReplicaSystem(star_cinema)
replica_system.run()