import random
from simulation_progress import progress
import time, sys
#from simulation_progress import simulation_progress
class rps(object):
    def __init__(self, rounds=100):
        self.rounds = rounds
        self.score_1 = 0
        self.score_2 = 0
        self.percentage = [0,1,0,2,0,3]
        self.data= [[1,3],[2,1],[3,2]]
        self.progress = progress('-', repeat=True, repeat_frequency=100000)
        self.games_played = 0
    def rps_generate(self):
        return(random.randint(1,3))
    def detect_win(self, rps_1, rps_2):
        #1 = r 2 = p 3 = s
        #print(rps_1, rps_2)
        if rps_1 == rps_2:
            for x in range(1, len(self.percentage), 2):
                if rps_1 == self.percentage[x]:
                    self.percentage[x-1] += 2
        elif list((rps_1, rps_2)) in self.data:
            self.score_1 += 1
        else:
            self.score_2 += 1
        if rps_1 != rps_2:
            for x in range(1, len(self.percentage), 2):
                if rps_1 == self.percentage[x]:
                    self.percentage[x-1] += 1
                if rps_2 == self.percentage[x]:
                    self.percentage[x-1] += 1
    def calculation(self):
        print('Statistics:')
        print(f'Player 1 Won: {self.score_1} and Player 2 Won: {self.score_2} Draws: {self.games_played-(self.score_1+self.score_2)} Games Played: {self.games_played}')
        print(f'Rock was Played {self.percentage[0]} Times, Paper was Played {self.percentage[2]} Times, and Scissors was Played {self.percentage[4]} Times')
    def main(self):
        for x in range(self.rounds):
            try:
                self.detect_win(self.rps_generate(), self.rps_generate())
                self.games_played += 1
                self.progress.add_progress()
            except KeyboardInterrupt:
                self.progress.finnish_progress('Incomplete', time.perf_counter())
                self.calculation()
                sys.exit()
        self.calculation()
        self.progress.finnish_progress('Completed', time.perf_counter())
rock_paper_scissors = rps(rounds=10000000)
rock_paper_scissors.main()