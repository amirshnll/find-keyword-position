from find import find_keyword_position
from read import read_json
from output import generate_csv

# show_output is True print in console, show_output is False generate csv file
show_output = False

config = read_json("keyword.json")

result = []
for keyword in config["keywords"]:
    positions = find_keyword_position(config["domain"], keyword)

    if show_output:
        print(keyword, ":")
        if positions is not None and len(positions) > 0:
            for pos, url in positions:
                print(f"Position {pos}\tPage {round(pos/10)}\tUrl {url}")
        else:
            print("No results found")
    else:
        if positions is not None and len(positions) > 0:
            for pos, url in positions:
                result.append(
                    {
                        "#": len(result) + 1,
                        "keyword": keyword,
                        "position": pos,
                        "page": round(pos / 10),
                        "url": url,
                    }
                )
        else:
            result.append(
                {
                    "#": len(result) + 1,
                    "keyword": keyword,
                    "position": "N/A",
                    "page": "N/A",
                    "url": "N/A",
                }
            )

if show_output is False:
    generate_csv("output.csv", result)
