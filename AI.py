import main
import neat
import numpy
import pygame
import os
import pickle

def test_ai(net):
    main.main(net)

        


def train_ai(genome1, genome2, genome3, genome4, genome5, config):
    run = True


    net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
    net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
    net3 = neat.nn.FeedForwardNetwork.create(genome3, config)
    net4 = neat.nn.FeedForwardNetwork.create(genome4, config)
    net5 = neat.nn.FeedForwardNetwork.create(genome5, config)
    

    negative = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        main.Play_train()
        plyr =main.player
        if plyr == 0:
            bot_move(genome1, net1, plyr)
        elif plyr ==1:
            bot_move(genome2, net2, plyr)
        elif plyr ==2:
            bot_move(genome3, net3, plyr)
        elif plyr ==3:
            bot_move(genome4, net4, plyr)
        elif plyr ==4:
            bot_move(genome5, net5, plyr)

        

        pygame.display.update()
        if main.check_win()!=-1 or main.PLAYERS[0].money<700:
            calculate_fitness([genome1, genome2, genome3, genome4, genome5], main.PLAYERS)
            main.reset_all()
            break
        

        
        

    return False


def bot_move(genome, net, player):
    bot = main.PLAYERS[player]
    river_input = []
    for card in main.RIVER:
        river_input.append(card.value)
        river_input.append(card.suite_val)
    while len(river_input)<10:
        river_input.append(0)
    output = net.activate((main.check_hand(main.RIVER, bot.card1, bot.card2), bot.call, main.RIVER_CARD_COUNT, main.POT_AMT))  
    decision = output.index(max(output[:-1]))
    if decision ==0 and main.check_hand(main.RIVER, bot.card1, bot.card2)<46 and bot.call!=0:
        genome.fitness+=10
    elif decision == 2 and output[3]<6:
        genome.fitness-=1

    if decision < 2:
        main.handle_bot_train_move(decision, 0)
    else:
        if bot.money-output[3]<0:
            genome.fitness-=100000
        main.handle_bot_train_move(2, output[3])

def calculate_fitness(genomes, players):
    
    for i in range(len(genomes)):
        genomes[i].fitness+=main.PLAYERS[i].money-1000
        
    

        
def find_combos(lst, n):
    if n == 0:
        return[[]]
    l = []
    for i in range(0, len(lst)):
        m = lst[i]
        remLst=lst[i+1:]
        for p in find_combos(remLst, n-1):
            l.append([m]+p)
    return l



def eval_genomes(genomes, config):
    sum = 0
    
    
    genomes = [i for j, i in genomes]
    for thing in genomes:
        thing.fitness = 0
    
    combos = find_combos(genomes, 5)
    print(str(len(combos)))
    for combo in combos:
        
        genome1 = combo[0]
        genome2 = combo[1]
        genome3 = combo[2]
        genome4 = combo[3]
        genome5 = combo[4]
        genome1.fitness = 0 if genome1.fitness == None else genome1.fitness
        genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
        genome3.fitness = 0 if genome3.fitness == None else genome3.fitness
        genome4.fitness = 0 if genome4.fitness == None else genome4.fitness
        genome5.fitness = 0 if genome5.fitness == None else genome5.fitness
        if sum%1000==0:
            print(str(sum))
        sum+=1

        force_quit =train_ai(genome1, genome2, genome3, genome4, genome5, config)
        if force_quit:
            quit()

                        

def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-30')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats) 
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)
    with open("secondBest.pickle", "wb") as f:
        pickle.dump(winner, f)


def test_best_network(config):
    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    
    test_ai(winner_net)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    run_neat(config)
    test_best_network(config)