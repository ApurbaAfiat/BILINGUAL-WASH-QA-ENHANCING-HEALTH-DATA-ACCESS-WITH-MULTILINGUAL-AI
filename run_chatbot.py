import sys
import os
from bangla_to_english import query_qa

# Ensure console prints UTF-8 correctly on Windows
if os.name == "nt":
    import ctypes
    ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("=" * 60)
    print("      🌟 JMP WASH Dataset RAG Chatbot 🌟      ")
    print("=" * 60)
    print("Loading chatbot engine... (Please wait)")
    
    # Trigger initial load of bangla_to_english (will print cache messages)
    try:
        query_qa("test", top_k=1)
    except Exception as e:
        print(f"Error initializing chatbot engine: {e}")
        return
        
    print("\nChatbot is ready! You can ask questions in Bangla or English.")
    print("Type 'exit' or 'quit' to close the chatbot.\n")
    print("-" * 60)

    while True:
        try:
            query = input("\nYou: ").strip()
            if not query:
                continue
            if query.lower() in ['exit', 'quit']:
                print("\nGoodbye! Have a great day!")
                break

            print("\nBot is thinking...")
            response = query_qa(query)
            print(f"\nBot:\n{response}")
            print("-" * 60)

        except KeyboardInterrupt:
            print("\n\nGoodbye! Have a great day!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("-" * 60)

if __name__ == "__main__":
    main()
