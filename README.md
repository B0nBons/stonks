# Stonks?
Yes, really. Stonks. We've all heard of stocks. Alas, as a broke kid, I was never able to partake in the purchasing of stocks. Which is precisely why I made STONKS!!!! 
My logic with this game was simple -- if I can't experience the joy of getting a windfall in real life, at least I can pretend to get one in a game!!!

## Uh, Why?
You, an average office worker, find yourself in crippling debt. Looking for a way out, you trust a fairly kind pink pig. The pig gives you a new purpose in life; buy stocks.
Yet, the day you finally have enough to live comfortably, the pig comes back. Not as your friend. As the Pig of Small Alleyway. You are offered a deal. Pay the pig back, or face the punishment. Eager to not be defeated by an angry pink blob, you agree to pay the pig back. ![Your creditor...](/assets/sprites/happy.png)

In order to pay the pig back, you must use the only money you have -- the 1,000 dollars that you originally borrowed from the pig -- to earn more money, to eventually (impossibly) pay off the ever-increasing debt that the pig has placed upon you. How will you multiply your money? Simple! Invest in the primary stocks, and once you have enough money... Well, have some fun, and let loose at the local RNG-Probability-Based Mysterious Area™ [Casino]. You'll *probably* earn your money back. Or at least *some* of it? 

## Tech Stack
- Time! It was mainly going to be used for animating the horse races, however it ended up being used to make the game feel less robotic and instant (if you get what I mean?)
- Random!!! Random is one of the (if not the most) import libraries, as almost everything relies upon it. It was used to vary stocks, and make the RNG games have, well, RNG
- Pygame... Pygame was honestly the one library I did NOT want to use, but had to be used in order to implement fun background music. That's it. We HATE pygame here.
- Python!!!!! Because I like Python more than C


## How to Play
Download the RELEASE for your system. As of now, only Linux can be implemented (sorry Windows). Once you have your release downloaded, follow the next steps.
First, check that python3 is installed. To do that, press `ctrl + alt + t` to open the terminal, and paste in the following command:
`python3 --version`
If it is NOT installed, use your systems package manager (for example, apt for ubuntu, dnf for fedora), and install it. I've included the UBUNTU example here:
`sudo apt update && sudo apt install python3`
(You may or may not need sudo permission, depending on how your computer is setup. If you are unable to install, try talking with your system administrator. Or google. That's also a choice.)
At any rate, once Python is installed, navigate to the FOLDER that has the RELEASE downloaded. For simplicity, we will be calling the release **"main"**. Usually, it will be in your downloads folder. If your terminal is not already in downloads (you can check by typing `pwd` which will show what folder you are in), navigate there. You can do this by typing `ls` (essentially, list all files in this folder), and then typing `cd Downloads` **NOTE THAT MOST LINUX DISTROS ARE CASE SENSITIVE!!!**
Once you're in the correct folder as the downloads, all you need to do, is run the following!
`chmod +x main`
And then,
`./main`
Have fun playing! It resets when you close it! See if you can pay off your debt to the pig. If not... You might be pork. ["He will VERY be mad"](/assets/sprites/ANGER.png)