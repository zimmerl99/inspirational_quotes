from fastapi import FastAPI
import random

quotes_list = [ 
" 'The only thing we have to fear is fear itself.' — Franklin D. Roosevelt ",
" 'In the middle of difficulty lies opportunity.' — Albert Einstein ",
" 'Not all those who wander are lost.' — J.R.R. Tolkien ",
" 'Act as if what you do makes a difference. It does.' — William James ",
" 'The secret of getting ahead is getting started.' — Mark Twain ",
" 'Happiness depends upon ourselves.' — Aristotle ",
" 'Well done is better than well said.' — Benjamin Franklin ",
" 'What you do speaks so loudly that I cannot hear what you say.' — Ralph Waldo Emerson ",
" 'Where there is love there is life.' — Mahatma Gandhi ",
" 'No one can make you feel inferior without your consent.' — Eleanor Roosevelt ",
" 'Courage is grace under pressure.' — Ernest Hemingway ",
" 'The future belongs to those who believe in the beauty of their dreams.' — Eleanor Roosevelt ",
" 'You must be the change you wish to see in the world.' — Attributed to Gandhi ",
" 'Nothing will work unless you do.' — Maya Angelou ",
" 'It is never too late to be what you might have been.' — George Eliot ",
" 'Turn your wounds into wisdom.' — Oprah Winfrey ",
" 'Life is either a daring adventure or nothing.' — Helen Keller ",
" 'Energy and persistence conquer all things.' — Benjamin Franklin ",
" 'The best way out is always through.' — Robert Frost ",
" 'What lies behind us and what lies before us are tiny matters compared to what lies within us.' — Ralph Waldo Emerson ",
" 'Dream big and dare to fail.' — Norman Vaughan ",
" 'Action is the foundational key to all success.' — Pablo Picasso ",
" 'Believe you can and you’re halfway there.' — Theodore Roosevelt ",
" 'Keep your face always toward the sunshine—and shadows will fall behind you.' — Walt Whitman ",
" 'The power of imagination makes us infinite.' — John Muir ",
" 'Hope is the thing with feathers.' — Emily Dickinson ",
" 'If you want to lift yourself up, lift up someone else.' — Booker T. Washington ",
" 'The only journey is the one within.' — Rainer Maria Rilke ",
" 'Do what you can, with what you have, where you are.' — Theodore Roosevelt ",
" 'He who has a why to live can bear almost any how.' — Friedrich Nietzsche ",
" 'What we think, we become.' — Buddha ",
" 'Be yourself; everyone else is already taken.' — Oscar Wilde ",
" 'The beginning is the most important part of the work.' — Plato ",
" 'Fortune favors the bold.' — Virgil ",
" 'Adventure is worthwhile in itself.' — Amelia Earhart ",
" 'You miss 100% of the shots you don’t take.' — Wayne Gretzky ",
" 'Success is not final; failure is not fatal: it is the courage to continue that counts.' — Winston Churchill ",
" 'Knowledge is power.' — Francis Bacon ",
" 'The greatest wealth is to live content with little.' — Plato ",
" 'The soul becomes dyed with the color of its thoughts.' — Marcus Aurelius ",
" 'Life is really simple, but we insist on making it complicated.' — Confucius ",
" 'The mind is everything. What you think you become.' — Buddha ",
" 'To live is the rarest thing in the world.' — Oscar Wilde ",
" 'Everything you can imagine is real.' — Pablo Picasso ",
" 'What you seek is seeking you.' — Rumi ",
" 'Be the master of your will and the slave of your conscience.' — Attributed to Aristotle ",
" 'A goal without a plan is just a wish.' — Antoine de Saint-Exupéry ",
" 'In three words I can sum up everything I’ve learned about life: it goes on.' — Robert Frost ",
" 'The measure of intelligence is the ability to change.' — Albert Einstein ",
" 'The glow of one warm thought is worth more than money.' — Thomas Jefferson "
]

app = FastAPI()

# GET REQUESTS

@app.get("/")              #when the root is visited it calls read root
def read_root():
    return {"message": "Quotes API up and running"}


@app.get("/quotes")
def get_quote():
    try:
        quote = random.choice(quotes_list)
        return {"data": quote}
    
    except Exception:
        return {"error with getting quote"}