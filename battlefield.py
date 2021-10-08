from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
from fleet import Fleet
from herd import Herd

#run game
class Battlefield:
    def __init__(self):
        self.rounds= 50

    #create dinos, teams, and weapons

    energy_sword = Weapon('sword',4)
    blaster = Weapon('blaster', 10)
    katar = Weapon('katar', 6)

    robot_one = Robot('rowdy',180,energy_sword)
    robot_two = Robot('dino smasher',75, blaster)
    robot_three = Robot('ninja',95, katar)


    dino_one = Dinosaur('rex',4,180)
    dino_two = Dinosaur('raptor',10,75)
    dino_three= Dinosaur('steg',6,95)


    fleet_one = Fleet()

    herd_one = Herd()

    fleet_one.add_robot('rowdy')
    fleet_one.add_robot('dino smasher')
    fleet_one.add_robot('ninja')

    herd_one.add_dinosaur('rex')
    herd_one.add_dinosaur('raptor')
    herd_one.add_dinosaur('steg')


#welcome player and ask for player name
    player= input('Welcom to robots vs dinosaurs! Please enter your name to begin playing')
    print(f'Welcome {player}')

#battlefield setup, weapon and team choices
    print('You will now be able to choose your team.')
    player_team = input('press 1 for robots and 2 for dinosaurs')
    if player_team == '1':
        player_team = fleet_one
        opposing_team = herd_one
        print(f'Your team is, {player_team.robot_fleet}, and the opposing team is {opposing_team.dino_herd}')
    if player_team == '2':
        player_team = herd_one
        opposing_team = fleet_one
        print(f'Your team is, {player_team.dino_herd}, and the opposing team is {opposing_team.robot_fleet}')
    
#take turns for battle with choices of attack
    print("welcome to the arena, the only way the contenders may leave is if their health reaches 0")
    round = 1
    while player_team == fleet_one:
        if player_team == fleet_one:
            print(opposing_team[0].health)
            if player_team.robot_fleet[0] == 'dead' and player_team.robot_fleet[1] == 'dead' and player_team.robot_fleet[2] == 'dead':
                print('The Dinos have won the game!')
                break
            if opposing_team.dino_herd[0] == 'dead' and opposing_team.dino_herd[1] == 'dead' and opposing_team.dino_herd[2] == 'dead':
                print('You have won the game!')
                break
            
            print('Welcome to the battlefield robot master!')
            print(f'We are now beginning round {round}')
            attacker= input('it is time to choose which robot you would like to fight first!'+'\n'+'press 1 for rowdy, press 2 for dino smasher and press 3 for ninja')

            #attacker 1
            if attacker == '1':
                if player_team.robot_fleet[0] == 'dead':
                    print(f'Im sorry but {robot_one.name} is no longer alive')
                    continue
                attacker = robot_one
                target = input(f'Who would you like {attacker.name} to attack?' + '\n' + 'Press 1 for Rex, 2 for Raptor, and 3 for Steg')
                if target == '1':
                    if opposing_team.dino_herd[0] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= dino_one
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_dino(target)
                                if target.health > 0:
                                    target.attack_robot(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.robot_fleet[0] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.dino_herd[0]= 'dead'
                            break
                                
                if target == '2':
                    if opposing_team.dino_herd[1] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= dino_two
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_dino(target)
                                if target.health > 0:
                                    target.attack_robot(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.robot_fleet[0] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.dino_herd[1]= 'dead'
                            break



                if target == '3':
                    if opposing_team.dino_herd[2] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= dino_three
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_dino(target)
                                if target.health > 0:
                                    target.attack_robot(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.robot_fleet[0] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.dino_herd[2]= 'dead'
                            break
             #
             # 
             # 
             # 
             #        
             #attacker 2
            if attacker== '2':
                if player_team.robot_fleet[1] == 'dead':
                    print(f'Im sorry but {robot_two.name} is no longer alive')
                    continue
                attacker = robot_two
                target = input(f'Who would you like {attacker.name} to attack?' + '\n' + 'Press 1 for Rex, 2 for Raptor, and 3 for Steg')

                if target == '1':
                    if opposing_team.dino_herd[0] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= dino_one
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_dino(target)
                                if target.health > 0:
                                    target.attack_robot(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.robot_fleet[1] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.dino_herd[0]= 'dead'
                            break
                                
                if target == '2':
                    if opposing_team.dino_herd[1] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= dino_two
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_dino(target)
                                if target.health > 0:
                                    target.attack_robot(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.robot_fleet[1] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.dino_herd[1]= 'dead'
                            break
                if target == '3':
                    if opposing_team.dino_herd[2] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= dino_three
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_dino(target)
                                if target.health > 0:
                                    target.attack_robot(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.robot_fleet[1] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.dino_herd[2]= 'dead'
                            break
            #
            ##
            #
            #
            #
            #attacker 3 
            if attacker== '3':
                if player_team.robot_fleet[2] == 'dead':
                    print(f'Im sorry but {robot_three.name} is no longer alive')
                    continue
                attacker = robot_three
                target = input(f'Who would you like {attacker.name} to attack?' + '\n' + 'Press 1 for Rex, 2 for Raptor, and 3 for Steg')
                if target == '1':
                    if opposing_team.dino_herd[0] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= dino_one
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_dino(target)
                                if target.health > 0:
                                    target.attack_robot(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.robot_fleet[2] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.dino_herd[0]= 'dead'
                            break
                                
                if target == '2':
                    if opposing_team.dino_herd[1] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= dino_two
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_dino(target)
                                if target.health > 0:
                                    target.attack_robot(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.robot_fleet[2] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.dino_herd[1]= 'dead'
                            break
                if target == '3':
                    if opposing_team.dino_herd[2] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= dino_three
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_dino(target)
                                if target.health > 0:
                                    target.attack_robot(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.robot_fleet[2] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.dino_herd[2]= 'dead'
                            break




         #
         # #
         # 
         # 
         # Team Change               
                
    while player_team == herd_one:

        if player_team == herd_one:
            if player_team.dino_herd[0] == 'dead' and player_team.dino_herd[1] == 'dead' and player_team.dino_herd[2] == 'dead':
                print('The Dinos have won the game!')
                break
            if opposing_team.robot_fleet[0] == 'dead' and opposing_team.robot_fleet[1] == 'dead' and opposing_team.robot_fleet[2] == 'dead':
                print('You have won the game!')
                break


            print('Welcome to the battlefield Dino master!')
            print(f'We are now beginning round {round}')
            attacker= input('it is time to choose which dinosaur you would like to fight first!'+'\n'+'press 1 for rex, press 2 for raptor and press 3 for steg')


             #attacker 1
            if attacker == '1':
                if player_team.dino_herd[0] == 'dead':
                    print(f'Im sorry but {dino_one.name} is no longer alive')
                    continue
                attacker = dino_one
                target = input(f'Who would you like {attacker.name} to attack?' + '\n' + 'Press 1 for Rowdy, 2 for dino smasher, and 3 for ninja')
                if target == '1':
                    if opposing_team.robot_fleet[0] == 'dead':
                        print('that Robot has already been destroyed.')
                        continue
                    target= robot_one
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_robot(target)
                                if target.health > 0:
                                    target.attack_dino(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.dino_herd[0] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.robot_fleet[0]= 'dead'
                            break
                                
                if target == '2':
                    if opposing_team.robot_fleet[1] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= robot_two
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_robot(target)
                                if target.health > 0:
                                    target.attack_dino(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.dino_herd[0] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.robot_fleet[1]= 'dead'
                            break



                if target == '3':
                    if opposing_team.robot_fleet[2] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= robot_three
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_robot(target)
                                if target.health > 0:
                                    target.attack_dino(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.dino_herd[0] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.robot_fleet[2]= 'dead'
                            break
             #
             # 
             # 
             # 
             #
             #attacker 2

            if attacker== '2':
                if player_team.dino_herd[1] == 'dead':
                    print(f'Im sorry but {dino_two.name} is no longer alive')
                    continue
                attacker = dino_two
                target = input(f'Who would you like {attacker.name} to attack?' + '\n' + 'Press 1 for rowdy, 2 for dino smasher, and 3 for ninja')

                if target == '1':
                    if opposing_team.robot_fleet[0] == 'dead':
                        print('that robot has already been destroyed.')
                        continue
                    target= robot_one
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_robot(target)
                                if target.health > 0:
                                    target.attack_dino(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.dino_herd[1] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.robot_fleet[0]= 'dead'
                            break
                                
                if target == '2':
                    if opposing_team.robot_fleet[1] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= robot_two
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_robot(target)
                                if target.health > 0:
                                    target.attack_dino(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.dino_herd[1] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.robot_fleet[1]= 'dead'
                            break
                if target == '3':
                    if opposing_team.robot_fleet[2] == 'dead':
                        print('that Dino has already been destroyed.')
                        continue
                    target= robot_three
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_robot(target)
                                if target.health > 0:
                                    target.attack_dino(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.dino_herd[1] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.robot_fleet[2]= 'dead'
                            break




            #
            ##
            #
            #
            #
            #attacker 3 
            if attacker== '3':
                if player_team.dino_herd[2] == 'dead':
                    print(f'Im sorry but {dino_three.name} is no longer alive')
                    continue
                attacker = dino_three
                target = input(f'Who would you like {attacker.name} to attack?' + '\n' + 'Press 1 for rowdy, 2 for dino smasher, and 3 for ninja')
                if target == '1':
                    if opposing_team.robot_fleet[0] == 'dead':
                        print('that robot has already been destroyed.')
                        continue
                    target= robot_one
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_robot(target)
                                if target.health > 0:
                                    target.attack_dino(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.dino_herd[2] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.robot_fleet[0]= 'dead'
                            break
                                
                if target == '2':
                    if opposing_team.robot_fleet[1] == 'dead':
                        print('that robot has already been destroyed.')
                        continue
                    target= robot_two
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_robot(target)
                                if target.health > 0:
                                    target.attack_dino(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.dino_herd[2] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.robot_fleet[1]= 'dead'
                            break
                if target == '3':
                    if opposing_team.robot_fleet[2] == 'dead':
                        print('that robot has already been destroyed.')
                        continue
                    target= robot_three
                    print(f'Prepare for {attacker.name} and {target.name} to go to battle!')
                    print(f'{attacker.name} and {target.name} will fight in the battlefield arena until one of them falls!')
                    while attacker:
                        if attacker.health >0:
                            if target.health >0:
                                attacker.attack_robot(target)
                                if target.health > 0:
                                    target.attack_dino(attacker)
                        if attacker.health ==0 or attacker.health < 0:
                            round += 1
                            print(f'{attacker.name} has lost the battle!')
                            input()
                            player_team.dino_herd[2] = 'dead'
                            break
                        if target.health == 0 or target.health < 0:
                            round += 1
                            print(f'{target.name} has lost the battle!')
                            input()
                            opposing_team.robot_fleet[2]= 'dead'
                            break

#display health pools for dinos and robots displayed

#death checks & team checks

#loop above until death, if death of opponent remove apponent from battle field

#display winner and prompt for play again