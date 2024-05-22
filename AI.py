import main
import neat
import numpy
import pygame
import os
import pickle




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
    river = main.River
    output = net.activate(bot.card1.value, bot.card1.suite_val, bot.card1.value, bot.card2.suite_val, river[0].value, river[0].suite_val, river[1].value, river[1].suite_val, river[2].value, river[2].suite_val, river[3].value, river[3].suite_val, river[4].value, river[4].suite_val)  
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
        for genome_id2, genome2 in genomes[i+1:-4]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = main.Play_train()

            force_quit = game.train_ai(genome1, genome2, config, draw=True)
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