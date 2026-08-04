After a couple of weeks of vacation after I left Google, it was time
to start my new job. The research lab I joined was called Recruit
Institute of Technology at the time, and only later it changed its
name to Megagon Labs. The lab had an office in Tokyo and another one
in Mountain View.

After Google, it was a bit of a shock to have to build software
without any of the technologies I had come to depend on. But the
hardest change for me was no longer being able to see my code running
at scale, in a production environment. This being a research lab, all
the code we wrote were of the proof-of-concept variety, which is a
very different animal. Still, the projects were interesting: for a
starter project I got to build a query language compiler and execution
engine for a system that extracted entities from text; then I worked
on a text classifier for a real estate application, a chatbot
assisting a hotel concierge with typical questions from guests, and
another one for ranking restaurants, hotels and tourist attractions on
subjective criteria.

A few months into my new job, Alon mentioned that the lab was going to
get a new name: they had involved an external company specialized in
naming companies (yes, such companies exist!), they created a short
list of candidate names, and they picked one: Megagon. What is a
megagon? Glad you asked: it's a regular polygon with one million
edges! Looks indistinguishable from a circle, like the red one in the
Japanese flag which symbolizes the raising Sun. The symbolism here was
something like this: we are working on systems that are approximating
human behavior so well as to be indistinuishable from real people. I
remember Alon telling us to keep the name secret from everyone,
including our families, until it was officially announced. It was a
great name, not yet used, and we didn't want anyone else to snatch it!

Soon after the new name was official, Megagon Labs became a platinum
sponsor for VLDB (the conference on Very Large Databases), which was
going to take place in Rio de Janeiro, Brazil. We had a couple of
accepted papers at VLDB, including the one on the text extraction
system I had worked on, so we all got to go! I even took Maria with
me (I just had to pay for her plane ticket and student registration). 


Pretty soon I realized that one of the major initiatives was
developing a chatbot aiming to apply positive psychology techniques to
improve wellbeing. Alon's vision was to build a chatbot that learned
about you and gently nudges to do more activities that are known to
make you happier: excercise, socialize, get involved in your
community, eat healthy, spend time in nature, etc. Back in 2016, years
before ChatGPT, this was a very ambitious goal, and we just didn't
have the critical mass to pull it off.

The chatbot user interface and backend was being outsourced to
contractors overseas, while the researchers onsite were focusing on
the natural language understanding component. Both were advancing
quite slowly at the time. I remember we were having a team lunch and I
couldn't keep quiet anymore and I said:

"The overseas developers are moving at a snail-pace, they deliver low
quality code, badly designed and buggy, and at this pace, we'll never
have a chatbot ready to release."

Everybody got quiet: they were all aware of this, but nobody dared to
put it so bluntly. I was new to the team, and I dind't know the full
history, but it was quite obvious, I thought. Alon then looked at the
team lead and asked her if this was true. She nodded.

"Well then, George, can you build it?", Alon challenged me.

"I can build the backend, storage and API endpoints myself but I need
someone to help me build the iPhone app; and that person would need to
work here, on-site, side by side with me", I said.

"Very well", Alon said, "we'll hire an iOS developer onsite and ditch
the contractors. You have six months to build everyting, can you do
it?"

"Definitely!", I replied, even though I only had a high-level idea of
the architecture of such a system, and I had never before built such a
thing.

The next week we interviewed three iOS engineers and hired an
ambitious Economics major who had just graduated top of his class from
a coding bootcamp for iOS developers (his instructor recommended him
to us). I had a very good feeling about him during the interview, and
I wasn't wrong. John took the desk next to mine and we worked side by
side: we agreed on a protocol for the communication with the backend
and we refined it over time, testing every change in the app.

I still had to build the database layer, and the API server and figure
out how to deploy them on the AWS cloud using Kubernetes (so clunky,
compared to Borg), but in a few months we had a functional system we
could iterate on, and integrate the natural language understanding
component.

At some point a group of senior people from the Tokyo lab came to
visit and one of them invited me to a small conference room for a
private meeting. I had some idea that the Tokyo leadership was not
fully on board with this happiness chatbot project, but I wasn't
prepared for the directness of the conversation that followed:

"George, why are you working on this? It's a useless idea, this will
never work in Japan. Recruit will never release something like this."

"Why are you asking me?", I replied. "This is a project that started
before I joined, I noticed it moved too slow with the offshore
contractors, and I took it on. I am just doing my job, as directed by
our CEO. If you have a problem, you should ask him."

"Yes, we know all that, but why waste your talent on something useless
like this?"

"First of all, Positive Psychology is a respectable science with real
results. Second, I view this as a vehicle for advancing natural
language understanding. If we can pull this off, we can then use the
natural language technology for pretty much anything, including
matching job seekers with opportunities, which is Recruit's main
business", I said.

He wasn't convinced, but we ended the conversation there. I took Alon
aside the next day and told him everything. I ended with "Are you sure
Recruit will continue to fund this project?" Alon assured me that he
has complete autonomy on the research direction of the lab and said
that the Japanese senior enginner overstepped his authority.

Not too long after this exchange, both Alon and I left Megagon
Labs. Most of the other senior researchers and engineers left within
the year.


