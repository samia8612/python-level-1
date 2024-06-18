import hashlib

def display_menu():
    print("Welcome to the Voting System!")
    print("Please choose an option:")
    print("1. Vote for a candidate")
    print("2. View voting results")
    print("3. Quit")
    choice = input("Enter your choice: ")
    return choice

def display_candidates():
    print("Available candidates:")
    print("1. Alice")
    print("2. Bob")
    print("3. Charlie")
    
    
def vote_process():
    name = input("Enter your name: ")
    candidate_id = input("Enter the candidate ID you wish to vote for: ")
    return name, candidate_id

def hash_candidate_id(candidate_id):
    # Create a SHA-256 hash of the candidate ID
    return hashlib.sha256(candidate_id.encode()).hexdigest()

def display_results(votes):
    print("Voting Results:")
    for candidate, vote_count in votes.items():
        print(f"{candidate}: {vote_count} votes")

def main():
    votes = {"Alice": 0, "Bob": 0, "Charlie": 0}
    voters = set()

    while True:
        choice = display_menu()

        if choice == '1':
            display_candidates()
            name, candidate_id = vote_process()
            #print(vote_process)

            if name in voters:
                print("Thank you for your voting.")
            else:
                hashed_candidate_id = hash_candidate_id(candidate_id)
                if candidate_id == '1':
                    votes["Alice"] += 1
                elif candidate_id == '2':
                    votes["Bob"] += 1
                elif candidate_id == '3':
                    votes["Charlie"] += 1
                else:
                    print("Invalid candidate ID.")
                    continue
                voters.add(name)
               # print(f"#{hashed_candidate_id}. Thank you for voting!\n")

        elif choice == '2':
            display_results(votes)

        elif choice == '3':
            print("Thank you for using the Voting System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()