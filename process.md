# Iterations

## 12

Got the mesh-web network to finally work. Not sure, however, that I like it. It doesn't really tie into what I'm thinking of just yet, however, the idea of the relations being depicted rather than the objects is kind of compelling. That which does not relate to anything else may as well not exist (of course, everything that exists (I think) relates to _something_, so this isn't much of a statement)!

Next I think I really need to start defining their behavior, so that I actually have something to depict.

## 13

Ok I think I'm going to start defining an agent's "confidence" in its strategy by connecting it to how much money it has made. The more money it's made (regardless of whether or not it was actually based on the agents behavior), the more confident it will be in its strategy. If its profits plummet, its more likely to experiment. How should this be written?

To start experimenting with this, I'll give them a basic choice when faced with a changing gaussian curve. They can bet "Higher" or "Lower", meaning that its value every, lets say, 5 seconds, is higher or lower than it was 5 seconds ago. If its correct, it is weighted towards its previous choice.