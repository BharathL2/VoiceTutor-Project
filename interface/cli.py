# CLI interface
from agents import router_agent, summarizer_agent, explainer_agent, quiz_agent, tts_agent

def start_cli():
    print("Welcome to VoiceTutor!")
    while True:
        user_input = input("\n🎙️ You: ")

        intent = router_agent.route_intent(user_input)

        if intent == "summarizer":
            response = summarizer_agent.summarize(user_input)
        elif intent == "explainer":
            response = explainer_agent.explain(user_input)
        elif intent == "quiz":
            response = quiz_agent.generate_quiz(user_input)
        else:
            response = "Sorry, I didn't understand that."

        print(f"🧠 VoiceTutor: {response}")
        tts_agent.speak(response)
