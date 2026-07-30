
Deciding to move was easy, actually doing it was harder than I
thought. First of all, while it was true that internal transfers were
possible, they weren’t as easy as just asking to move. One had to find
a team to join in the other office. To facilitate that, there was an
internal website where managers could post open positions for internal
transfers. I spent weeks scouring those listings, and got some calls,
but none of them materialized into an offer. I needed to expand my
search. It so happens that around that time I got contacted by a
recruiter from Netflix for a job opening in Los Gatos. I wasn’t really
looking to leave Google, but I figured an interview in California
could be fun. Especially if I could combine the trip with a visit to
the Google office.

I told my manager I’m going to California to visit a friend (which was
true, we visited Roxana too), and while I’m there I could meet with
the researchers we were working with for our project. So, one rainy
day in early May 2012, I took Grațiela and our nine months old
daughter Xenia to with me to Mountain View to soft launch my
California dream! We stayed at a nice hotel and while I was
interviewing at Netflix or at the office, they explored the downtown
area on foot. The Netflix interview didn’t work out, but my visit to
the Google Research office paid off: I got to meet the researchers
that designed that great question answering system we integrated into
Google Search. We talked at length about ways we could improve the
system, new scoring signals we could use, how to add normalization,
how to account for missing features, and other ideas. The net result
was that when their manager visited the New York office a few weeks
later he asked to meet with me. My manager had also reached out to him
to let him know I am looking for opportunities in the Mountain View
office. The way he put it to me was: “If life hands you lemons, make
lemonade: I don’t want to lose you, but if you’re going to move to
California, at least we can continue to work together in the same
project.” Separately, Alon Haley also visited the New York office and
we had coffee together, and I mentioned to him that I would love to
transfer to that team. He was a research director then, in a close
area, and knew the question answering people well, they were working
in the same building. I don’t know what he told his peer about me, but
the net result was that my transfer was fast-tracked! We set my move
day for August 15.

We packed all our belongings into a moving container, and then all six
of us got in our Toyota Highlander and took the highway 80 to the West
Coast! We took our time, never driving more than eight hours each day
and got there in a week, checking into hotels along the way whenever
we got tired. Our older daughters had a blast, they were already used
to long road trips from our yearly drives to Florida. The youngest one
got a lot of sleep, so she was fine too. In fact, she turned one
halfway through: we had a mini birthday party for her when we stopped
for lunch. When we got to Utah, in the mountains, we almost couldn’t
find a room, it was packed with tourists.

The next day we got back in the car, drove for a while, and just when
we were in the middle of the Boneville Salt Flats, Xenia choked on
something and started turning blue. Gratiela paniked and kept asking
me to go to the ER, except there was nothing around us for
miles. Luckily, she coughed it out and turned pink again!

We finally arrived in Milpitas, California, where I had found a
four-bedroom house to rent. We got there before the shipping container
(yes, just like in “Inside Out”), and had to sleep on inflatable
mattresses for the first few days. Why Milpitas, you ask? Well, on the
map it looked like it was pretty close to Mountain View and it was the
only place we could afford for a house of that size. We had sold our
Yorktown Heights house at a loss (we had paid $415,000 in 2003, and we
sold it for $299,000 in 2012, a few years after the sub-prime mortgage
crash). 

We enjoyed our stay in Milpitas, especially the inexpensive and
delicious Asian food there, but pretty soon we realized that the
schools were not that great, despite being reasonably well rated on
greatschools.com. The stress caused by moving the kids to a worse
school was weighing on me pretty heavily. Grațiela and I decided we
needed to move to a better school district for our kids. So we went
back online to look for houses to rent. Eventually we found a three
bedroom townhouse at the Southern edge of Palo Alto for under $4,000 a
month. The catch: absolutely no maintenance in the rental contract,
whatever broke we would be responsible for fixing it ourselves. The
place was also significantly smaller than the Milpitas home, but it
had a large back yard; most importantly, though, it allowed our kids
to enroll in Palo Altos public schools, widely considered one of the
best school districts in the country. So, only six months after we
moved to Milpitas, we moved again. We had to pay a penalty for
breaking the one year lease early, but it was worth it: we got our
daughters into good schools and my commute became walking distance! I
actually started walking or cycling to the office almost every day, an
amazing improvement after the two-hour commute to the New York office!

At work, the project was going well, we were still meeting with my
former teammates regularly over videoconference, with me working
inside the Research team this time. It seemed to be everything I ever
wanted from a Research position, but with actual product impact. That
arrangement didn’t last long, it did however morph into something
better, although I didn’t quite see it at the time. Let me explain.

It started with one of the engineers in the Research team announcing
his transfer into a product team within Search. It was a team that was
planning to develop a long-form question answering system, that is, a
system that would answer in complete sentences, not just short factual
answers to entity-attribute queries.  A few days after that, we got
invited to a meeting with the architect of that new system on neutral
ground, in a meeting room half-way across the campus, between the
Research building and the Search building, on Shoreline boulevard. It
was a momentous and consequential moment, although I had no idea at
the time. A couple of days later, the manager of that team came to see
me and ask me if I would like to join his team. As I had just
transferred into my current team, I declined, saying that I quite
enjoyed working with my new team, and also that I would have to
consult with my manager. That’s when he clarified: “Oh, I already
spoke to your manager, your entire team is joining our project.”

That completely changed the situation: unbeknownst to me, there was a
Google-wide effort underway to “embed” researchers into the product
teams, to have them work side by side with the software engineers to
build products. A totally reasonable idea, in my opinion, as I had
already seen the challenges of keeping Research separate from
Engineering in IBM’s case. The best way it was described to me was
that trying to get research ideas into production as like pushing on a
rope: it only works if the other party (Engineering) is pulling. So,
we all moved into the Search Division and got assigned to this new
project. Of course, short answers would get incorporated into the long
answers, and our short answer candidates would be a critical signal
for scoring the candidate sentences. There was a lot more that needed
to be figured out though. So the team grew more, and many different
subsystems were developed to realize this vision.

I learned a lot during that process: I remember our new manager coming
to our desks to ask why our experimental system was giving a wrong
answer, and we didn’t have an easy way to answer that. “We would need
to add some debugging print statements, compile the code, and run it
again to trace the exact scores produced by the subsystems”. “No”, he
said, “I know you can do that for this particular case, but I want to
be able to debug the scoring myself anytime I see a wrong answer”. It
hadn’t occurred to me that a simple observability change like this
could be so valuable. So we set out to add a detailed “debug mode”
internal URL parameter he could use anytime and get a detailed view of
each and every scoring signal computed by the system for any given
query. In retrospect, we should have thought about that. It reminded
me of my manager from my first job in Toronto who was always telling
us to “never build something that you can’t monitor”.

The system grew more and more complex over time, but with each quality
improvement it became slower and slower, to the point where it was
frequently exceeding the timeout of 100 milliseconds the Google search
process allocated to our question answering system. Unfortunately, a
system that could give great answers but times out is not very useful,
so a new team was formed to address this. A manager with a good track
record of radical performance improvements started looking for
engineers to work on this. He approached me with a small challenge:
cut the running time of one of the scoring systems. I don’t remember
now what I did, but he asked me to join his team. We first tried the
usual tricks: run the scoring systems in parallel to reduce the
overall wall clock time. That helped somewhat, at the expense of using
more CPU cores, which would sit idle between requests. Not a very
efficient use of resources. The cloud managers came after us soon
enough, our CPU utilization was abysmal. Our manager then made an
aggressive bet: “Give me three engineers for six months, and we’ll
reduce the running time from the current median of 80 milliseconds
running in parallel on 8 CPU cores, to 10 milliseconds running
single-threaded on a single core!”. Nobody believed him, but he was
given the time to try. The thinking was that even if we managed to
accomplish half that goal it would still solve the timeout issues.

Not to brag, but under his guidance, we managed to completely
re-implement all the scoring systems in a more efficient way by using
numerical token identifiers everywhere instead of strings, and the
resulting system did accomplish a 10 millisecond median running time
on a single core. That allowed us to drastically improve the CPU
utilization and run well under the timeout threshold for all
queries. Enormously satisfying project!