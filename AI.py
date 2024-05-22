import main
import neat
import numpy
import pygame
import os
import pickle


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.event.clear()
            run = False
            
    main.Play_Easy()
    if main.check_win()!=-1:
        main.reset_game()
        main.reset_all()
        break
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    main.Play_Easy()
    if main.check_win()!=-1:
        main.reset_game()
        break
pygame.quit()

def train_ai(self, genome1, genome2, genome3, genome4, genome5, config, draw=False):
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

        main.Play_Easy()

        bot_move()

        if draw:
            self.game.draw(draw_score=False, draw_hits=True)

        pygame.display.update()

        
        if game_info.left_score == 1 or game_info.right_score == 1 or game_info.left_hits >= max_hits:
            self.calculate_fitness(game_info, duration)
            break

    return False


def bot_move(genome, net, player):
    bot = main.PLAYERS[player]
    river = main.River
    output = net.activate(bot.card1.value, bot.card1.suite_val, bot.card1.value, bot.card2.suite_val, river[0].value, river[0].suite_val, river[1].value, river[1].suite_val, river[2].value, river[2].suite_val, river[3].value, river[3].suite_val, river[4].value, river[4].suite_val)  
    decision = output.index(max(output[:-1]))
    if decision < 2:
        main.handle_bot_ai_move(decision, 0)
    else:
        main.handle_bot_ai_move(2, output[3])

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
            game = main.Play_Easy()

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
    pong = main.Play_Easy()
    pong.test_ai(winner_net)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    run_neat(config)
    test_best_network(config)