import main
import neat
import numpy
import pygame
import os
import pickle

def test_ai(net):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        


def train_ai(genome1, genome2, genome3, genome4, genome5, config):
    run = True


    net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
    net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
    net3 = neat.nn.FeedForwardNetwork.create(genome3, config)
    net4 = neat.nn.FeedForwardNetwork.create(genome4, config)
    net5 = neat.nn.FeedForwardNetwork.create(genome5, config)
    



    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        main.Play_train
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

        
        

    return False


def bot_move(genome, net, player):
    bot = main.PLAYERS[player]
    river = main.RIVER
    river_input = []
    for card in river:
        river_input.append(card.value)
        river_input.append(card.suite_val)
    while len(river)<5:
        river.append(0)
    output = net.activate(bot.card1.value, bot.card1.suite_val, bot.card1.value, bot.card2.suite_val, river[0], river[1], river[2], river[3], river[4], river[5], river[6], river[7], river[8], river[9], river[10], )  
    decision = output.index(max(output[:-1]))
    if decision < 2:
        main.handle_bot_train_move(decision, 0)
    else:
        main.handle_bot_train_move(2, output[3])

def calculate_fitness(genomes, players):
    for genome, player in genomes, players:
        genome.fitness+=player.money
    

        




def eval_genomes(genomes, config):
    """
    Run each genome against eachother one time to determine the fitness.
    """

    for i, (genome_id1, genome1) in enumerate(genomes):
        
        genome1.fitness = 0
        for genome_id2, genome2 in (genomes[i+1:]):
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            for genome_id3, genome3 in genomes[i+2:]:
                genome3.fitness = 0 if genome3.fitness == None else genome3.fitness
                for genome_id4, genome4 in (genomes[i+3:]):
                    genome4.fitness = 0 if genome4.fitness == None else genome4.fitness
                    for genome_id5, genome5 in (genomes[i+4:]):
                        genome5.fitness = 0 if genome5.fitness == None else genome5.fitness
            

                        force_quit =train_ai(genome1, genome2, genome3, genome4, genome5, config)
                        if force_quit:
                            quit()


def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-85')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)


def test_best_network(config):
    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    width, height = 700, 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")
    pong = main.Play_train()
    pong.test_ai(winner_net)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    run_neat(config)
    test_best_network(config)