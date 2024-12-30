3. System Design and Architecture
3.1.OVERVIEW OF THE SYSTEM
At the core of GestureSpeakAI lies its ability to turn air writing into spoken
communication. To achieve this goal, multiple technologies including gesture
recognition, language processing and speech synthesis work together
seamlessly in real time to provide instantaneous translation and answer
generation - giving users instantaneous answers they can hear! Let's examine
each component.
3.2.SYSTEM ARCHITECTURE
The GestureSpeakAI system consists of three primary components:
• Gesture Recognition Module
• Language Processing Module
• Speech Synthesis Module
These interdependent components form a system which transforms air-written
gestures into audible communication. Below is a high-level view of how it all
works.
19
3.3.GESTURE RECOGNITION MODULE
At the outset of any process is recognising gestures made by users in the air.
This is accomplished using cameras or sensors such as webcams that capture
hand movements made by the user and utilize computer vision techniques to
track hands as they trace patterns over an image in space.
To interpret these air-written gestures, we utilize a Convolutional Neural
Network (CNN), which excels at recognizing patterns. The CNN is then trained
to identify letters and words from hand movements captured during capture; so
when someone writes "Hello" aloft in the air, our system recognizes each letter
individually before turning them into text - making recognition as accurate and
speedy as possible so users don't have to wait long for their input to be
recognized by us.
3.4.LANGUAGE PROCESSING MODULE
Once the system has recognized text from air-writing, it's sent onward to the
Language Processing Module of the system for further processing by AI - here,
the recognized text is processed using an LLM like GPT which recognizes it
20
and generates relevant responses based on what's read from input and process
it accordingly.
LLMs are truly remarkable machines because of their ability to understand not
just words but also context behind them. If a user writes "What's the weather
today?", an LLM can recognize this as a question and provide an appropriate
response. Furthermore, GestureSpeakAI was developed specifically with this
in mind so as to cover many topics so as to respond effectively in various
scenarios; whether answering general knowledge queries or helping with
everyday tasks.
3.5.SPEECH SYNTHESIS MODULE
At this point, the Speech Synthesis Module plays a critical role in turning text
responses from LLMs into speech. Employing advanced Text-to-Speech (TTS)
technology like Taco Tron or Wave Net, the system takes the generated
response and transforms it into natural-sounding speech output.
At its heart lies the goal of producing speech as clear and lifelike as possible,
so that when speaking to it feels as if talking directly to a real person. To
accomplish this goal, the TTS engine not only converts text into speech but
also adds natural intonations, pauses, and variations in tone to make the voice
engaging - this feature being especially crucial for users reliant on this system
as their primary means of communication, as it ensures interactions feel
humane and comfortable.
3.6.SYSTEM WORKFLOW
Here's how GestureSpeakAI works step-by-step:
1. User Input: The user enters their message into GestureSpeakAI by writing it
aloft with their hand or pen in the air.
2. Gesture Detection and Recognition Module (GRM): A camera captures hand
movements which the GRM translates into text.
3. Text Processing: Once text recognition has been complete, the recognized
text is passed along to the Language Processing Module where an LLM
generates a response that meets user criteria.
21
4. Speech Synthesis Module transforms this response into spoken words which
users can hear directly.
Users are ensured an effortless communication experience while the system
handles everything behind-the-scenes.
3.7.HARDWARE AND SOFTWARE RE
