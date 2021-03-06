import random
import game as gamemod
import numpy as np


OFF = gamemod.OFF
ON = gamemod.ON

class Player:
    def __init__(self,color,num):
        self.color = color
        self.num = num
    
    def take_turn(self,moves,game=None):
        raise NotImplementedError("Override me")

class RandomPlayer(Player):
    def take_turn(self,moves,game=None):
        if moves:
            return random.choice(list(moves))
        return None

class HumanPlayer(Player):

    def take_turn(self,moves,game=None):
        while True:
            if not moves:
                raw_input("No moves for you...(hit enter)")
                break
            while True:
                mv1 = raw_input("Please enter a move <location start,location end> ('%s' for off the board): "%OFF)
                mv1 = self.get_formatted_move(mv1)
                if not mv1:
                    print 'Bad format enter e.g. "3,4"'
                else:
                    break

            while True:
                mv2 = raw_input("Please enter a seond move (enter to skip): ")
                if mv2 == '':
                    mv2 = None
                    break
                mv2 = self.get_formatted_move(mv2)
                if not mv2:
                    print 'Bad format enter e.g. "3,4"'
                else:
                    break

            if mv2:
                move = (mv1,mv2)
            else:
                move = (mv1,)

            if move in moves:
                break
            elif move[::-1] in moves:
                move = move[::-1]
                break
            else:
                print "You can't play that move"

        return move

    def get_formatted_move(self,move):
        try:
            start,end = move.split(",")
            if start==ON:
                return (start,int(end))
            start = int(start)
            if end == OFF:
                return (start,end)
            end = int(end)
            return (start,end)
        except:
            return False
