Visualizing the extended network of some ["sensemaking" podcasts](https://www.listennotes.com/listen/sensemaking-extended-lOr1NJsGawm/?display=podcast)

## How to use

To explore this data yourself, you can download the `podcast.gephi` file and open it with the free cross-platform program [Gephi](https://gephi.org/)

If you want to look at the raw data, see `raw.txt`.

## How it was made

Because of inconsistences in how podcasts indicate their guests, this process can't be fully automated. I did this semiautomatically. If a podcast had only a few episodes I just typed them out. If a podcast had one or two conventions for putting their guests in titles I just copied the markup and handled it adhoc with a bit of BeautifulSoup and regex (see the messy regex.py). 

If a podcast had too many episodes and no consistency in indicating guests I just excluded it (for now): Psychedelic Salon, Buddhist Geeks, Skeptiko, Future Primitive, Duncan Trussell Family Hour, The Sheldrake Vernon Dialogues, Expanding Mind. If someone wants to volunteer to do those painstakingly I would appreciate it.

If a podcast has no guests I excluded it: The Symbolic World, Awakening from the Meaning Crisis.

The raw data is simply formatted like so:

```
Circling Wizardry Podcast;Josh Levin, Jordan Allen, Jack Hart, Sara Ness, Guy Sengstock
Infinite Conversations;Marco V Morelli, Douglas Prater, Greg Thomas, Caroline Savery, John Davis, Jenn Zahrt, J. F. Martel, Bonnitta Roy, Trevor Malkinson, Jeremy D. Johnson, Mark Binet
```

Each line is a podcast. The podcast name goes first followed by a semicolon and a list of guests in roughly date-published order, with the hosts prepended. It doesn't matter if there are duplicates.

There are obvious problems here with nicknames, titles, typos, etc. I use a fuzzy matcher to try to get around that, but I may have made some mistakes. If you spot some let me know.

Once this raw data was ready, I just made two CSVs files ready to import to Gephi. One has podcasts as nodes and edges represent shared guests. Another has people as nodes and edges represent having been on the same podcast.