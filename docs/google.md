
I started my new job at Google in December 2010, ten years after I rejected
their first offer. After actually experiencing the day to day life of a
researcher, I was now going full circle to an engineering position, the very
same role I snubbed for so many years. A few words of explanation are in order:
why now, what had changed? Many things, but most importantly my own
attitude. You see, throughout college and graduate school I had been conditioned
to value "science" above "mere engineering". Coding was something I picked
up early, on my ZX Spectrum back in the eighties, and it felt easy; research, on
the other hand, was actually hard, and writing and endlessly rewriting
conference papers was harder. 

I was confusing difficulty with value. On honest reflection, a lot of the
research I was involved in was not very impactful: it led to conference
publications and patents, all right, but how many of those ideas actually made
it into actual products that people used? Not many. You see, I had this nagging
feeling that my effort was largely irrelevant, removed as I was from production.

This was what made the Google offer so attractive: I was finally going to
directly contribute to a product used every day by so many people.

And Google understood how to curate an exciting and fun on-boarding experience
for the new hires, which in turn allowed people to become productive faster. Let
me explain: on the first day we were given a tour of the office, complete with
gourmet breakfast and coffee, and for the first two weeks we had no work
assignments, other than attending classes on the Google internal systems, such
as "Life of a Google Query" (a high-level systems view of query processing),
"Life of a Dollar" (an overview of Google Ads), "Your first Change List" (how to
use the Google internal source control system), "Word count with MapReduce" (how
to use the massively parallel computing environment to process large amounts of
data quickly), "Borg" (the internal cloud infrastructure), and others like
these.  It really felt like we were briefed on a highly advanced software
engineering wonderland, because that's exactly what this was! Everything was
carefully designed for maximum effect, from the playfully colored interior
design and the free food and gourmet coffee, to the design of the internal
websites we used every day. The internal classes didn't end after the first two
weeks, there were lots more hands-on "labs" available on the intranet, each one
of them personalized for each engineer, already configured to work
out-of-the-box with one's work account. 

But the thing that shocked me the most was the availability of seemingly
unlimited computing resources. Let me explain. For my starter project I was
assigned a new feature for an experimental question-answering system. The system
was designed to provide short answers to factual entity-attribute type
questions, like "What is the height of the Empire State Building?". My task was
to extend this system to also handle questions where the answer was a list, like
"What is the cast of Casablanca?". In order to do that, I had to implement a
MapReduce job to extracted lists from the Web and associate them with
entity-attribute pairs (eg. Casablanca-cast). I implemented a first solution
using what I had just learned from the introductory class and it was time to
test it. I asked a teammate if I can test it on some sample data, and he looked
at me surprised and said: 

"Why bother with sample data, just run it on the whole Web corpus.".

"Wouldn't that take a long time?", I asked. 

"No, just submit it to Borg and ask for 5,000 machines. It will be done in an
hour or so."

I could not believe it! At any other previous job, including IBM, I would need
to have a good reason to request access to a cluster of 10 servers, most of my
work was done on a single machine. Here, I could request 5,000 machines just
like that, and process the whole Web in an hour! It was amazing.

Now, that's not to say it was easy getting things done. I had not been a
professional software engineer for over 15 years now, all the coding I've done
lately was for research prototypes, working mostly on my own. Here, all the code
had to go through peer review before it could be committed into the
repository. For new hires, there was an additional "readability review", in
addition to the regular code review. To be approved, every code change I made
had to conform to the internal style guidelines, and be reviewed by an engineer
who had "readability certification" for that specific programming language. A
new hire could only apply for that certification after writing some substantial
amount of original code in that language. The justification that was often
invoked was that "source code is read by a computer only once, but it is read by humans many times". 

And the senior engineers were dead serious on not approving anything until it
was perfectly designed and thoroughly tested. As you can imagine, this slowed me
down significantly. I had my first results relatively quickly but I couldn't
merge my code for weeks. Meanwhile, the code around my pieces would change, and
I had to constantly readjust my own code to fit the new structures.

Finally, after about six months my new feature was ready to launch! I cannot
express in words the joy I experienced when I typed my first query on my
Android phone "Who are the four Beatles?" on google.com and I saw the results
prominently shown on the top of the results page!
