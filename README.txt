Generate random map
===================

Simple code for genrating random "cave like" enviroments in python.

Project inspired by http://roguebasin.roguelikedevelopment.org/index.php/Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels thx! 

Example with density 45 % and height 20 and width 90.
(Check this out in "raw" format, the new github rendering makes it ugly). 

=====================================================
First iteration
 # #   ## #   ###  #### # ## #   ##  # #        #   ##  #  # # # ### #   ######## # #  #  
   #  #    ## #   ##  # # #      # ##  ##  ##   #  #    ##   #      # #### ##        #### 
 ## ##   ## #   #  #  #  ### #####  # ####    # ##  ## #         ###       #   # ### #    
  # ### #   ## #  # #   #### # ### ###  ####  #### ## # #   ######## ##  #  ##   ### #  ##
 #   ### #    #    #   ### # #     #   #         ##   #  # # # ## # #  #    # #### # # ## 
#  ## # #    ##    #  # # #  #   ### #  ## ##    # ##  ##    ##   # #  # #   # ###   # # #
### # #    ##   # #  ### #  ##     ## #  #    # ## # ### # #    ## #      #  ## #     # ##
 ###  # ##  #    # ## ##  # # #  ## # # ###  ### #  ##          ## ### #### ### ##  # ## #
#      #  # #  ## #    ####   ##        ## ### #####    #  #### #     ###  #####  #   ##  
 #  ##    # # #### # ##   ### #  ####    #  ####   ####  ###   # ####     ##  ## ####   ##
# #  # # #     ####  ### ### ##  # #### #   # ##   # ###### # # ###  # # # #       #    ##
      #  ###     #    # #   ## ##      ##  # ##  #  ## #   #  #  #    ##  #   ##   #####  
  ## #   # ##       ########   # ##   ##     ####    # ##   ##     #### # #  #     #   ## 
 # ##    ## ### ####     #  #  # ## ##   #    ### ####  # ##       ##### # ### #### # #  #
## ##   # #  # #  # ##    #  ##  ## ####        ## ### # ####     ### # #     # # # ###   
##   ### # #   # #  ##  # #   # ##  #  # #  ###          #    ##      ### #  #    #  ## # 
  ##      # #     #    # ## ### # #     #     #### # ##          ### #  # ##     ### # # #
   #  ###  #  ## #    #  ## #    # ## #### #### # ### ###  ## # ##       ### # #  ##  # ##
#   #    #   # # # # #  # ####  ### #  #   # # #     # # ### ##  #      #    ##  ## # # ##
## #  #  #  ###   #   ##  ##     ## #   # # #     ##  ### ###   # #### # ### ###    # ####

Smoothing the map
# ### #######################   #########  ##  ### ### #### ### ################## #######
# #        #   #   ### # ###    ###   ###           #             ##      ###         #   
   ###     ###     #     ###  ######## ####    ###  #            ###        #     # # #  #
#   ###                 ##### ###   #  ###     ####  #        ######            #####    #
#   ####     ##        #### #     ###   ###     ####   #    ########         ###### # # ##
##   ###              ####  #     ###            ##   ###        # #         #####    ####
#### # #             ###     #    ####  ###     # # ###          ####   ##   #####    ####
###        #     #    ####   #          ###  ###### #           ##     ### #####      ####
#          #   ####   ## ### #    ##    ### ##### ####          #####  #############   ###
#              ####   ###### ##   ###       ##### ############ ####       ### #   ##    ##
#         #    ####  ###  #####   ###       ####    ########    ###       #       ###   ##
          #          ######## # #     ##     ###    #####    #       ###            #  ###
         ####          ###      ##           ####   ###             ####      #    ##### #
# ###    #####     ###   ##     #### ##       #### #### #####      #####         # # #   #
### #    ##   # #####           #######        #   ##    ###       ######        # # ##  #
###                      #   ### #             ##   #             ##   # #       ######  #
#     ##                 ### #   #     ##   ####                         ###      ##  ####
                         #####   ###   ##   #####   ####         ##      ##      ###   ###
#            ##          ####    ###   ##  ###     #  ########   #       ## ###    # # ###
######  ### ##################  ###### ########   ########################################

#############################  ########### ##  ###########################################
#  ##     #####   ##### ####   ###########      #   #            ####     ####       ### #
#   ##                  ####   #####  ####      ##               ###               #     #
#   ###                 ####   ######  ####    ####           ######            #### #   #
#   ####               #####       ##   ##      ###           ######          ######   ###
##  ####              ####        ###    #       ###  ##        ####         #####    ####
###   #               ###          ##    #      #### #           ##     #   #####     ####
###                   ###          #    ###  #########          ####   ###########    ####
##              ###   ##### #      #     #  ##########          ###     ########  #    ###
#              ####   #########   ###       #####  #########    ####     #####   ###    ##
#               ##   ##########    #        ####   ##########   ##                 #    ##
          ##          ########               ###    #####            ##            ### ###
         ####         #####     ##           ####   ####            ####            ### ##
## #     ####      ##           ######        ###  ###   ###       #####          # ###  #
####      #        ##           ######         ##  ###   ###       ######         #####  #
##                              ###           ##                        #         ########
#                        ######   #          ####                        ##      #### ####
#                        ####    ##    ##   ####      ##                 ###      ##  ####
#            ##         ######   ####  ### ####    ###########  ###     #######  #### ####
######  ######################  ###############   ########################################

#############################  ########### ##  ###########################################
#  ##     #####   ##### ####   ###########      #   #            ####     ####       ### #
#   ##                  ####   #####  ####      ##               ###               #     #
#   ###                 ####   ######  ####    ####           ######            #### #   #
#   ####               #####       ##   ##      ###           ######          ######   ###
##  ####              ####        ###    #       ###  ##        ####         #####    ####
###   #               ###          ##    #      #### #           ##     #   #####     ####
###                   ###          #    ###  #########          ####   ###########    ####
##              ###   ##### #      #     #  ##########          ###     ########  #    ###
#              ####   #########   ###       #####  #########    ####     #####   ###    ##
#               ##   ##########    #        ####   ##########   ##                 #    ##
          ##          ########               ###    #####            ##            ### ###
         ####         #####     ##           ####   ####            ####            ### ##
## #     ####      ##           ######        ###  ###   ###       #####          # ###  #
####      #        ##           ######         ##  ###   ###       ######         #####  #
##                              ###           ##                        #         ########
#                        ######   #          ####                        ##      #### ####
#                        ####    ##    ##   ####      ##                 ###      ##  ####
#            ##         ######   ####  ### ####    ###########  ###     #######  #### ####
######  ######################  ###############   ########################################
