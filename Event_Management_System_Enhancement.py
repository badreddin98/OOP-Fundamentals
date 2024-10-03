class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participant_count = 0
            
        def add_participant(self):
            self.participant_count += 1
            print(f"One participant added to {self.name}. Total participants: {self.participant_count}")
            
        def get_participant_count(self):
            return self.participant_count
        
concert = Event("Music Concert", "2024-10-02")

print(f"Initial participant count for {concert.name}: {concert.get_participant_count()}")

concert.add_participant()
concert.add_participant()
concert.add_participant()

print(f"Final participant count for {concert.name}: {concert.get_participant_count()}")
