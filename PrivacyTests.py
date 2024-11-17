import json
from collections import defaultdict

def count_passed_tests(data):
    passed_count = 0
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "passed" and value is True:
                passed_count += 1
            else:
                passed_count += count_passed_tests(value)
    elif isinstance(data, list):
        for item in data:
            passed_count += count_passed_tests(item)
    return passed_count

file_categories = {
    "index.json": "Desktop Browsers:",
    "private.json": "Desktop Private Mode:",
    "ios.json": "iOS Browsers:",
    "android.json": "Android Browsers:",
    "nightly.json": "Nightly Build:",
    "nightly-private.json": "Nightly Private Mode:"
}

category_winners = {}
winner_counts = defaultdict(int)

for filename, category in file_categories.items():
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            results = {}

            for browser_data in data["all_tests"]:
                browser_name = browser_data["browser"]
                results[browser_name] = count_passed_tests(browser_data)
            print(f"\n{category}")
            sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

            if sorted_results:
                winner_browser, winner_count = sorted_results[0]
                category_winners[category] = {
                    "browser": winner_browser,
                    "count": winner_count
                }
                winner_counts[winner_browser] += 1

            for index, (browser, count) in enumerate(sorted_results, start=1):
                print(f"{index}. {browser.title()}: {count}")

            if sorted_results:
                print(f"\nWinner: {winner_browser.title()} 🌟")

    except FileNotFoundError:
        print(f"\n{category}")
        print(f"File {filename} not found")
        
    except Exception as e:
        print(f"\n{category}")
        print(f"Error processing {filename}: {str(e)}")
print("\nWin Count Breakdown:")

sorted_win_counts = sorted(winner_counts.items(), key=lambda x: x[1], reverse=True)

for browser, wins in sorted_win_counts:
    print(f"{browser.title()}: {wins} {'win' if wins == 1 else 'wins'}")

if winner_counts:
    max_wins = max(winner_counts.values())
    overall_winners = [browser for browser, wins in winner_counts.items() if wins == max_wins]
    print("\nOverall Winner:", end=" ")

    if len(overall_winners) == 1:
        print(f"{overall_winners[0].title()} 🏆")
    else:
        print("Tie between " + " and  🪢".join(winner.title() for winner in overall_winners))
