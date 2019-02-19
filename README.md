# Bazaar

Future:

- [ ] Make agent independent of Sprite class
- [ ] Add "debug view" option, for quickly setting up on Macbook v. 3 Monitor layout.
- [ ] Get agents as shapes (for now)
- [ ] Abstract Stele
  - [ ] Experiment with the rectangle/pyramid layout! (Complete with dynamic tags).

v19:

- [x] Resolve latency of Stele
- [x] Get Stele to blink on contact
- [ ] Get graph to work properly (Start random and add in known value.)

v18:

- [x] Get everything running in a single file (other than utils/resources/vector2)
- [x] Restructure according to "vertex_buffer_1" reference code

----

## 19

So far, a lot of improvements made. I'm mostly just excited to have it running relatively quickly. I'd like to find a way to get the graph to work before moving on to 20.

It's being really fussy. Right now I'm trying to get it to initialize with some random points, and then slowly start adding a set value, just to make sure the "update" method works right when pushing one value to the next "lower" index.

## 18

Going to experiment with having everything in one file, other than vector2 and utilities.

Removed the name module and graph test.

## 17

Likely the final I'll be showing for thesis final for fall. I'm about to restructure everything.


## 16

Starting with deleting the name module for now. Commenting, rather. Need to slow down the graph also.


## 15

Going to formalize the Graph class, clean it up a bit, and start really laying out what each window will do. Also, going to fold data and common into one another because I'm not certain I really get why they're different.

Huge problem...lol...for some reason the names all become the same after long enough? Name swap module should be changed. But also, should probably not exist in its current state anyway.

## 14

Added a graph test, just made a little class that you then update. We'll see how this works out. I'm going to turn it into a module and turn the "data window" into the stock chart for v15.

## 13

Ok I think I'm going to start defining an agent's "confidence" in its strategy by connecting it to how much money it has made. The more money it's made (regardless of whether or not it was actually based on the agents behavior), the more confident it will be in its strategy. If its profits plummet, its more likely to experiment. How should this be written?

To start experimenting with this, I'll give them a basic choice when faced with a changing gaussian curve. They can bet "Higher" or "Lower", meaning that its value every, lets say, 5 seconds, is higher or lower than it was 5 seconds ago. If its correct, it is weighted towards its previous choice.

I actually ended up doing something different. I just have it choose -1 or 1 and modify the agent's bias based on an initial guess. It's a random sequence that it tries to interpret as meaningful. I also have them influence nearby agents biases if they posess a stronger bias. Next I need the sequence to start resembling stock information, and to have it be affected by the biases themselves. How do?????

Also going to start breaking features up into little testing modules, such as for no. 13 I made a data test module that just tests the new trading features.

## 12

Got the mesh-web network to finally work. Not sure, however, that I like it. It doesn't really tie into what I'm thinking of just yet, however, the idea of the relations being depicted rather than the objects is kind of compelling. That which does not relate to anything else may as well not exist (of course, everything that exists (I think) relates to _something_, so this isn't much of a statement)!

Next I think I really need to start defining their behavior, so that I actually have something to depict.
