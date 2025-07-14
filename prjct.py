import random
import os

# Detailed DSA roadmap
dsa_roadmap = [
    "1. Arrays > Introduction, Insert/Delete, Search, Sorting, Prefix Sum, Sliding Window, Two Pointers",
    "2. Strings > Slicing, Reversing, Anagrams, Palindromes, Frequency Count, Compression, Pattern Matching",
    "3. Linked Lists > Singly, Doubly, Traversal, Reversal, Cycle Detection, Merge Sorted Lists",
    "4. Stacks & Queues > Stack Ops, Balanced Brackets, Postfix Eval, Queues, Deque, Stack-Queue Conversion",
    "5. Trees > Binary Trees, BST, Traversals, Height/Depth, Level Order, LCA, Balanced Trees, Inversion",
    "6. Graphs > Adjacency Matrix/List, BFS, DFS, Cycle Detection, Connected Components",
    "7. Dynamic Programming > Recursion vs DP, Memoization, Tabulation, Common DP Patterns (Fibonacci, Knapsack, LIS)"
]

# Full Stack roadmap (kept simple here)
fullstack_roadmap = [
    "1. HTML/CSS/JS", 
    "2. Git & GitHub", 
    "3. Responsive Design", 
    "4. React (Frontend)",
    "5. Python (Flask) or Node.js", 
    "6. MongoDB or PostgreSQL", 
    "7. REST APIs", 
    "8. Deployment (Render, Netlify)"
]

completed = []

tips = [
    "💡 Tip: Don’t just learn, build small projects with every concept.",
    "🚀 Build confidence by solving 1 DSA problem daily on LeetCode or GFG.",
    "✅ Stick to the roadmap, but feel free to explore side topics.",
    "📚 Understanding > Memorizing. Practice logic.",
    "🧠 Revise often. DSA sticks when repeated!"
]

# Show roadmap
def show_roadmap(track):
    print(f"\n📘 {track} Roadmap:\n")
    roadmap = dsa_roadmap if track == "DSA" else fullstack_roadmap
    for topic in roadmap:
        status = "✅" if topic in completed else "🔲"
        print(f"{status} {topic}")

# Mark any topic as completed
def mark_complete():
    topic = input("Enter exact topic number or name to mark as complete: ").strip()
    matched = None
    for item in dsa_roadmap + fullstack_roadmap:
        if topic.lower() in item.lower():
            matched = item
            break
    if matched:
        completed.append(matched)
        save_progress()
        print(f"✅ '{matched}' marked as complete!")
    else:
        print("❌ Topic not found. Please try again.")

# Show what’s completed
def view_completed():
    print("\n🎉 Completed Topics:")
    if not completed:
        print("No topics completed yet.")
    for topic in completed:
        print("✅", topic)

# Save to file
def save_progress():
    with open("progress.txt", "w") as f:
        for topic in completed:
            f.write(topic + "\n")

# Load saved progress
def load_progress():
    if os.path.exists("progress.txt"):
        with open("progress.txt", "r") as f:
            for line in f:
                completed.append(line.strip())

# Random motivational tip
def show_tip():
    print("\n💡", random.choice(tips))

# Main menu loop
def menu():
    load_progress()
    while True:
        print("\n🧑‍💻 Welcome to Tech Path Buddy")
        print("1. View DSA Roadmap")
        print("2. View Full Stack Roadmap")
        print("3. Mark Topic as Completed")
        print("4. View Completed Topics")
        print("5. Show Random Tip")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            show_roadmap("DSA")
        elif choice == "2":
            show_roadmap("Full Stack")
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            view_completed()
        elif choice == "5":
            show_tip()
        elif choice == "6":
            print("👋 Bye! Keep learning and building.")
            break
        else:
            print("❌ Invalid choice. Try again.")

menu()