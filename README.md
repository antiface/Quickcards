quickcards ![] (https://zenodo.org/badge/doi/10.5281/zenodo.9872.png)
==========

What is this quickcards repository you wonder? Why did I call it quickcards, and why did I choose to create a repository that seemingly has no code?

The term quickcards actually comes from an old piece of software called [Zoomracks] (http://en.wikipedia.org/wiki/Zoomracks). Zoomracks was a database management system for the Atari ST and IBM PC that represented data in a form that was visually represented by a filing card, known as "QUICKCARD"s.

Basically, what I want to do is write software that is as minimalistic as possible. I don't just want to go for elegance and readability: I want to go for code that is the absolute minimum it needs to be to "get stuff done".

Firstly, I want to look at a few things: I want to rewrite a kind of [Hypercard] (http://en.wikipedia.org/wiki/Hypercard) system in Python; I want it to be loosely based on the simplest [flat file database] (http://en.wikipedia.org/wiki/Flat_file_database) possible, loosely based also on the simplest blog platform possible, + loosely based on the simplest wiki implementation possible. All in Python. (Possible inspiration: [Smallest Federated Wiki] (https://github.com/WardCunningham/Smallest-Federated-Wiki), [Cardbox] (http://www.cardbox.com/)).

The paradigm is inspired largely by the work of [Paul Otlet] (http://en.wikipedia.org/wiki/Paul_Otlet), with his Mundaneum + Universal Decimal Classification + Traité de Documentation, etc., as well as the work of [Herman Hollerith] (http://en.wikipedia.org/wiki/Herman_Hollerith) (i.e. the Art of Compiling Statistics, he developed a mechanical tabulator based on punched cards to rapidly tabulate statistics from millions of pieces of data, circa 1880s). Also a huge inspiration is the work of [Gina Trapani] (https://github.com/ginatrapani) (i.e. inventor of the [todo.txt 2.0 paradigm] (http://todotxt.com/) and other [Lifehacks](http://en.wikipedia.org/wiki/Lifehack)).

Basically, I want to write the simplest Python program possible to deal with .txt files at first, until I write the functions to store the contents of the "Cards" in lists and hash tables. I am using the metaphor of the Index Card. Basically, a Card is composed of a given number of lines of text. The lines of text are about entities, objects, and are references to other entities, objects. The Cards are hyperlinked and form a network-of-cards. That's how I am seeing it for now. More to come. Still in conceptual modeling phase.

The design philosophy is simple. Software is Text. There is little difference between a Python program written in the 21st century and a clay tablet made 5000 years ago. Both are Texts. In one case, one uses a stylus to make marks on the clay tablet. In the other, one uses a keyboard or touchscreen to input text into a text editor, displayed on a monitor, etc. The point is that both use character sets to make lines of text. One could imagine someone using clay tablets to write software; one would just need to scan the clay tablet and use Optical Character Recognition to make the content machine-readable. So basically I am reinventing the library card catalog, version 3.0, inspired by Herman Hollerich, Paul Otlet and Gina Trapani.

One implementation of the "quickcards" idea would be a simple [tumbleblog] (http://www.kottke.org/05/10/tumblelogs) platform that displays index cards in a [dynamic grid layout] (http://www.queness.com/post/11133/the-famous-pinterest-dynamic-grid-layout-and-design-inspirations) similar to how boards and pins are displayed on Pinterest. Index cards would be tagged and categorized and would be searchable using a simple faceted search interface. (Perhaps with advanced tag filtering à la [Filtrify] (http://luis-almeida.github.com/filtrify/) or dynamic html tree view controls à la [dynatree] (http://luis-almeida.github.com/filtrify/)).

In other words, it would be a simple card catalog. I'd like it to have something like the Redis Data Structure Store or just a simple key-value store. I will take a look at MongoDB and Hyperdex, as well as Tokyo Cabinet, Kyoto Cabinet, PostgreSQL, and SQLite to see what is best, but I'm very far away from such considerations at the moment. This is just a toy problem I want to play with, the idea of a cloud-based super-hypermedia card catalog. The vision is closer to the vision of Otlet's Mundaneum than the vision of the WWW. I want it to be a masterpiece of the Inter-Referential Database Arts.

I'm not even sure what I want to build yet. All I know is that I want it to be very fast. [Fetchnotes] (http://www.fetchnotes.com/) is a wonderful note-taking service. Possibly the thing I love the most about it though is how responsive and fast it is. I really don't know how they made it so fast. It is amazing.

Other services I've long had a fondness for are social bookmarking services. The problem is, though, that they are full of problems. Either they are buggy or too slow, or they lack useful features (read: necessary features non-existent). It's almost as though most people in the KM or Knowledge Management field are not always the best software developers and great software developers are not always the most well-read in terms of KM practises, esp. the knowledge management problems knowledge workers encounter on a day-to-day basis. :relaxed:

## [BACK TO INDEX OF REPOSITORIES] (https://github.com/antiface/Index)

[A.G. (c) 2016. ![A.G. (c) 2016. All Rights Reserved]
(https://historiotheque.files.wordpress.com/2016/11/ag_signature_official_2015_50px_cropped.jpg) All Rights Reserved.](http://alexgagnon.com)
